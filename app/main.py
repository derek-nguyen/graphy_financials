from fastapi import FastAPI, APIRouter

app = FastAPI()

company_router = APIRouter()

# Root route
@app.get('/')
async def root():
    return {'message': 'Hello World!'}

# Subrouter route for /company
@company_router.get('/')
async def get_all_company():
    return {'Company': 'All'}

app.include_router(company_router, prefix='/company')
