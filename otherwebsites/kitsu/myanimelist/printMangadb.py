import sqlite3

conn = sqlite3.connect('manga.db')
c = conn.cursor()

c.execute("SELECT * FROM manga")

i = 0

for item in c.fetchall():
    i += 1
    print("i", i, "item\n", item)

c.close()
conn.close()