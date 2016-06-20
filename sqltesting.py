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

# 	name = str(i[0]).lower()
# 	if len(i)>1:
# 		fetcharray.append([name,i[1]])
# 	else:
# 		fetcharray.append([name, None])

# print fetcharray

# for i in fetcharray:
# 	if i[0] == 'aaron' and i[1] == None:
# 		cursor.execute("UPDATE commonnames SET COUNT=1 WHERE NAME='AARON'")
# 	elif i[0] == 'aaron':
# 		cursor.execute("UPDATE commonnames SET COUNT=COUNT+1 WHERE NAME='AARON'")

# # cursor.close()

# print("\nfetch one:")
# res = cursor.fetchall("""
# 	SELECT NAME FROM commonnames
# 	WHERE NAME LIKE "%A"
# 	""")
# print(res)