import sqlite3

connection = sqlite3.connect("names.db")

cursor = connection.cursor()

namecheck = raw_input("Enter a name\n>").upper()

cursor.execute("SELECT * FROM commonnames WHERE NAME LIKE 'A%'")


fetcharray = []
result = cursor.fetchall()

for i in result:
	name = str(i[0])
	counter = int(i[1])
	fetcharray.append([name.upper(), counter])

print fetcharray


for i in fetcharray:
	if i[0] == namecheck:
		cursor.execute("UPDATE commonnames SET COUNT=COUNT+1 WHERE NAME=?",(i[0]))
	
connection.commit()

cursor.close()