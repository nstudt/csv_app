# this is the non-psycopg2 method of copying from csv to table
import csv
import psycopg2
from create_prods_table import create_table
from psycopg2.extensions import AsIs


conn = psycopg2.connect("host=localhost dbname=products user=postgres password=asdf")
cur = conn.cursor()
fname = 'prods.csv'

def process_csv(fname):
	with open(fname, 'r') as f:
	    reader = csv.reader(f)
	    next(reader)  # Skip the header row.
	    for row in reader:
	        try:
	        	cur.execute("INSERT INTO products VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
	        	row
	        	)
	        except psycopg2.InternalError as e:
	        	print(e)
	        	continue
	        except psycopg2.DataError as e:
	        	print(e)
	        	continue
	conn.commit()
	print()

def alter_table(tname):
	cur.execute("DROP TABLE %s" % tname)
	conn.commit()
	wait = input('Press any key')
	print('table dropped')
	create_table() #products is hard coded
	print(tname +' table created')
            
def main():
	a = input("Do you want to purge old table? (Y/N)")
	if a.lower() == 'y':
		alter_table("products")
		process_csv(fname)
	elif a.lower() == 'n':
		#process_csv(fname)
		print("Operation Completed!")
	else:
		print('Wrong Answer: Operatons Terminated')
		
if __name__== "__main__":
  main()


