import sqlite3

con = sqlite3.connect("tutorial.db")
cur = con.cursor()

cur.execute("""UPDATE movie
              SET title=?,
                  year=?
              WHERE score=?""", ("12345", 2000, 8.2))

con.commit()
con.close()
