import sqlite3
              
src_db = r"C:/Program Files/IPBan/ipban.sqlite"
con = sqlite3.connect(src_db)
cur = con.cursor()
cur.execute('''select IPAddress, IPAddressText, LastFailedLogin, FailedLoginCount, BanDate, State, BanEndDate, UserName, Source from IPAddresses I ''')
print(cur.fetchall())
con.commit()
con.close()