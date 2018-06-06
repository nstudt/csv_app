
import psycopg2

conn = psycopg2.connect("host=localhost dbname=products user=postgres password=asdf")
cur = conn.cursor()

cur.execute("select Category, Product, Code, Inventory_Dapa from products where Inventory_Dapa < 2;")
print(cur.fetchmany(2))
print(cur.fetchmany(2))