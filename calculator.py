from tkinter import *
root=Tk()
#title of  the application
root.title(" pushpa calculator")
e=Entry(root,width=50,borderwidth=20,fg="blue")
e.grid(row=0,column=0,columnspa=20,padx=20,pady=30)


#declaring functions
def buttonclick(number):
    #e.delete(0,END)# delete the numbers of pre
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))
def clear():
    e.delete(0,END)
def buttonadd():
    firstnum=e.get()
    global fnum
    global math
    math="add"
    fnum=int(firstnum)
    e.delete(0,END)
def equal():
    secondnum=e.get()
    e.delete(0,END)
    if math=="add":
        e.insert(0,fnum+int(secondnum))
    elif math=="sub":
        e.insert(0,fnum-int(secondnum))
    elif math=="mul":
        e.insert(0,fnum*int(secondnum))
    elif math=="div":
        e.insert(0,fnum/int(secondnum))
    elif math=="pow":
        e.insert(0,fnum**int(secondnum))
#functions that calculate globe is used to access another functions
def sub():
    firstnum=e.get()
    global fnum
    global math
    math="sub"
    fnum=int(firstnum)
    e.delete(0,END)
    return
def mul():
    firstnum=e.get()
    global fnum
    global maath
    math="mul"
    fnum=int(firstnum)
    e.delete(0,END)
    return
def div():
    firstnum=e.get()
    global fnum
    global math
    math="div"
    fnum=int(firstnum)
    e.delete(0,END)
    return
def pow():
    firstnum=e.get()
    global fnum
    global math
    math="pow"
    fnum=int(firstnum)
    e.delete(0,END)
    return
#creation of the buttons
button1=Button(root,text="1",padx=40,pady=20,command=lambda:buttonclick(1))
button2=Button(root,text="2",padx=40,pady=20,command=lambda:buttonclick(2))
button3=Button(root,text="3",padx=40,pady=20,command=lambda:buttonclick(3))
button4=Button(root,text="4",padx=40,pady=20,command=lambda:buttonclick(4))
button5=Button(root,text="5",padx=40,pady=20,command=lambda:buttonclick(5))
button6=Button(root,text="6",padx=40,pady=20,command=lambda:buttonclick(6))
button7=Button(root,text="7",padx=40,pady=20,command=lambda:buttonclick(7))
button8=Button(root,text="8",padx=40,pady=20,command=lambda:buttonclick(8))
button9=Button(root,text="9",padx=40,pady=20,command=lambda:buttonclick(9))
button0=Button(root,text="0",padx=40,pady=20,command=lambda:buttonclick(0))


#operations
buttonaddd=Button(root,text="+",padx=40,pady=20,command=buttonadd)
buttonsub=Button(root,text="-",padx=40,pady=20,command=sub)
buttonmul=Button(root,text="*",padx=40,pady=20,command=mul)
buttondiv=Button(root,text="/",padx=40,pady=20,command=div)
buttonequal=Button(root,text="=",padx=40,pady=20,command=equal)
buttonclear=Button(root,text="clear",padx=40,pady=20,command=clear)
buttonpow=Button(root,text="pow",padx=40,pady=20,command=pow)
buttonquit=Button(root,text="exit",padx=40,pady=20,command=root.quit)
#buttonquit.pack()
#put button on screen
button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)
button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)
button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)
button0.grid(row=4,column=0)
buttonaddd.grid(row=4,column=1)
buttonsub.grid(row=4,column=2)
buttonmul.grid(row=5,column=0)
buttondiv.grid(row=5,column=1)
buttonclear.grid(row=6,column=0)
buttonequal.grid(row=5,column=2)
buttonpow.grid(row=6,column=1)
buttonquit.grid(row=6,column=2)
#without this the application couldn't run
root.mainloop()