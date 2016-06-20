import sqlite3

connection = sqlite3.connect("names.db")

cursor = connection.cursor()

namecheck = raw_input("Enter a name\n>").upper()

cursor.execute("SELECT * FROM commonnames")

result = cursor.fetchall()
for i in result:
	print i

for i in result:
	if str(i[0]) == namecheck:
	 	cursor.execute("UPDATE commonnames SET COUNT=COUNT+1 WHERE NAME=?",(i[0],))
	
connection.commit()

cursor.close()