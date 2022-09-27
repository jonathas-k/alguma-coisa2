from tkinter import *
#___________________________________________________________________________________
#Back-end
def IMC():
    try:
        Label_['text'] = float(Box_.get()) / (float(Box2.get()) * float(Box2.get()))
    except:
        Label_['text'] = 'Valor Invalido'
#___________________________________________________________________________________
#Front-end
SENAC = Tk()
FN = 'Verdana 20 bold'
Label_= Label(SENAC, text=0.0, font=FN) 
Label2= Label(SENAC, text='Altura:', font=FN) 
Label3= Label(SENAC, text='Peso:', font=FN) 
Box_= Entry(SENAC, font=FN)
Box2= Entry(SENAC, font=FN)
But_= Button(SENAC, font=FN, text='IMC', command=IMC)
#___________________________________________________________________________________
#Org
Label_.grid(row=0, column=1)
Label2.grid(row=2, column=0)
Label3.grid(row=1, column=0)
Box_.grid  (row=1, column=1)
Box2.grid  (row=2, column=1)
But_.grid  (row=3,column=1)
SENAC.mainloop()
#___________________________________________________________________________________
