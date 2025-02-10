import psycopg2

# Connect to PostgreSQL database
conn = psycopg2.connect(
    dbname="my_database",
    user="postgres",
    password="root",
    host="localhost",
    port="5432"
)

conn.commit()
conn.close()
