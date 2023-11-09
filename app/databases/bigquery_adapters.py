import json
from typing import Any
from google.cloud import bigquery
from datetime import date

client = bigquery.Client()

async def get_all_companies():
    query = """
    select * 
    from graphy-financials.main.companies
    """
    
    query_job = client.query(query)
    results = query_job.result()
    
    companies_list = []
    
    for company in results:
        company_dict = dict(company.items())
        companies_list.append(company_dict)
    
    companies_json = json.dumps(companies_list, default=str)
    return companies_json