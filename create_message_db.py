import sqlite3
con = sqlite3.connect("squeek.db")

cur = con.cursor()

cur.execute("""CREATE TABLE Messages (uuid TEXT, datetime TEXT, to TEXT, from TEXT, message BLOB, status TEXT,)""")
con.commit()
cur.close()
con.close()
