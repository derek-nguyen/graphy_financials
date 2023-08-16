import psycopg2
import psycopg2.extras as extras

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