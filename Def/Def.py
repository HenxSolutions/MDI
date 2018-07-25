from DB import Database
from tkinter import *
from tkinter import ttk
import time
time = time.localtime()
hour = ('{}:{}'.format(time[3], time[4]))
date = ('{}/{}/{}'.format(time[0], time[1], time[2]))

#-------------------------------------------
#  CONSULTANDO AO GESTOR DE BANCO DE DADOS
#-------------------------------------------
def login(user, passw):
    if Database.login(user, passw) == True:
        return True
    else:
        return False


#--------------------------------------
#      INTERFACE GRAFICA DO MENU
#--------------------------------------
def menu(user):
    cargo = Database.cargo(user)
    root = Tk()
    root.geometry("1024x768+0+0")
    root.title('S4U® Bem Vindo {}'.format(user))
    title = Label(root, text='Seja Bem Vindo "{} {}"\n{}\n{}'.format(cargo.title(), user.title(), date, hour))
    title.grid(row=0, columnspan=2, sticky=W+E)


#--------------------------------------
#      INTERFACE DE CADASTRO
#--------------------------------------
    cad = LabelFrame(root, text='Cadastro')
    cad.grid(row=1,columnspan=2, sticky=W+E)
    Button(cad, text='CADASTRAR', command=Database.cadastro).grid(row=0, column=0, sticky=W+E)
    Button(cad, text='CONSULTAR', command=Database.consulta).grid(row=1, column=0, sticky=W+E)


#--------------------------------------
#      INTERFACE DE CONFIGURAÇÃO
#--------------------------------------
    conf = LabelFrame(root, text='Configurações')
    Button(conf, text='CONFIGURAR').grid(row=0, column=0, sticky=W+E)


#--------------------------------------
#      INTERFACE DE DADOS
#--------------------------------------
    dados = LabelFrame(root, text='Dados')
    Button(dados, text='DADOS').grid(row=0, column=0, sticky=W+E)


#--------------------------------------
#      GESTOR DE PERMISSÃO
#--------------------------------------
    if cargo == 'admin' or cargo == 'fiscal':
        dados.grid(row=3,columnspan=2, sticky=W+E)
    if cargo == 'admin':
        conf.grid(row=2,columnspan=2, sticky=W+E)

    root.mainloop()
