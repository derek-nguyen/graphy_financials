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
from issuer_info ii