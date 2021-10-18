import psycopg2

conn_url = 'postgresql://postgres:lusm123@localhost:5432/college'

try:
    conn = psycopg2.connect(conn_url)
except Exception as db_err:
    print(db_err)
    raise db_err

