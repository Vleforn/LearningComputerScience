import psycopg2
import getpass

password = getpass.getpass(prompt="Enter password: ")
with psycopg2.connect(f"dbname=dvdrental user=postgres password={password}") as conn:
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM actor;")
        print(cur.fetchone())