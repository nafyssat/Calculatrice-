from tkinter import *
from functools import partial



    
#creer une fenetre 
root=Tk()

#afficher la fenetre

root.title("My Application")
root.geometry("400x400")
root.minsize(400,400)
root.iconbitmap("projet/imag/OIP.ico")
root.config(background='#A55050')
#frame
frame=Frame(root,bg='#A55050')
#text
titre=Label(frame,text="Calculatrice",font=("Courrier",30),bg="#A55050",fg='white')
titre.pack()

#autre frame
frame2=Frame(root,bg='#A55050')
haut=Frame(frame2,width=400,height=100,bd=2,relief=SUNKEN)
bas=Frame(frame2,bg='#A55050',width=400,height=300)
haut.grid(row=0,column=0)
bas.grid(row=1,column=0)
operateur=Frame(bas,bg='white',width=100,height=300)
cal=Frame(bas,bg='#A55050',width=300,height=300)
    
cal.grid(row=0,column=0)
operateur.grid(row=0,column=1)






affiche=Label(haut,text="",font=("Courrier",20),bg='white',fg='#A55050',width=20)
affiche.grid(row=0,column=0);
var=""



#fonction
def calculadd(n):
    global var
    n=var
    for i in range(0,len(n)):
        if(n[i]=="+" and i!=len(n)-1):
             affiche['text']=str(somme(n))
        if(n[i]=="-" and i!=len(n)-1):
             affiche['text']=str(sous(n))
        if(n[i]=="x" and i!=len(n)-1):
             affiche['text']=str(multi(n))
    var=""

def somme(n):
    for i in range(0,len(n)):
        if(n[i]=="+"):
            return int(n[0:i])+somme(n[i+1:len(n)])
    return int(n)
def sous(n):
    for i in range(0,len(n)):
        if(n[i]=="-"):
            return int(n[0:i])-sous(n[i+1:len(n)])
    return int(n)

def multi(n):
    for i in range(0,len(n)):
        if(n[i]=="x"):
            return int(n[0:i])*multi(n[i+1:len(n)])
    return int(n)
    
# autre frame
def calculateentree(n):
    global var
    var=var+str(n)
    affiche['text'] =var
    
    
   
   
   
    
def calculate():
    frame.pack_forget()
   
   
    k=1
    for i in range(0,3):
        for j in range(0,3):
            button=Button(cal,text=str(k), font=("Courrier",20),bg="white",fg='#A55050',width=3,command=partial(
    calculateentree, k))
            button.grid(row=i+1,column=j,padx=15,pady=10)
            k+=1
    button0=Button(cal,text="0", font=("Courrier",20),bg="white",fg='#A55050',width=3,command=partial(
    calculateentree, str(0)))
    button0.grid(row=4,column=1,padx=15,pady=10)
    
    button1=Button(operateur,text="=", font=("Courrier",20),bg="white",fg='#A55050',width=3,command=partial(calculadd,var))
    button1.grid(row=1,column=0,padx=10,pady=10)
    button2=Button(operateur,text="+", font=("Courrier",20),bg="white",fg='#A55050',command=partial(
    calculateentree, "+"))
    button2.grid(row=2,column=0,padx=10,pady=10)
    button3=Button(operateur,text="-", font=("Courrier",20),bg="white",fg='#A55050',command=partial(
    calculateentree, "-"))
    button3.grid(row=3,column=1,padx=10,pady=10)
    button4=Button(operateur,text="*", font=("Courrier",20),bg="white",fg='#A55050',command=partial(
    calculateentree, "x"))
    button4.grid(row=3,column=0,padx=10,pady=10)
    button4=Button(operateur,text="/", font=("Courrier",20),bg="white",fg='#A55050',command=partial(
    calculateentree, "/"))
    button4.grid(row=2,column=1,padx=10,pady=10)
   
   
    
    
    
    frame2.pack(expand=YES)
   
    

#button
buttons=Button(frame,text="LET'S GO", font=("Courrier",13),bg="white",fg='#A55050',command=calculate)
buttons.pack(pady=25,fill=X)

frame.pack(expand=YES)
root.mainloop()