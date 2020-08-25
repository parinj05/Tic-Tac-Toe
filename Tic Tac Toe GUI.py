from tkinter import *
import pygame
turn=1; 
x=0
o=0
pygame.mixer.init()
def reset():

    root = Tk()
    root.size
    root.title("PJ's TIC-Tac-Toe ")
    root.geometry("414x500")
    root.configure(bg="pink")

    
    def soundClick():
        pygame.mixer.music.load("C:\\Users\\Parin Joshi\\Desktop\\Python Files\\Tic Tac Toe\\Mouse Click - Free Sound Effect.mp3")
        pygame.mixer.music.play(loops=0)

    def cheers():
        pygame.mixer.music.load("C:\\Users\\Parin Joshi\\Desktop\\Python Files\\Tic Tac Toe\\Cheering sound effect.mp3")
        pygame.mixer.music.play(loops=2)

    def sadSound():
        pygame.mixer.music.load("C:\\Users\\Parin Joshi\\Desktop\\Python Files\\Tic Tac Toe\\uh oh.mp3")
        pygame.mixer.music.play(loops=2)

    def create_button():

        def close():
            root.destroy()
        
        def win(button):
            global turn,x,o
            cheers()
            lbl = Label(root,bg="pink",width=100,height=100).grid(column=0,row=0)
            if button=='X':
                x+=1
            elif button == 'O':
                o+=1
            text1 = Label(root,text="CONGRATULATIONS!", font=('Helvetica','20'),bg="pink")
            text1.place(x=70,y=120)
            text2 = Label(root,text=button+ " won", font=('Helvetica','20'),bg="pink")
            text2.place(x=170,y=160)
            turn=1
            restart = Button(root,text="Ready for a new match?", bg="black",fg="pink",width=25,height=2,font=("Helvetica","15"),activebackground = "pink",command = lambda:[soundClick(),close(),reset()])
            restart.place(x=70,y=220)
            gameOver = Button(root,text="Nah, I'd rather quit.", bg="black",fg="pink",width=25,height=2,font=("Helvetica","15"), activebackground = "pink",command = lambda:[soundClick(),close()])
            gameOver.place(x=70,y=300)



        def clicked1(btn):
            
            global turn
            if btn["text"]==" ":   #For getting the text of a button
                if turn%2!=0:
                    btn["text"]="X"
                elif turn%2==0:
                    btn["text"]="O"
                turn+=1
            
            if (btn1["text"]==btn2['text'] and btn2["text"]==btn3['text'] and btn1["text"]=="X") or (btn1["text"]==btn2['text'] and btn2["text"]==btn3['text'] and btn1["text"]=="O"):
                win(btn1['text'])
            
            if (btn4["text"]==btn5['text'] and btn5["text"]==btn6['text'] and btn4["text"]=="X") or (btn4["text"]==btn5['text'] and btn5["text"]==btn6['text'] and btn4["text"]=="O"):
                win(btn4['text'])

            if (btn7["text"]==btn8['text'] and btn8["text"]==btn9['text'] and btn7["text"]=="X") or (btn7["text"]==btn8['text'] and btn8["text"]==btn9['text'] and btn7["text"]=="O"):
                win(btn7['text'])

            if (btn1["text"]==btn4['text'] and btn4["text"]==btn7['text'] and btn7["text"]=="X") or (btn1["text"]==btn4['text'] and btn4["text"]==btn7['text'] and btn7["text"]=="O"):
                win(btn1['text'])

            if (btn2["text"]==btn5['text'] and btn5["text"]==btn8['text'] and btn2["text"]=="X") or (btn2["text"]==btn5['text'] and btn5["text"]==btn8['text'] and btn2["text"]=="O"):
                win(btn2['text'])

            if (btn3["text"]==btn6['text'] and btn6["text"]==btn9['text'] and btn3["text"]=="X") or (btn3["text"]==btn6['text'] and btn6["text"]==btn9['text'] and btn3["text"]=="O"):
                win(btn3['text'])

            if (btn1["text"]==btn5['text'] and btn5["text"]==btn9['text'] and btn1["text"]=="X") or (btn1["text"]==btn5['text'] and btn5["text"]==btn9['text'] and btn1["text"]=="O"):
                win(btn1['text'])

            if (btn3["text"]==btn5['text'] and btn5["text"]==btn7['text'] and btn3["text"]=="X") or (btn3["text"]==btn5['text'] and btn5["text"]==btn7['text'] and btn3["text"]=="O"):
                win(btn3['text'])

            if turn == 10:
                lbl = Label(root,bg="pink",width=100,height=100).grid(column=0,row=0)
                sadSound()
                text2 = Label(root,text="It's a Tie", font=('Helvetica','20'),bg="pink")
                text2.place(x=170,y=110)
                restart = Button(root,text="Ready for a new match?", bg="black",fg="pink",width=25,height=2,font=("Helvetica","15"),activebackground = "pink",command = lambda:[soundClick(),close(),reset()])
                restart.place(x=70,y=170)
                gameOver = Button(root,text="Nah, I'd rather quit.", bg="black",fg="pink",width=25,height=2,font=("Helvetica","15"),command=lambda:[soundClick(),close()])
                gameOver.place(x=70,y=260)
                
            
        global x,o

        frame1 = Label(root,bg="pink",text = "X wins: "+ str(x),font=("Helvetica","15")).place(x=25,y=10)
        frame2 = Label(root,bg="pink",text = "O wins: "+ str(o),font=("Helvetica","15")).place(x=300,y=10)
      

        btn1 = Button(root, text=" ",bg="black", fg="pink",width=8,height=4,font=('Helvetica','20'),activebackground = "pink",command=lambda:[soundClick(),clicked1(btn1)])
        btn1.place(x=0,y=50)
        btn2 = Button(root, text=" ",bg="black", fg="pink",width=8,height=4,font=('Helvetica','20'),activebackground = "pink",command=lambda:[soundClick(),clicked1(btn2)])
        btn2.place(x=138,y=50)
        btn3 = Button(root, text=" ",bg="black", fg="pink",width=8,height=4,font=('Helvetica','20'),activebackground = "pink",command=lambda:[soundClick(),clicked1(btn3)])
        btn3.place(x=276,y=50)
        btn4 = Button(root, text=" ",bg="black", fg="pink",width=8,height=4,font=('Helvetica','20'),activebackground = "pink",command=lambda:[soundClick(),clicked1(btn4)])
        btn4.place(x=0,y=200)
        btn5 = Button(root, text=" ",bg="black", fg="pink",width=8,height=4,font=('Helvetica','20'),activebackground = "pink",command=lambda:[soundClick(),clicked1(btn5)])
        btn5.place(x=138,y=200)
        btn6 = Button(root, text=" ",bg="black", fg="pink",width=8,height=4,font=('Helvetica','20'),activebackground = "pink",command=lambda:[soundClick(),clicked1(btn6)])
        btn6.place(x=276,y=200)
        btn7 = Button(root, text=" ",bg="black", fg="pink",width=8,height=4,font=('Helvetica','20'),activebackground = "pink",command=lambda:[soundClick(),clicked1(btn7)])
        btn7.place(x=0,y=350)
        btn8 = Button(root, text=" ",bg="black", fg="pink",width=8,height=4,font=('Helvetica','20'),activebackground = "pink",command=lambda:[soundClick(),clicked1(btn8)])
        btn8.place(x=138,y=350)
        btn9 = Button(root, text=" ",bg="black", fg="pink",width=8,height=4,font=('Helvetica','20'),activebackground = "pink",command=lambda:[soundClick(),clicked1(btn9)])
        btn9.place(x=276,y=350)

        
        
        
        

    a= Label(root,text="          ",bg="pink",font=("Helvetica","20")).grid(row=0,column=0)
    b= Label(root,text="          ",bg="pink",font=("Helvetica","20")).grid(row=1,column=1)
    ab= Label(root,text="        ",bg="pink",font=("Helvetica","20")).grid(row=2,column=2)
    bc= Label(root,text="        ",bg="pink",font=("Helvetica","20")).grid(row=3,column=3)
    bc= Label(root,text="        ",bg="pink",font=("Helvetica","20")).grid(row=4,column=0)
    welcome = Label(root,text="Welcome to",bg="pink",font=("Helvetica","20")).grid(row=4,column=1)
    ttt = Label(root,text="PJ's TIC-TAC-TOE",bg="pink",font=("Helvetica","20")).grid(row=5,column=1) 
    c= Label(root,text="         ",bg="pink",font=("Helvetica","20")).grid(row=6,column=1)

    start = Button(root,text="START", bg="black",fg="pink",width=30,height=2,font=("Helvetica","10"),activebackground = "pink",command=lambda:[soundClick(),create_button()])
    start.grid(row=7,column=1)


    root.mainloop()

reset()
