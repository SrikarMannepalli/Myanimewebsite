import sqlite3, time

#conn = sqlite3.connect('thehyliadatabasesql.db')
conn = sqlite3.connect('thehyliaALBUMS.db')
c = conn.cursor()
c.execute("SELECT * FROM albums")
for row in c.fetchall():
    print(row)

c.close()
conn.close()
