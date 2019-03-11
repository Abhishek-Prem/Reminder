import mysql.connector
from mysql.connector import Error
from python_mysql_dbconfig import read_db_config
import sys

conn = mysql.connector.connect(host='localhost', database='Reminder', user='root', password='root')

while(1):

	print('MENU\n1. Create\n2. Update\n3. View\n4. Exit\nEnter Choice: ')
	n = int(input())

	if(n==1):
		print('Create\n')
		name=input('Name: ')
		description=input('Description: ')
		query = "INSERT INTO books(name, description) VALUES(%s,%s)"
		args = (name, description)
		db_config = read_db_config()
		conn = MySQLConnection(**db_config)
		cursor = conn.cursor()
		cursor.execute(query, args)

	elif(n==2):
		print('Update\n')
		db_config = read_db_config()
		name=input('Name: ')
		description=input('Description: ')
		query = """ UPDATE reminder SET description = %s WHERE name = %s """
		data = (name, description)
		conn = MySQLConnection(**db_config)
		cursor = conn.cursor()
		cursor.execute(query, data)
		conn.commit()

	elif(n==3):
		print('View\n')
		cursor = conn.cursor()
		cursor.execute("SELECT * FROM reminder")
		row = cursor.fetchone()
		while row is not None:
			print(row)
			row = cursor.fetchone()

	elif(n==4):
		sys.exit()

	else:
		print('Wrong Choice!\n')

conn.close()
