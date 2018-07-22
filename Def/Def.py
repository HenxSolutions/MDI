from DB import Database
from tkinter import *
from tkinter import ttk


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
    root.title('S4U® Bem Vindo {}'.format(user))


#--------------------------------------
#      INTERFACE DE CADASTRO
#--------------------------------------
    cad = LabelFrame(root, text='Cadastro')
    cad.grid(row=0,columnspan=2, sticky=W+E)
    Button(cad, text='CADASTRAR').grid(row=0, column=0, sticky=W+E)

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
        dados.grid(row=2,columnspan=2, sticky=W+E)
    if cargo == 'admin':
        conf.grid(row=1,columnspan=2, sticky=W+E)

    root.mainloop()
