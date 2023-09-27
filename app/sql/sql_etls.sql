create table issuer_info as
select 
distinct name_of_issuer as company
, case when legal_status_form = 'NaN' then null else legal_status_form end as legal_status_form  
, case when date_incorporation = '1900-01-01' then null else date_incorporation end as date_incorporation  
, case when street1 = 'NaN' then null else street1 end as street1  
, case when street2 = 'NaN' then null else street2 end as street2  
, case when city = 'NaN' then null else city end as city 
, case when state_or_country = 'NaN' then null else state_or_country end as state_or_country  
, case when zipcode = 'NaN' then null else zipcode end as zipcode  
, case when issuer_website = 'NaN' then null else issuer_website  end as issuer_website  
, commission_cik as cik 
from sandbox_issuer_info sii;


-- FLATTENS COMPANY INFO TABLE
create table companies 
as
with company as (
	with dup_company as (
		select 
		distinct name_of_issuer as company
		, case when legal_status_form = 'NaN' then null else legal_status_form end as legal_status_form  
		, case when date_incorporation = '1900-01-01' then null else date_incorporation end as date_incorporation  
		, case when street1 = 'NaN' then null else street1 end as street1  
		, case when street2 = 'NaN' then null else street2 end as street2  
		, case when city = 'NaN' then null else city end as city 
		, case when state_or_country = 'NaN' then null else state_or_country end as state_or_country  
		, case when zipcode = 'NaN' then null else zipcode end as zipcode  
		, case when issuer_website = 'NaN' then null else issuer_website  end as issuer_website  
		, commission_cik as cik 
		from temp_issuer_info sii
	)
	select 
	company
	, max(legal_status_form) as legal_status_form  
	, max(date_incorporation) as date_incorporation 
	, max(street1) as street1 
	, max(street2) as street2 
	, max(city) as city
	, max(state_or_country) as state_or_country 
	, max(zipcode) as zipcode 
	, max(issuer_website) as issuer_website 
	, max(cik)::text as cik
	from dup_company
	group by 1
)
select * 
from company 

-- REMOVED DUPLICATES
with dedup_companies as (
	select 
	*
	, row_number() over (partition by cik) as rn
	from companies c 
	where 1=1
	order by rn asc
)
select distinct 
	dc.name_of_issuer
	, coalesce(dc.street1, c.street1) as street1 
	, coalesce(dc.street2, c.street2) as street2 
	, coalesce(dc.city, c.city) as city
	, coalesce(dc.state_or_country, c.state_or_country) as state_or_country 
	, coalesce(dc.zipcode, c.zipcode) as zipcode 
	, coalesce(dc.issuer_website, c.issuer_website) as issuer_website 
	, coalesce(dc.cik, c.cik) as cik
	, coalesce(dc.date_incorporation, c.date_incorporation) as date_incorporation 
from dedup_companies dc
left join companies c on c.cik = dc.cik
where 1=1 
and rn=1

-- CLEANED SUBMISSION TABLE
drop table if exists submission
create table submission 
as
select 
	accession_number 
	, submission_type 
	, filing_date::date
	, cik 
	, file_number 
	, case when "period" = '1900-01-01' then null else "period" end as "period" 
from temp_submission ts


-- CREATE PRODUCTION FINANCIAL DISCLOSURES
drop table if exists financial_disclosures
create table financial_disclosures
as
select *
from temp_disclosures td 

-- CONSOLIDATED FINANCIAL INFORMATION
with consolidated_disclosures as (
	select d.accession_number
	, s.filing_date
	, date_trunc('year',s.filing_date)::date as filing_year
	, s.cik
	, d.compensation_amount_description
	, d.financial_interest
	, d.security_offered_type
	, d.security_offered_other_desc
	, case when d.no_of_security_offered = 'NaN' then null else d.no_of_security_offered end as no_of_security_offered
	, case when d.price = 'NaN' then null else d.price end as price
	, d.price_determination_method
	, case when d.offering_amount = 'NaN' then null else d.offering_amount end as offering_amount
	, d.oversubscription_accepted
	, d.oversubscription_allocation_type
	, d.desc_oversubscription
	, d.maximum_offering_amount
	, d.deadline_date
	, d.current_employees
	, d.total_assets_most_recent_fiscal_year
	, d.total_assets_prior_fiscal_year
	, d.cash_equity_most_recent_fiscal_year
	, d.cash_equity_prior_fiscal_year
	, d.act_received_recent_fiscal_year
	, d.act_received_prior_fiscal_year
	, d.short_term_debt_recent_fiscal_year
	, d.short_term_debt_prior_fiscal_year
	, d.long_term_debt_recent_fiscal_year
	, d.long_term_debt_prior_fiscal_year
	, d.revenue_most_recent_fiscal_year
	, d.revenue_prior_fiscal_year
	, d.cost_goods_sold_recent_fiscal_year
	, d.cost_goods_sold_prior_fiscal_year
	, d.tax_paid_most_recent_fiscal_year
	, d.tax_paid_prior_fiscal_year
	, d.net_income_most_recent_fiscal_year
	, d.net_income_prior_fiscal_year
	, s.accession_number
	, s.submission_type
	, s.file_number
	, case when s.period = '1900-01-01' then null else s.period end as fiscal_period
	, case when s."period" = '1900-01-01' then null else date_trunc('year',s."period")::date end as fiscal_year
	from temp_disclosures d 
	left join temp_submission s on s.accession_number = d.accession_number 
	where 1=1
	and d.total_assets_most_recent_fiscal_year <> 'NaN'
)
select * 
from consolidated_disclosures