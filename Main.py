from Def import Def
from tkinter import *


#--------------------------------------
#       AUTENTICANDO O LOGIN
#--------------------------------------
def auth():
    user = et_user.get()
    passw = et_passw.get()
    if (user, passw) == ('', ''):
        result['text'] = 'Preencher os Campos'
    else:
        if Def.login(user, passw) == True:
            root.destroy()
            Def.menu(user)
        else:
            result['text'] = 'Usuario ou Senha Incorretos'

#--------------------------------------
#     INTERFACE GRAFICA DO LOGIN
#--------------------------------------
root = Tk()
root.title('S4U® LOGIN')
Label(root, text='User:').grid(row=0, column=0)
Label(root, text='Passw:').grid(row=1, column=0)
result = Label(root, fg='red')
Button(root, text='Login', command=auth).grid(row=3, columnspan=2)
et_user = Entry(root)
et_passw = Entry(root, show='*')
et_user.grid(row=0, column=1)
et_passw.grid(row=1, column=1)
result.grid(row=2, columnspan=2, sticky=W+E)
Label(root, text='S4U® Designed for {}').grid(row=4, columnspan=2)
root.mainloop()

