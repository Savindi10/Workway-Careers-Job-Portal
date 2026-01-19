from db import get_db_connection

def get_admin_by_email(email):
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            sql = "SELECT * FROM users WHERE email=%s AND role='admin'"
            cursor.execute(sql, (email,))
            return cursor.fetchone()
    finally:
        conn.close()

# create Add job function 
def create_job(
        title,
        description,
        location,
        company_name,
        job_type,
        closing_date,
        admin_id,
):
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            sql = """
            INSERT INTO jobs (title,description,location,company_name,job_type,closing_date,admin_id)
            VALUES (%s,%s,%s,%s,%s,%s,%s)"""

            cursor.execute(sql,(
                title,
                description,
                location,
                company_name,
                job_type,
                closing_date,
                admin_id
            ))
            conn.commit()

    finally: 
        conn.close()        

# Get all the job function 
def get_all_jobs():
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            sql = "SELECT * FROM jobs"
            cursor.execute(sql)
            return cursor.fetchall()
            conn.commit()
    finally:
        conn.close()