import sqlite3



connection = sqlite3.connect("db.sl3")

cur = connection.cursor()

print(connection)
print(cur)
connection.close()




connection = sqlite3.connect("db.sl3")
cur = connection.cursor()

cur.execute("CREATE TABLE students (bulbul city);")

connection.commit()
connection.close()




connection = sqlite3.connect("db.sl3")
cur = connection.cursor()

cur.execute("INSERT INTO students (name) VALUES ('bulbulbul bag')")
cur.execute("INSERT INTO students (name) VALUES ('bulbulbul bog')")
cur.execute("INSERT INTO students (name) VALUES ('BulBulBuulBul dog')")
cur.execute("INSERT INTO students (name) VALUES ('bulbulbul bul')")

connection.commit()
connection.close()



connection = sqlite3.connect("db.sl3")
cur = connection.cursor()

cur.execute("SELECT name FROM students")

connection.commit()
res = cur.fetchall()
print(res)
connection.close()



connection = sqlite3.connect("db.sl3")
cur = connection.cursor()

cur.execute("DELETE FROM students WHERE(name == 'bulbulbul bag')")

connection.commit()
connection.close()


connection = sqlite3.connect("db.sl3")
cur = connection.cursor()

cur.execute("UPDATE students SET name='Murad Otlichnik' WHERE(name == 'BulBulBuulBuldog')")

connection.commit()
connection.close()



connection = sqlite3.connect("db.sl3")
cur = connection.cursor()

cur.execute("DROP TABLE students")

connection.commit()
connection.close()