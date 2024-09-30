import sqlite3



def get_users(name, pwd):
    con = sqlite3.connect("users.db")
    cur = con.cursor()
    cur.execute(f"select * from users where name='{name}' and pwd='{pwd}'")
    fetched = cur.fetchall()
    con.close()
    return fetched

# init
# name pwd admin
# users_data = [
#     ('admin', '@1sjoifjpaoifb', 1),
#     ('banana', 'banana', 0),
#     ('cindy', "cindy", 0),
#     ('david', 'david', 0),
#     ('ncu', 'ncu', 0)
# ]

if __name__ == '__main__':
    users_data = [
        ('ncu', 'ncu', 0),
        ('admin', '@1sjoifjpaoifb', 1),
        ('banana', 'banana', 0),
        ('cindy', "cindy", 0),
        ('david', 'david', 0),
    ]
    con = sqlite3.connect("users.db")
    cur = con.cursor()
    cur.execute(f"create table users (name text, pwd text, admin integer)")
    cur.executemany('insert into users values (?,?,?)',users_data)
    con.commit()
    con.close()