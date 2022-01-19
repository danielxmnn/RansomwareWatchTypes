import sqlite3

con = sqlite3.connect('base.db')
cur = con.cursor()


cur.execute("SELECT * FROM projects WHERE name_group = 'Cuba'")

j = (cur.fetchall())
print(j)