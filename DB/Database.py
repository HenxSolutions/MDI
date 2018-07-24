from tkinter import *
from tkinter import ttk
import sqlite3
import time


#--------------------------------------
#   DEFININDO MODULO HORA E DATA
#--------------------------------------
time = time.localtime()
hour = ('{}:{}'.format(time[3], time[4]))
date = ('{}/{}/{}'.format(time[0], time[1], time[2]))


#--------------------------------------
# GESTOR DE BANCO DE DADOS
#--------------------------------------
con = sqlite3.connect('database.db')
c = con.cursor()
sql = 'SELECT * FROM Users WHERE user = ?'
clt = 'INSER INTO Clientes(data, funcionario, nome, cpf, tel, email) VALUES (?,?,?,?,?,?)'

c.execute('CREATE TABLE IF NOT EXISTS Users(user text, passw text, cargo text)')
c.execute("""
CREATE TABLE IF NOT EXISTS Clientes(data text, funcionario text, nome text, cpf text, tel text,email text)
""")


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
    global auth
    auth = c.fetchone()
    return auth[2]


#--------------------------------------
#       CADASTRO DE CLIENTES
#--------------------------------------
def cadastro():


#--------------------------------------
#       GESTOR DE INFORMAÇÃO
#--------------------------------------
    def get():
        data = "{} {}".format(date, hour)
        user = auth[0]
        cargo = auth[2]
        name = et_name.get()
        cpf = et_cpf.get()
        tel = et_tel.get()
        email = et_email.get()
        c.execute('')

    root = Tk()
    cad = LabelFrame(root, text='Cadastro')
    root.title("S4U® CADASTRO")
    Label(cad, text='Nome').grid(row=0, column=0)
    Label(cad, text='CPF').grid(row=1, column=0)
    Label(cad, text='Telefone').grid(row=2, column=0)
    Label(cad, text='E-Mail').grid(row=3, column=0)

    et_name = Entry(cad)
    et_cpf = Entry(cad)
    et_tel = Entry(cad)
    et_email = Entry(cad)

    et_name.grid(row=0, column=1)
    et_cpf.grid(row=1, column=1)
    et_tel.grid(row=2, column=1)
    et_email.grid(row=3, column=1)
    cad.grid(row=0, columnspan=4)

    Button(root, text='Salvar', command=get).grid(row=1, column=0, sticky=W+E)
    Button(root, text='Cadastrar Equipamento').grid(row=1, column=1, sticky=W+E)
    Button(root, text='Limpar').grid(row=1, column=2, sticky=W+E)
    Button(root, text='Sair').grid(row=1, column=3, sticky=W+E)

    root.mainloop()
