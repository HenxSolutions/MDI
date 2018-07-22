import sqlite3


#--------------------------------------
# GESTOR DE BANCO DE DADOS
#--------------------------------------
con = sqlite3.connect('database.db')
c = con.cursor()
c.execute('CREATE TABLE IF NOT EXISTS Users(user text, passw text, cargo text)')
sql = 'SELECT * FROM Users WHERE user = ?'


#--------------------------------------
#         QUERRY DE LOGIN
#--------------------------------------
def login(user, passw):
    c.execute(sql, (user,))
    auth = c.fetchone()
    if auth == None:
        return False
    else:
        if (user, passw) == (auth[0], auth[1]):
            return True
        else:
            return False


#--------------------------------------
#         QUERRY DE CARGO
#--------------------------------------
def cargo(user):
    c.execute(sql, (user,))
    auth = c.fetchone()
    return auth[2]
