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
	fetcharray.append(i)

print fetcharray

cursor.close()

# print("\nfetch one:")
# res = cursor.fetchall("""
# 	SELECT NAME FROM commonnames
# 	WHERE NAME LIKE "%A"
# 	""")
# print(res)