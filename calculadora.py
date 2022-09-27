from tkinter import *
import tkinter.messagebox

root = Tk()
root.geometry('1350x750+0+0')
root.title('Tic Tac Toe')
root.configure(background='cadet Blue')

Tops = Frame(root,bg= 'sky blue',pady=2,width=1350,height=100,relief=RIDGE)
Tops.grid(row=0,column=0)

label_title = Label(Tops,font=('arial',50,'bold'),text= 'Tic Tac Toe Game',bd=21,bg='cadet Blue',fg='cornsilk',justify=CENTER)
label_title.grid(row=0,column=0)

MainFrame = Frame(root,bg= 'Powder blue',pady=2,width=1350,height=600,relief=RIDGE)
MainFrame.grid(row=1,column=0)

leftFrame = Frame(MainFrame,bd=10, width=750, height=500, pady=2,padx=10, bg='cadet Blue',relief=RIDGE)
leftFrame.pack(side=LEFT)

rightFrame = Frame(MainFrame,bd=10, width=600, height=500, pady=2,padx=10, bg='cadet Blue',relief=RIDGE)
rightFrame.pack(side=RIGHT)

rightFrame1 = Frame(rightFrame,bd=10, width=550, height=200, pady=2,padx=10, bg='cadet Blue',relief=RIDGE)
rightFrame1.grid(row=0,column=0)

rightFrame2 = Frame(rightFrame,bd=10, width=550, height=200, pady=2,padx=10, bg='cadet Blue',relief=RIDGE)
rightFrame2.grid(row=1,column=0)

playerX = IntVar()
playerO = IntVar()

playerX.set(0)
playerO.set(0)

buttons = StringVar()
click = True

def check(buttons):
	global click
	if buttons['text'] == '' and click == True:
		buttons ['text'] = 'X'
		click = False
		scorekeeper()

	elif buttons['text'] == '' and click == False:
		buttons ['text'] = 'O'
		click = True
		scorekeeper()

def scorekeeper():
	if (button1['text'] =='X' and button2['text']=='X' and button3['text']=='X'  ):
		button1.configure(background='light green')
		button2.configure(background='light green')
		button3.configure(background='light green')
		n = float(playerX.get())
		score = n + 1
		playerX.set(score)
		tkinter.messagebox.showinfo('Winner X','you have won the game')

	if (button4['text'] =='X' and button5['text']=='X' and button6['text']=='X'  ):
		button4.configure(background='light green')
		button5.configure(background='light green')
		button6.configure(background='light green')
		n = float(playerX.get())
		score = n + 1
		playerX.set(score)
		tkinter.messagebox.showinfo('Winner X','you have won the game')

	if (button7['text'] =='X' and button8['text']=='X' and button9['text']=='X'  ):
		button7.configure(background='light green')
		button8.configure(background='light green')
		button9.configure(background='light green')
		n = float(playerX.get())
		score = n + 1
		playerX.set(score)
		tkinter.messagebox.showinfo('Winner X','you have won the game')

	if (button1['text'] =='X' and button5['text']=='X' and button9['text']=='X'  ):
		button1.configure(background='light green')
		button5.configure(background='light green')
		button9.configure(background='light green')
		n = float(playerX.get())
		score = n + 1
		playerX.set(score)
		tkinter.messagebox.showinfo('Winner X','you have won the game')

	if (button3['text'] =='X' and button5['text']=='X' and button7['text']=='X'  ):
		button3.configure(background='light green')
		button5.configure(background='light green')
		button7.configure(background='light green')
		n = float(playerX.get())
		score = n + 1
		playerX.set(score)
		tkinter.messagebox.showinfo('Winner X','you have won the game')

	if (button3['text'] =='X' and button6['text']=='X' and button9['text']=='X'  ):
		button3.configure(background='light green')
		button6.configure(background='light green')
		button9.configure(background='light green')
		n = float(playerX.get())
		score = n + 1
		playerX.set(score)
		tkinter.messagebox.showinfo('Winner X','you have won the game')

	if (button2['text'] =='X' and button5['text']=='X' and button8['text']=='X'  ):
		button2.configure(background='light green')
		button5.configure(background='light green')
		button8.configure(background='light green')
		n = float(playerX.get())
		score = n + 1
		playerX.set(score)
		tkinter.messagebox.showinfo('Winner X','you have won the game')

	if (button1['text'] =='X' and button4['text']=='X' and button7['text']=='X'  ):
		button1.configure(background='light green')
		button4.configure(background='light green')
		button7.configure(background='light green')
		n = float(playerX.get())
		score = n + 1
		playerX.set(score)
		tkinter.messagebox.showinfo('Winner X','you have won the game')
#mu nfg gfoerfhdbhwuie gyueg weidhhhh

