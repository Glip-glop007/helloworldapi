import os
import psycopg2
from psycopg2.extras import RealDictCursor 

# fetch DATABASE_URL  from env var
DATABASE_URL = "dbname=exampledb user=postgres password=qwer1234 host=localhost port=5432"


def connect_db():
    conn = psycopg2.connect(DATABASE_URL, cursor_factory=RealDictCursor)
    return conn

conn = connect_db()
cur = conn.cursor()
    