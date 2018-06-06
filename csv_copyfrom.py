import psycopg2

conn = psycopg2.connect("host=localhost dbname=mydb user=postgres password=asdf")
cur = conn.cursor()
with open('prods.csv', 'r') as f:
    # Notice that we don't need the `csv` module.
    next(f)  # Skip the header row.
    cur.copy_from(f, 'users', sep=',', columns=('Product', 'Code'))
    
conn.commit()