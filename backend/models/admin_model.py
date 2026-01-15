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
