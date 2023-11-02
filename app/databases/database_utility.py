import psycopg2
import psycopg2.extras as extras
from google.cloud import storage, bigquery

def get_db_connection():
    return psycopg2.connect(
    database="graphyfinancials",
    host="localhost",
    user="derek",
    password="",
    port="5432"
)

def query_google_bq(query: str): 
    client = bigquery.Client()
    query_job = client.query(query)
    rows = query_job.result()
    return rows

def insert_into_db(conn, df, table:str):
    tuples = [tuple(x) for x in df.to_numpy()]
    cols = ','.join(list(df.columns))
    
    print(tuples)
    query = "INSERT INTO %s(%s) VALUES %%s" % (table,cols)
    cursor = conn.cursor()
    try:
        extras.execute_values(cursor, query, tuples)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("error", error)
        conn.rollback()
    finally:
        cursor.close()
    print("the dataframe is inserted")
    cursor.close()

for row in query_google_bq('select * from main.financials'):
    print(row)