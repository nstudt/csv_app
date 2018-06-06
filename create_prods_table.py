#use to create table for the first row of the products cvs. NOT FINISHED
import psycopg2

conn = psycopg2.connect("host=localhost dbname=mydb user=postgres password=asdf")
cur = conn.cursor()

def create_table():
	try:



		cur.execute("""
		CREATE TABLE products
		             (Category text,
		             Product text,
		             Variant text,
		             Code integer PRIMARY KEY,
		             Supplier text,
		             UnitCost real,
		             UnitPrice real,
		             Discount real,
		             Type text,
		             UOM text,
		             Released text,
		             ID text,
		             ProductID text,
		             ProductCode text,
		             Product_Description text,
		             Description text,
		             Inventory_Cebu real,
		             Inventory_Dapa real,
		             Inventory_Gen_Luna real
		)
		""")
		conn.commit()
	except Exception as e:
		print('something bad happened' + e)

if __name__ == '__main__':
	create_table()

