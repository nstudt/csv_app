import sqlite3
conn = sqlite3.connect('prods.db')

c = conn.cursor()

# Create table
c.execute('''CREATE TABLE products
             (Category text, 
             Product text, 
             Variant text,
             Code integer,
             Supplier text,
             UnitCost real,
             UnitPrice real,
             Discount integer,
             Type text,
             UOM text,
             Released text,
             ID text,
             ProductID text,
             ProductCode text,
             Product_Description text,
             Description text,
             Inventory_Cebu integer,
             Inventory_Dapa integer,
             Inventory_Gen_Luna integer)
             '''
             )

# Insert a row of data
#c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()