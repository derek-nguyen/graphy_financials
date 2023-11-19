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
    
    return companies_list

async def get_company(cik: str):
    query = f"""
    select *
    from graphy-financials.main.companies
    where 1=1
    and cik = '{cik}'
    """
    
    query_job = client.query(query)
    results = query_job.result()
    
    company_dict = None
    for company in results:
        try:
            company_dict = dict(company)
        except Exception as e:
            print('Error converting to dictionary',e)
    
    if not company_dict:
        return {'Error': 'No company found'}
    else:
        return company_dict
    
async def get_company_financials(cik: str):
    query = f"""
    select *
    from graphy-financials.main.financials
    where 1=1
    and cik = '{cik}'
    """
    
    query_job = client.query(query)
    results = query_job.result()
    
    financials_list = []
    
    for financial in results:
        financial_dict = dict(financial.items())
        financials_list.append(financial_dict)
    return financials_list

# print(get_company_financials('1882217'))
# print(get_company('1882217'))