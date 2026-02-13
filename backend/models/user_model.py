import pymysql
from db import get_db_connection
from werkzeug.security import generate_password_hash

# User Registration
def create_user(name, email,password):
    conn = get_db_connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    hashed_password = generate_password_hash(password)

    query = """
        INSERT INTO users (name, email,password,role)
        VALUES (%s, %s, %s,'user')
    """
    cursor.execute(query, (name,email, hashed_password))
    conn.commit()

    user_id = cursor.lastrowid
    cursor.close()
    conn.close()
    return user_id


# user login 
from db import get_db_connection

def get_user_by_email(email):
    conn = get_db_connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    sql = "SELECT * FROM users WHERE email=%s AND role='user'"
    cursor.execute(sql, (email,))
    user = cursor.fetchone()

    cursor.close()
    conn.close()
    return user


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