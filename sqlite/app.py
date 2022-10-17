import python_sqlite

#python_sqlite.delete_one('7') # Will get value error with int. Need parameter as str

list_1 = [
		('Brenda', 'Matthews', 'bmatt@yahoo.com'),
		('Terry', 'Waters', 'twaters@gmail.com'),
		('James', 'Worthy', 'jworthy@gmail.com')
		]


#python_sqlite.add_many(list_1)

#Got interface error by having execute() instead of executemany()

#python_sqlite.email_lookup('bmatt@yahoo.com')

#noticed this works w/o conn.commit() and conn.close()

python_sqlite.id_lookup('8')

#python_sqlite.show_all()
