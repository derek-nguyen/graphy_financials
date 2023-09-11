from database_utility import get_db_connection

conn = get_db_connection()

def get_all_company() -> list:
    companies_list = []
    
    cursor= conn.cursor()
    query="""
            select 
            distinct name_of_issuer as company
            , legal_status_form 
            , date_incorporation 
            , street1 
            , street2 
            , city
            , state_or_country 
            , zipcode 
            , issuer_website 
            , commission_cik as cik 
            from issuer_info ii
        """
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        
        for row in result:
            company_dict = {
                    "company": row[0], 
                    "legal_status_form": row[1],
                    "date_incorporation": row[2].isoformat() if row[2] else None,
                    "street1": row[3],
                    "street2": row[4],
                    "city": row[5],
                    "state_or_country": row[6],
                    "zipcode": row[7],
                    "issuer_website": row[8],
                    "cik": row[9]
                }
            companies_list.append(company_dict)
        return companies_list
    except Exception as e:
        raise e
    finally:
        cursor.close()