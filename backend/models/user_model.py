from db import get_db_connection

# user login 
from db import get_db_connection

def get_user_by_email(email):
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            sql = "SELECT * FROM users WHERE email=%s AND role='user'"
            cursor.execute(sql, (email,))
            return cursor.fetchone()
    finally:
        conn.close()

# view all the jobs 
def get_all_jobs():
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM jobs")
            jobs = cursor.fetchall()
    finally: 
        conn.close()
    return jobs

# View job details (by ID specific job)
def get_job_by_id(job_id):
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM jobs WHERE job_id=%s", (job_id,))
            job = cursor.fetchone()
    finally:
        conn.close()
    return job

# Insert job application 
def insert_application(user_id, job_id,resume_url):
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO job_applications (user_id,job_id,resume_url)"
                " VALUES (%s, %s, %s)",
                (user_id, job_id, resume_url)
            )
            conn.commit()
    finally:
        conn.close()        