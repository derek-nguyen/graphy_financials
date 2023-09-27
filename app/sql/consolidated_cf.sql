with consolidated_cf as (
	select d.accession_number
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
	, s.filing_date
	, date_trunc('year',s.filing_date)::date as filing_year
	, s.cik
	, s.file_number
	, case when s.period = '1900-01-01' then null else s.period end as fiscal_period
	, case when s."period" = '1900-01-01' then null else date_trunc('year',s."period")::date end as fiscal_year
	, ii.accession_number
	, ii.is_amendment
	, case when ii.progress_update = 'NaN' then null else ii.progress_update end as progress_update
	, case when ii.nature_of_amendment = 'NaN' then null else ii.nature_of_amendment end as nature_of_amendment
	, ii.name_of_issuer
	, ii.legal_status_form
	, case when ii.legal_status_other_desc = 'NaN' then null else ii.legal_status_other_desc end as legal_status_other_desc
	, ii.jurisdiction_organization
	, case when ii.date_incorporation = '1900-01-01' then null else ii.date_incorporation end as date_incorporation
	, case when ii.street1 = 'NaN' then null else ii.street1 end as street1
	, case when ii.street2 = 'NaN' then null else ii.street2 end as street2
	, case when ii.city = 'NaN' then null else ii.city end as city
	, case when ii.state_or_country = 'NaN' then null else ii.state_or_country end as state_or_country
	, case when ii.zipcode = 'NaN' then null else ii.zipcode end as zipcode
	, case when ii.issuer_website = 'NaN' then null else ii.issuer_website end as issuer_website 
	, case when ii.company_name = 'NaN' then null else ii.company_name end as company_name
	, case when ii.commission_cik = 'NaN' then null else ii.commission_cik end as cik
	, case when ii.commission_file_number = 'NaN' then null else ii.commission_file_number end as commission_file_number
	, case when ii.crd_number = 'NaN' then null else ii.crd_number end as crd_number
	, case when ii.is_co_issuer = 'NaN' then null else ii.is_co_issuer end as is_co_issuer
	from disclosures d 
	left join submission s on s.accession_number = d.accession_number 
	left join issuer_info ii on ii.accession_number = d.accession_number 
	where 1=1
	and d.total_assets_most_recent_fiscal_year <> 'NaN'
)
select * 
from consolidated_cf