#Player O strartar here
	############################################################################

	if (button1['text'] =='O' and button2['text']=='O' and button3['text']=='O'  ):
		button1.configure(background='light green')
		button2.configure(background='light green')
		button3.configure(background='light green')
		n = float(playerX.get())
		score = n + 1
		playerO.set(score)
		tkinter.messagebox.showinfo('Winner O','you have won the game')

	if (button4['text'] =='O' and button5['text']=='O' and button6['text']=='O'  ):
		button4.configure(background='light green')
		button5.configure(background='light green')
		button6.configure(background='light green')
		n = float(playerX.get())
		score = n + 1
		playerO.set(score)
		tkinter.messagebox.showinfo('Winner O','you have won the game')

	if (button7['text'] =='O' and button8['text']=='O' and button9['text']=='O'  ):
		button7.configure(background='light green')
		button8.configure(background='light green')
		button9.configure(background='light green')
		n = float(playerX.get())
		score = n + 1
		playerO.set(score)
		tkinter.messagebox.showinfo('Winner O','you have won the game')

	if (button1['text'] =='O' and button5['text']=='O' and button9['text']=='O'  ):
		button1.configure(background='light green')
		button5.configure(background='light green')
		button9.configure(background='light green')
		n = float(playerX.get())
		score = n + 1
		playerO.set(score)
		tkinter.messagebox.showinfo('Winner O','you have won the game')

	if (button3['text'] =='O' and button5['text']=='O' and button7['text']=='O'  ):
		button3.configure(background='light green')
		button5.configure(background='light green')
		button7.configure(background='light green')
		n = float(playerX.get())
		score = n + 1
		playerO.set(score)
		tkinter.messagebox.showinfo('Winner O','you have won the game')

	if (button1['text'] =='O' and button4['text']=='O' and button7['text']=='O'  ):
		button1.configure(background='light green')
		button4.configure(background='light green')
		button7.configure(background='light green')
		n = float(playerX.get())
		score = n + 1
		playerO.set(score)
		tkinter.messagebox.showinfo('Winner O','you have won the game')

	if (button2['text'] =='O' and button5['text']=='O' and button8['text']=='O'  ):
		button2.configure(background='light green')
		button5.configure(background='light green')
		button8.configure(background='light green')
		n = float(playerX.get())
		score = n + 1
		playerO.set(score)
		tkinter.messagebox.showinfo('Winner O','you have won the game')

	if (button3['text'] =='O' and button6['text']=='O' and button9['text']=='O'  ):
		button3.configure(background='light green')
		button6.configure(background='light green')
		button9.configure(background='light green')
		n = float(playerX.get())
		score = n + 1
		playerO.set(score)
		tkinter.messagebox.showinfo('Winner O','you have won the game')

def reset():
	button1['text'] = ''
	button2['text'] = ''
	button3['text'] = ''
	button4['text'] = ''
	button5['text'] = ''
	button6['text'] = ''
	button7['text'] = ''
	button8['text'] = ''
	button9['text'] = ''

	button1.configure(background='gainsboro')
	button2.configure(background='gainsboro')
	button3.configure(background='gainsboro')
	button4.configure(background='gainsboro')
	button5.configure(background='gainsboro')
	button6.configure(background='gainsboro')

	button7.configure(background='gainsboro')
	button8.configure(background='gainsboro')
	button9.configure(background='gainsboro')

def NewGame():
	reset()
	playerX.set(0)
	playerO.set(0)


label_playerX = Label(rightFrame1,font=('arial',40,'bold'),text='Player X:', pady=2,padx=2, bg='cadet Blue')
label_playerX.grid(row=0, column=0, sticky=W)

playerXENtry = Entry(rightFrame1, font=('arial',40,'bold'), bd=2, fg='black', textvariable=playerX, width=14, justify=LEFT)
playerXENtry.grid(row=0,column=1)

label_playerO = Label(rightFrame1,font=('arial',40,'bold'),text='Player O:', pady=2,padx=2, bg='cadet Blue')
label_playerO.grid(row=1, column=0, sticky=W)

playerOENtry = Entry(rightFrame1, font=('arial',40,'bold'), bd=2, fg='black', textvariable=playerO, width=14, justify=LEFT)
playerOENtry.grid(row=1,column=1)

resetButton = Button(rightFrame2,text='Reset', bg='gainsboro',font=('Time 26 bold'),height=1,width=20,command=reset)
resetButton.grid(row=0,column=0,padx=6,pady=11)

NewGameButton = Button(rightFrame2,text='New Game', bg='gainsboro',font=('Time 26 bold'),height=1,width=20,command=NewGame)
NewGameButton.grid(row=1,column=0,pady=10,padx=6)

button1 = Button(leftFrame,text='', bg='gainsboro',font=('Time 26 bold'),height=3,width=8,command= lambda:check(button1))
button1.grid(row=1,column=0,sticky= S+N+E+W)

button2 = Button(leftFrame,text='', bg='gainsboro',font=('Time 26 bold'),height=3,width=8,command= lambda:check(button2))
button2.grid(row=1,column=1,sticky= S+N+E+W)

button3 = Button(leftFrame,text='', bg='gainsboro',font=('Time 26 bold'),height=3,width=8,command= lambda:check(button3))
button3.grid(row=1,column=2,sticky= S+N+E+W)

button4 = Button(leftFrame,text='', bg='gainsboro',font=('Time 26 bold'),height=3,width=8,command= lambda:check(button4))
button4.grid(row=2,column=0,sticky= S+N+E+W)

button5 = Button(leftFrame,text='', bg='gainsboro',font=('Time 26 bold'),height=3,width=8,command= lambda:check(button5))
button5.grid(row=2,column=1,sticky= S+N+E+W)

button6 = Button(leftFrame,text='', bg='gainsboro',font=('Time 26 bold'),height=3,width=8,command= lambda:check(button6))
button6.grid(row=2,column=2,sticky= S+N+E+W)

button7 = Button(leftFrame,text='', bg='gainsboro',font=('Time 26 bold'),height=3,width=8,command= lambda:check(button7))
button7.grid(row=3,column=0,sticky= S+N+E+W)

button8 = Button(leftFrame,text='', bg='gainsboro',font=('Time 26 bold'),height=3,width=8,command= lambda:check(button8))
button8.grid(row=3,column=1,sticky= S+N+E+W)

button9 = Button(leftFrame,text='', bg='gainsboro',font=('Time 26 bold'),height=3,width=8,command= lambda:check(button9))
button9.grid(row=3,column=2,sticky= S+N+E+W)

root.mainloop()