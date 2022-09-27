def exit():
    janela.destroy()
 
def convert():
    c = int(e1.get())
    f = ((c*9)/(5))+32
    t1.config(state='normal')
    t1.delete('1.0', tk.END)
    t1.insert(tk.END,f)
    t1.config(state='disabled')
 
import tkinter as tk
janela = tk.Tk()
janela.geometry("300x250")
janela.config(bg="#A569BD")
janela.resizable(width=False,height=False)
janela.title('Celsius para Fahrenheit Convertor!')
 
l1 = tk.Label(janela,text="Celsius para Fahrenheit Convertor",font=("Arial", 15),fg="white",bg="black")
l2= tk.Label(janela,text="coloque temperatura em Celsius: ",font=("Arial", 10,"bold"),fg="white",bg="#A569BD")
l3= tk.Label(janela,text="Temperatura em Fahrenheit é: ",font=("Arial", 10,"bold"),fg="white",bg="#A569BD")
 
empty_l1 = tk.Label(janela,bg="#A569BD")
empty_l2 = tk.Label(janela,bg="#A569BD")
 
e1= tk.Entry(janela,font=('Arial',10))
 
btn1 = tk.Button(janela,text="Converter para Fahrenheit!",font=("Arial", 10),command=convert)
btn2 = tk.Button(janela,text="sair",font=("Arial", 10),command=exit)
 
t1=tk.Text(janela,state="disable",width=15,height=0)
 
l1.pack()
l2.pack()
e1.pack()
empty_l1.pack()
btn1.pack()
l3.pack()
t1.pack()
empty_l2.pack()
btn2.pack()
 
janela.mainloop()