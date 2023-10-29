from database_utility import get_db_connection
from google.cloud import bigquery

conn = get_db_connection()

# conn = psycopg2.connect(
#     database="graphyfinancials",
#     host="localhost",
#     user="derek",
#     password="",
#     port="5432"
# )

cursor = conn.cursor()

def createTables():
    cursor.execute(
        """
        create table companies (
            company_title varchar(255),
            street_1 varchar(255),
            street_2 varchar(255),
            city varchar(255),
            state_or_country varchar(255),
            zipcode varchar(255),
            website varchar(255),
            cik varchar(255),
            date_incorporation date
        );
        
        create table financials (
            cik varchar(255),
            revenue float,
            cogs float,
            tax float,
            total_assets float,
            cash_equity float,
            act_received float,
            short_term_debt float,
            long_term_debt float
        )
        """
        )

def dropTables():
    cursor.execute(
        """
        drop table if exists companies;
        drop table if exists financials;
        """
        )
    
def buildLocalTables():
    print('Dropping tables')
    dropTables()
    print('Finished dropping tables')
    print('Building tables')
    createTables()
    print('Finished building tables')

buildLocalTables()
conn.commit()