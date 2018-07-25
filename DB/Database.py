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

c.execute('CREATE TABLE IF NOT EXISTS Users(user text, passw text, cargo text)')
c.execute("""
CREATE TABLE IF NOT EXISTS Clientes(data text, cargo text, user, name text, cpf text, tel text,email text)
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
        clt = 'INSERT INTO Clientes(data, cargo, user, name, cpf, tel, email) VALUES (?,?,?,?,?,?,?)'
        data = "{} {}".format(date, hour)
        user = auth[0]
        cargo = auth[2]
        name = et_name.get()
        cpf = et_cpf.get()
        tel = et_tel.get()
        email = et_email.get()
        c.execute(clt,(data, cargo, user, name, cpf, tel, email),)
        con.commit()


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


#--------------------------------------
#       GESTOR DE CONSULTA
#--------------------------------------
def consulta():
    sql_consulta = 'SELECT * FROM Clientes WHERE name = ?'
    c.execute(sql_consulta, ('cabrito',))
    result_consulta = c.fetchone()
    user = auth[0]
    cargo = auth[2]
    root = Tk()
    root.title('S4U® CONSULTA')
    consult = LabelFrame(root, text='Consulta')
    Label(consult, text='Data: ').grid(row=0, column=0, sticky=W)
    Label(consult, text='Funcionario: ').grid(row=1, column=0, sticky=W)
    Label(consult, text='Nome: ').grid(row=2, column=0, sticky=W)
    Label(consult, text='CPF: ').grid(row=3, column=0, sticky=W)
    Label(consult, text='Telefone: ').grid(row=4, column=0, sticky=W)
    Label(consult, text='E-Mail: ').grid(row=5, column=0, sticky=W)


#--------------------------------------
#       EXIBIR INFORMAÇÕES
#--------------------------------------
    lb_tempo = Label(consult, text='{}'.format(result_consulta[0]))
    lb_user = Label(consult, text='{} {}'.format(result_consulta[1].title(), result_consulta[2].title()))
    lb_name = Label(consult, text='{}'.format(result_consulta[3]))
    lb_cpf = Label(consult, text='{}'.format(result_consulta[4]))
    lb_tel = Label(consult, text='{}'.format(result_consulta[5]))
    lb_email = Label(consult, text='{}'.format(result_consulta[6]))

    lb_tempo.grid(row=0, column=1, sticky=W)
    lb_user.grid(row=1, column=1, sticky=W)
    lb_name.grid(row=2, column=1, sticky=W)
    lb_cpf.grid(row=3, column=1, sticky=W)
    lb_tel.grid(row=4, column=1, sticky=W)
    lb_email.grid(row=5, column=1, sticky=W)
    consult.grid(row=0, columnspan=4, sticky=W+E)


#--------------------------------------
#       BUSCANDO CLIENTES
#--------------------------------------
    def refresh():
        for clear in treeview.get_children():
            treeview.delete(clear)

        c.execute('SELECT * FROM Clientes')
        for sql_cliente in c.fetchall():
            treeview.insert('', 0, text=sql_cliente[3], values=(sql_cliente[5], sql_cliente[6]))


#--------------------------------------
#       INTERFACE GRAFICA DE BUSCA
#--------------------------------------
    Label(root, text='Pesquisar:').grid(row=1, column=0, sticky=E)
    Button(root, text='Pesquisar').grid(row=1, column=2, sticky=W+E)
    Button(root, text='Buscar', command=refresh).grid(row=1, column=3, sticky=W+E)
    et_busca = Entry(root)
    treeview = ttk.Treeview(root, columns=('#0', '#1'))
    treeview.heading('#0', text='Nome')
    treeview.heading('#1', text='Telefone')
    treeview.heading('#2', text='E-Mail')
    et_busca.grid(row=1, column=1, sticky=W+E)
    treeview.grid(row=2, columnspan=4, sticky=W+E)


    refresh()
    root.mainloop()
















