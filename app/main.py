from fastapi import FastAPI, APIRouter,HTTPException
from databases.bigquery_adapters import get_all_companies, get_company, get_company_financials

app = FastAPI()
company_router = APIRouter()
company_financial_router = APIRouter()

# Root route
@app.get('/')
async def root():
    return {'message': 'Hello World!'}

# Subrouter route for /companies
@company_router.get('/')
async def get_all_company():
    # return {'message': 'List of companies'}
    try:
        companies = await get_all_companies()
        if not companies:
            raise HTTPException(status_code=404, detail='No companies found')
    except Exception as e:
        raise HTTPException(status_code=500)
    return companies

@company_router.get('/{cik_id}')
async def get_company_info(cik_id):
    try:
        company = await get_company(f'{cik_id}')
        return company
    except Exception as e:
        print('Error occurred while getting company details: ',e)


@company_financial_router.get('/{cik_id}')
async def get_financial_info(cik_id):
    try:
        financial_data = await get_company_financials(cik_id)
        return financial_data
    except Exception as e:
        print('Error occurred while getting financial data: ',e)

app.include_router(company_router, prefix='/companies')
app.include_router(company_financial_router,prefix='/financials')