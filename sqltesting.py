import sqlite3

connection = sqlite3.connect("names.db")

cursor = connection.cursor()
# sql_command = """
# 	SELECT NAME FROM commonnames
# 	WHERE NAME = 'AARON'
# 	"""

cursor.execute("SELECT NAME FROM commonnames WHERE NAME LIKE 'A%'")

print("fetchall:")
fetcharray = []

result = cursor.fetchall()
for i in result:
	print i 
# for i in result:
# 	if len(i)>1:
# 		fetcharray.append([i[0].lower(), i[1]])
# 	else:
# 		fetcharray.append([i[0].lower(), None])

# print fetcharray

# for i in fetcharray:
# 	if i == 'aaron':
# 		cursor.execute("UPDATE NAME SET COUNT = COUNT+1 WHERE NAME ='AARON'")

cursor.close()

# print("\nfetch one:")
# res = cursor.fetchall("""
# 	SELECT NAME FROM commonnames
# 	WHERE NAME LIKE "%A"
# 	""")
# print(res)