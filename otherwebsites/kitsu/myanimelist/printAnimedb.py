import sqlite3

conn = sqlite3.connect('anime.db')
c = conn.cursor()

c.execute("SELECT * FROM anime")

i = 0

for item in c.fetchall():
    i += 1
    print("i", i, "item\n", item)

c.close()
conn.close()