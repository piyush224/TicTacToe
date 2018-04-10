from Tkinter import *
import tkMessageBox

root = Tk()
root.title("Tic Tec Toe")
click = True
v = IntVar()
v.set(1)
nameX = StringVar()
nameY = StringVar()
countx = 0
county = 0

def count_win(ch):
    global countx,county
    if ch == "X":
        countx += 1
    else:
        county += 1

def showChoice():
    var = v.get()
    btn1.config(bg = color1[var])
    btn2.config(bg = color1[var])
    btn3.config(bg = color1[var])
    btn4.config(bg = color1[var])
    btn5.config(bg = color1[var])
    btn6.config(bg = color1[var])
    btn7.config(bg = color1[var])
    btn8.config(bg = color1[var])
    btn9.config(bg = color1[var])

color = [("sienna",1),("limegreen",2),("aqua",3),("rosybrown",4),("darkgray",5)]
color1 = {1: "sienna", 2:"limegreen",3:"aqua",4:"rosybrown",5:"darkgray"}

lab = Label(root,text = "Choose Color Of Board",justify = LEFT,padx = 20,width = 20,bg = "powder blue",bd = 5).grid()

for txt,num in color:
    Radiobutton(root,text = txt,value = num,variable = v,padx = 20,indicatoron = 0,width = 20,bg = txt,command =showChoice).grid()

labX = Label(root,text = "Name of player[X]",justify= LEFT,padx = 20,width = 20 ,bd = 5).grid(column = 1,row = 0)
labO = Label(root,text = "Name of player[O]",justify= LEFT,padx = 20,width = 20 ,bd = 5).grid(column = 1,row = 1)
NameX = Entry(root,text = "Name of player[X]",justify= LEFT,width = 25 ,bd = 5,textvariable = nameX).grid(column = 2,row = 0)
NameO = Entry(root,text = "Name of player[O]",justify= LEFT,width = 25 ,bd = 5,textvariable = nameY).grid(column = 2,row = 1)
labGX = Label(root,text = "Player[X]", justify= LEFT,padx = 20,width = 20 ,bd = 5).grid(column = 1,row = 2)
labGY = Label(root,text = "Player[Y]", justify= LEFT,padx = 20,width = 20 ,bd = 5).grid(column = 1,row = 3)
labwx = Label(root,text = countx, justify= LEFT,padx = 20,width = 20 ,bd = 5).grid(column = 2,row = 2)
labwy = Label(root,text = county, justify= LEFT,padx = 20,width = 20 ,bd = 5).grid(column = 2,row = 3)
labw = Label(root,text = "Draw", justify= LEFT,padx = 20,width = 20 ,bd = 5).grid(column = 1,row = 4)
labwd = Label(root,text = "0", justify= LEFT,padx = 20,width = 20 ,bd = 5).grid(column = 2,row = 4)

def Click(buttons):
    global click  
    if buttons["text"] == " " and click == True:
        buttons["text"] = "O"
        click = False

    elif buttons["text"] == " " and click == False:
        buttons["text"] = "X"
        click = True

    elif btn1["text"] == "X" and btn2["text"]== "X" and btn3["text"]=="X"or btn4["text"] == "X" and btn5["text"]=="X" and btn6["text"]=="X" or btn7["text"] =="X" and btn8["text"]=="X" and btn9["text"]=="X" or btn1["text"] =="X" and btn4["text"]=="X" and btn7["text"]=="X" or btn2["text"] == "X"and btn5["text"]=="X"and btn8["text"]=="X" or btn3["text"] == "X" and btn6["text"]=="X"and btn9["text"]=="X" or btn1["text"] =="X"and btn5["text"]=="X"and btn9["text"]=="X" or btn3["text"] =="X"and btn5["text"]=="X" and btn7["text"]=="X":
          count_win("X") 
          tkMessageBox.showinfo("X won","you have just won the game")

    elif btn1["text"] == "O" and btn2["text"]== "O" and btn3["text"]=="O"or btn4["text"] == "O" and btn5["text"]=="O"and btn6["text"]=="O" or btn7["text"] =="O"and btn8["text"]=="O"and btn9["text"]=="O" or btn1["text"] =="O" and btn4["text"]=="O" and btn7["text"]=="O" or btn2["text"] == "O"and btn5["text"]=="O"and btn8["text"]=="O" or btn3["text"] == "O" and btn6["text"]=="O"and btn9["text"]=="O" or btn1["text"] =="O"and btn5["text"]=="O"and btn9["text"]=="O" or btn3["text"] =="O"and btn5["text"]=="O" and btn7["text"]=="O":
          count_win("O")
          tkMessageBox.showinfo("O Won","you have just won the game")

    else:
          tkMessageBox.showinfo("Ohh..","Drawn")
        


      

 

buttons = StringVar()

btn1 = Button(root,font = 'Times 26 bold',width = 8,height = 4,command = lambda:Click(btn1),text = " " ,bg = "sienna")
btn1.grid(row = 6,column = 0,sticky = N+W+S+E)
btn2 = Button(root,font = 'Times 26 bold',width = 8,height = 4,command = lambda:Click(btn2),text = " ",bg = "sienna" )
btn2.grid(row = 6,column = 1,sticky = N+W+S+E)
btn3 = Button(root,font = 'Times 26 bold',width = 8,height = 4,command = lambda:Click(btn3),text = " ",bg = "sienna" )
btn3.grid(row = 6,column = 2,sticky = N+W+S+E)


btn4 = Button(root,font = 'Times 26 bold',width = 8,height = 4,command = lambda:Click(btn4),text = " ",bg = "sienna" )
btn4.grid(row = 7,column = 0,sticky = N+W+S+E)
btn5 = Button(root,font = 'Times 26 bold',width = 8,height = 4,command = lambda:Click(btn5),text = " ",bg = "sienna" )
btn5.grid(row = 7,column = 1,sticky = N+W+S+E)
btn6 = Button(root,font = 'Times 26 bold',width = 8,height = 4,command = lambda:Click(btn6),text = " ",bg = "sienna" )
btn6.grid(row = 7,column = 2,sticky = N+W+S+E)

btn7 = Button(root,font = 'Times 26 bold',width = 8,height = 4,command = lambda:Click(btn7),text = " ",bg = "sienna" )
btn7.grid(row = 8,column = 0,sticky = N+W+S+E)
btn8 = Button(root,font = 'Times 26 bold',width = 8,height = 4,command = lambda:Click(btn8),text = " ",bg = "sienna" )
btn8.grid(row = 8,column = 1,sticky = N+W+S+E)
btn9 = Button(root,font = 'Times 26 bold',width = 8,height = 4,command = lambda:Click(btn9),text = " ",bg = "sienna" )
btn9.grid(row = 8,column = 2,sticky = N+W+S+E)


root.mainloop()
