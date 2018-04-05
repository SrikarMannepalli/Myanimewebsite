import sqlite3

conn = sqlite3.connect('anime.db')
c = conn.cursor()
conn2 = sqlite3.connect('manga.db')
c2 = conn2.cursor()

c.execute("SELECT * FROM anime")
c2.execute("SELECT * FROM manga")
i = 0

for item in c.fetchall():
    i += 1
    print("i", i)
    print("item\n", item)

print('\n'*34)


i = 0

for item in c2.fetchall():
    i += 1
    print("i", i)
    print("item\n", item)



c.close()
conn.close()
c2.close()
conn2.close()