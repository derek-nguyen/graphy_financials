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