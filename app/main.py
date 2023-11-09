from fastapi import FastAPI, APIRouter,HTTPException
from databases.bigquery_adapters import get_all_companies

app = FastAPI()

company_router = APIRouter()

# Root route
@app.get('/')
async def root():
    return {'message': 'Hello World!'}

# Subrouter route for /company
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

app.include_router(company_router, prefix='/company')