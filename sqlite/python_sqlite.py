#Use of SQLite database module w/ Python and GitBash


import sqlite3

#conn = sqlite3.connect('customer.db')

#could also use .connect(':memory:')

#c = conn.cursor()


#c.execute('''CREATE TABLE customers(
#		first_name text,
#		last_name text,
#		email text
#	)''')

#c.execute('INSERT INTO customers VALUES ("Mary", "Smith", "m_smith@yahoo.com")')

#c.execute('INSERT INTO customers VALUES ("John", "Doe", "jdoe@yahoo.com")')

#c.execute('INSERT INTO customers VALUES ("Tim", "Allen", "timallen@yahoo.com")')

################## INSERT MANY ##############################

#many_customers = [	('Wes', 'Brown', 'wesbrown@gmail.com'),
				
#					('Steph', 'Wills', 'stwills@gmail.com'),

#					('Lisa', 'Thompson', 'listhompson@yahoo.com'),
#				]

#c.executemany('INSERT INTO customers VALUES (?,?,?)', many_customers) #? is placeholder for data

######### Query Database ##########################

#c.execute('SELECT * FROM customers')
#c.fetchone()
#c.fetchmany(3)


#Format Results
#items = c.fetchall()

#for item in items:
	#print(item)
#	print(item[0] + ' ' + item[1] + ' - ' + item[2])

#Primary Key
#c.execute('SELECT rowid, * FROM customers')

#items = c.fetchall()

#for item in items:
#	print(item)

########### Where Clause #####################

#c.execute("SELECT * FROM customers WHERE last_name = 'Smith'")

#Use LIKE

#c.execute("SELECT * FROM customers WHERE last_name LIKE 'Wi%'")

#c.execute("SELECT * FROM customers WHERE email LIKE '%yahoo%'")

############ Update Records ####################

#c.execute('''UPDATE customers SET first_name = 'Bob'
#			WHERE last_name = 'Doe'
#		''')

#Use row ID

#c.execute('''UPDATE customers SET first_name = 'Sarah'
#			WHERE rowid = 1
#		''')

############ Delete ###################

#c.execute('DELETE from customers WHERE rowid = 6')

########### ORDER BY ##################

#c.execute('SELECT * FROM customers ORDER BY last_name DESC') #ASC is default

##### AND & OR ######

#c.execute("SELECT * FROM customers WHERE last_name = 'Smith' AND rowid = 1")

#Both AND conditions need to be true

#c.execute("SELECT * FROM customers WHERE first_name = 'Tim' OR rowid = 6")

#one or both conditions can be true


##### LIMIT ######

#c.execute("SELECT rowid, * FROM customers LIMIT 4")

#### DROP TABLE ######

#c.execute("DROP TABLE customers")
#conn.commit()

#### App w/ Functions #######

#Function that queries DB and returns all records

def show_all():

	conn = sqlite3.connect('customer.db')

	c = conn.cursor()

	c.execute("SELECT rowid, * FROM customers")

	items = c.fetchall()

	for item in items:
		print(item)

	conn.commit()
	conn.close()

	print('Command executed')

#Function that add records to DB

def add_one(first, last, email):

	conn = sqlite3.connect('customer.db')

	c = conn.cursor()

	c.execute("INSERT INTO customers VALUES (?,?,?)", (first, last, email))

	conn.commit()
	conn.close()

#Function that deletes records

def delete_one(id):
	conn = sqlite3.connect('customer.db')

	c = conn.cursor()

	c.execute("DELETE from customers WHERE rowid = (?)", id)

	conn.commit()
	conn.close()

#Function that adds many records

def add_many(list):
	conn = sqlite3.connect('customer.db')

	c = conn.cursor()

	c.executemany("INSERT INTO customers VALUES (?,?,?)", (list))

	#Will get interface error by having execute() instead of executemany()

	conn.commit()
	conn.close()

#Function that returns records by email

def email_lookup(email):

	conn = sqlite3.connect('customer.db')

	c = conn.cursor()

	c.execute("SELECT * FROM customers WHERE email = (?)", (email,)) #since it's a tuple need comma after email

	items = c.fetchall()

	for item in items:
		print(item)

#Function to lookup by ID

def id_lookup(id):

	conn = sqlite3.connect('customer.db')

	c = conn.cursor()

	c.execute("SELECT * FROM customers WHERE rowid = (?)", (id))

	items = c.fetchall()

	for item in items:
		print(item)

#interesting that both lookup functions work w/o conn.commit() and conn.close()

#Use triple quotes to condense code


'''
SQLite Data Types

NULL
INTEGER
#REAL (float)
TEXT
BLOB (image, mp3 file)
'''