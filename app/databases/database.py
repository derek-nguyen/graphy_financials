import psycopg2 
from database_utility import get_db_connection

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
        CREATE TABLE disclosures (
            accession_number VARCHAR(255),
            compensation_amount_description TEXT,
            financial_interest TEXT,
            security_offered_type VARCHAR(255),
            security_offered_other_desc text,
            no_of_security_offered float,
            price numeric(10,2),
            price_determination_method TEXT,
            offering_amount FLOAT8,
            oversubscription_accepted TEXT,
            oversubscription_allocation_type TEXT,
            desc_oversubscription TEXT,
            maximum_offering_amount VARCHAR(255),
            deadline_date DATE,
            current_employees int,
            total_assets_most_recent_fiscal_year FLOAT8,
            total_assets_prior_fiscal_year FLOAT8,
            cash_equity_most_recent_fiscal_year FLOAT8,
            cash_equity_prior_fiscal_year FLOAT8,
            act_received_recent_fiscal_year FLOAT8,
            act_received_prior_fiscal_year FLOAT8,
            short_term_debt_recent_fiscal_year FLOAT8,
            short_term_debt_prior_fiscal_year FLOAT8,
            long_term_debt_recent_fiscal_year FLOAT8,
            long_term_debt_prior_fiscal_year FLOAT8,
            revenue_most_recent_fiscal_year FLOAT8,
            revenue_prior_fiscal_year FLOAT8,
            cost_goods_sold_recent_fiscal_year FLOAT8,
            cost_goods_sold_prior_fiscal_year FLOAT8,
            tax_paid_most_recent_fiscal_year FLOAT8,
            tax_paid_prior_fiscal_year FLOAT8,
            net_income_most_recent_fiscal_year FLOAT8, 
            net_income_prior_fiscal_year FLOAT8
        );
        
        CREATE TABLE coissuer_info (
            accession_number VARCHAR(255),
            id int,
            is_edgar_filer VARCHAR(255),
            co_issuer_cik VARCHAR(255),
            name_of_co_issuer VARCHAR(255),
            legal_status_form VARCHAR(255),
            legal_status_other_desc VARCHAR(255),
            jurisdiction_organization VARCHAR(255),
            date_incorporation DATE,
            street_1 VARCHAR(255),
            street_2 VARCHAR(255),
            city VARCHAR(255),
            state_or_country VARCHAR(255),
            zipcode VARCHAR(20),
            co_issuer_website VARCHAR(255)
        );
        
        CREATE TABLE issuer_info (
            accession_number           VARCHAR(255),
            is_amendment               VARCHAR(20),
            progress_update            TEXT,
            nature_of_amendment        TEXT,
            name_of_issuer             VARCHAR(255),
            legal_status_form          VARCHAR(255),
            legal_status_other_desc    VARCHAR(255),
            jurisdiction_organization  VARCHAR(255),
            date_incorporation         DATE,
            street1                    VARCHAR(255),
            street2                    VARCHAR(255),
            city                       VARCHAR(255),
            state_or_country           VARCHAR(255),
            zipcode                    VARCHAR(20),
            issuer_website             VARCHAR(255),
            company_name               VARCHAR(255),
            commission_cik             VARCHAR(255),
            commission_file_number     VARCHAR(255),
            crd_number                 NUMERIC,
            is_co_issuer               VARCHAR(255)
        );
        
        CREATE TABLE submission (
            accession_number  VARCHAR(255),
            submission_type   VARCHAR(255),
            filing_date       DATE,
            cik               VARCHAR(255),
            file_number       VARCHAR(255),
            period            DATE
        )
        """
        )

def dropTables():
    cursor.execute(
        """
        DROP TABLE IF EXISTS disclosures;
        DROP TABLE IF EXISTS coissuer_info;
        DROP TABLE IF EXISTS issuer_info;
        DROP TABLE IF EXISTS submission;
        """
        )
    
def buildTables():
    dropTables()
    createTables()

buildTables()
conn.commit()