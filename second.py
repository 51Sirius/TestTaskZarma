import sqlite3

connection = sqlite3.connect('test.db')
cursor = connection.cursor()

print(*cursor.execute('''
Select name, age from USERS where age>30
''').fetchall(), sep='\n')
connection.close()
