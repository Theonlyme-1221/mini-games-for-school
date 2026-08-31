from tkinter import *
from PIL import ImageTk , Image

win = Tk()
win.geometry("1370x1000")

win.title("Guess The Correct Option Program")

def o():
    global data,data1,a,b,c,d,e,f,g,h,i,j,a1,b1,c1,d1,e1,f1,g1,h1,i1,j1,z
    a=ent[0].get()
    b=ent[1].get()
    c=ent[2].get()
    d=ent[3].get()
    e=ent[4].get()
    f=ent[5].get()
    g=ent[6].get()
    h=ent[7].get()
    i=ent[8].get()
    j=ent[9].get()
    print(a,b,c,d,e,f,g,h,i,j)
    a1=' '
    b1=c1=d1=e1=f1=h1=i1=j1=' '
    g1=' '

    '''if a=='a'and b=='b'and c=='c'and d=='d'and e=='5'and f=='6' and g=='7' and h=='8'and i=='9' and j=='10':
        print(a,b,c,d,e,f,g,h,i,j,'hi')'''
    z=10
    if a!='c':
        a=' '
        a1='Ares Chevrolet Corvette Stingray'
        z-=1
    else:
        a='Ares Chevrolet Corvette Stingray'
    if b!='d':
        b=' '
        b1='1962 Corvette Hardtop Restomod'
        z-=1
    else:
        b='1962 Corvette Hardtop Restomod'
    if c!='a':
        c=' '
        c1='Devon GTX'
        z-=1
    else:
        c='Devon GTX'
    if d!='a':
        d=' '
        d1='PositDodge Viper Hennessey Venom 1000 Twin Turbo'
        z-=1
    else:
        d='PositDodge Viper Hennessey Venom 1000 Twin Turbo'
    if e!='a':
        e=' '
        e1='Kellison J6'
        z-=1
    else:
        e='Kellison J6'
    if f!='b':
        f=' '
        f1='DeLorean DMC12 Restomod'
        z-=1
    else:
        f='DeLorean DMC12 Restomod'
    if g!='c':
        g=' '
        g1='Shelby Cobra V12'
        z-=1
    else:
        g='Shelby Cobra V12'
    if h!='a':
        h=' '
        h1='Dodge Viper Hennessey Venom 1000 Twin Turbo'
        z-=1
    else:
        h='Dodge Viper Hennessey Venom 1000 Twin Turbo'
    if i!='c':
        i=' '
        i1='Ford Mustang Mach 40'
        z-=1
    else:
        i='Ford Mustang Mach 40'
    if j!='a':
        j=' '
        j1='1962 Chevrolet Corvette C1 RS Restomod'
        z-=1
    else:
        j='1962 Chevrolet Corvette C1 RS Restomod'
    data=[
    ['Sl.no.','Correct Answer','Mark',' '],
    [f"{1:^6d}",a,420,' ',' '],
    [f"{2:^6d}",b,22,' ',' '],
    [f"{3:^6d}",c,3,' ',' '],
    [f"{4:^6d}",d,3,' ',' '],
    [f"{5:^6d}",e,3,' ',' '],
    [f"{6:^6d}",f,3,' ',' '],
    [f"{7:^6d}",g,3,' ',' '],
    [f"{8:^6d}",h,3,' ',' '],
    [f"{9:^6d}",i,3,' ',' '],
    [f"{10:^6d}",j,3,' ',' ']
    ]
    data1=[
    ['Sl.no.','Wrong Answer','Mark'],
    [f"{1:^6d}",a1,42,' ',' '],
    [f"{2:^6d}",b1,2,' ',' '],
    [f"{3:^6d}",c1,30,' ',' '],
    [f"{4:^6d}",d1,3,' ',' '],
    [f"{5:^6d}",e1,3,' ',' '],
    [f"{6:^6d}",f1,3,' ',' '],
    [f"{7:^6d}",g1,3,' ',' '],
    [f"{8:^6d}",h1,3,' ',' '],
    [f"{9:^6d}",i1,3,' ',' '],
    [f"{10:^6d}",j1,'Total Mark ',z ]
    ]
    print(z)

def ans():
    root=Tk()
    root.geometry('1370x420')
    root.title("i am Program") 
    o()
    totalrow=len(data)
    totalcolum=len(data[0])
    class Table:
        def __init__(self,root):
            for i in range(totalrow):
                for j in range(totalcolum):
                    #self.e=Entry(border=10,borderwidth=10,relief='ridge',fg="black",bg="lime", font=('courier',15, 'bold'))
                    self.e=Entry(root,width=6,fg="black", font=('courier',15, 'bold'))
                    self.e.grid(row=i,column=1)
                    self.e.insert(END,data1[i][0])
            
                    #self.e=Entry(border=10,borderwidth=10,relief='ridge',fg="black",bg="lime", font=('courier',15, 'bold'))
                    self.e=Entry(root,width=54,fg="black",bg="red", font=('courier',15, 'bold'))
                    self.e.grid(row=i,column=3)
                    self.e.insert(END,data1[i][1])

                    #self.e=Entry(border=10,borderwidth=10,relief='ridge',fg="black",bg="lime", font=('courier',15, 'bold'))
                    self.e=Entry(root,width=54,fg="black",bg="lime", font=('courier',15, 'bold'))
                    self.e.grid(row=i,column=6)
                    self.e.insert(END,data[i][1])
                    
                    self.e=Entry(root,border=5,borderwidth=5,width=11,relief='ridge',fg="black",bg="lime", font=('courier',25, 'bold'))
                    #self.e=Entry(root,width=11,fg="black", font=('courier',25, 'bold'))
                    self.e.place(x=200,y=350)
                    self.e.insert(END,data1[10][2])
                    
                    #self.e=Entry(root,width=2,fg="black", font=('courier',25, 'bold'))
                    self.e=Entry(root,border=5,borderwidth=5,width=2,relief='ridge',fg="black",bg="lime", font=('courier',25, 'bold'))
                    self.e.place(x=433,y=350)
                    self.e.insert(END,data1[10][3])

                    #ent[0].delete(0, END)

            
    z=Table(root)
    t=Table(root)
    nex[19].place_forget()
    nex[20].place(x=619,y=540)
    root.mainloop()
    

#Label(root,text='10').pack()
def nex1():

    m[0].place_forget()
    m[1].place_forget()
    m[2].place_forget()
    m[3].place_forget()
    m[4].place_forget()
    m[5].place_forget()
    
    my_label[10].place_forget()
    my_label[11].place_forget()
    my_label[12].place_forget()
    my_label[13].place_forget()

    my_label[0].pack(pady=50)
    op[0].place(x=400,y=310)
    op[1].place(x=400,y=350)
    op[2].place(x=400,y=390)
    op[3].place(x=400,y=430)
    ent[0].place(x=650,y=490)
    nex[0].place(x=619,y=540)
    ent[0].delete(0, END)


def nexa1():
    if ent[0].get().lower()=='c':
        nex2()
    else:  
        nex[0].place_forget()   
        nex[10].place(x=619,y=540)
        a11[0].place(x=400,y=600)
def nex2():
    my_label[0].pack_forget()
    op[0].place_forget()
    op[1].place_forget()
    op[2].place_forget()
    op[3].place_forget()
    ent[0].place_forget()
    nex[0].place_forget()

    a11[0].place_forget()
    nex[10].place_forget()

    my_label[1].pack(pady=50)
    op[4].place(x=400,y=310)
    op[5].place(x=400,y=350)
    op[6].place(x=400,y=390)
    op[7].place(x=400,y=430)
    ent[1].place(x=650,y=490)
    nex[1].place(x=619,y=540) 
    ent[1].delete(0, END)

def nexa2():
    if ent[1].get().lower()=='d':
        nex3()
    else:
        nex[1].place_forget()   
        nex[11].place(x=619,y=540)
        a11[1].place(x=400,y=600)
        
def nex3():
    my_label[1].pack_forget()
    op[4].place_forget()
    op[5].place_forget()
    op[6].place_forget()
    op[7].place_forget()
    ent[1].place_forget()
    nex[1].place_forget()

    a11[1].place_forget()
    nex[11].place_forget()

    my_label[2].pack(pady=50)
    op[8].place(x=400,y=310)
    op[9].place(x=400,y=350)
    op[10].place(x=400,y=390)
    op[11].place(x=400,y=430)
    ent[2].place(x=650,y=490)
    nex[2].place(x=619,y=540) 
    ent[2].delete(0, END)

def nexa3():
    if ent[2].get().lower()=='a':
        nex4()
    else:
        nex[2].place_forget()   
        nex[12].place(x=619,y=540)
        a11[2].place(x=400,y=600)
def nex4():
    my_label[2].pack_forget()
    op[8].place_forget()
    op[9].place_forget()
    op[10].place_forget()
    op[11].place_forget()
    ent[2].place_forget()
    nex[2].place_forget()
    
    a11[2].place_forget()
    nex[12].place_forget()

    my_label[3].pack(pady=50)
    op[12].place(x=400,y=310)
    op[13].place(x=400,y=350)
    op[14].place(x=400,y=390)
    op[15].place(x=400,y=430)
    ent[3].place(x=650,y=490)
    nex[3].place(x=619,y=540)
    ent[3].delete(0, END)

def nexa4():
    if ent[3].get().lower()=='a':
        nex5()
    else:
        nex[3].place_forget() 
        nex[13].place(x=619,y=540)
        a11[3].place(x=400,y=600)

def nex5():
    my_label[3].pack_forget()
    op[12].place_forget()
    op[13].place_forget()
    op[14].place_forget()
    op[15].place_forget()
    ent[3].place_forget()
    nex[3].place_forget()

    a11[3].place_forget()
    nex[13].place_forget()

    my_label[4].pack(pady=50)
    op[16].place(x=400,y=310)
    op[17].place(x=400,y=350)
    op[18].place(x=400,y=390)
    op[19].place(x=400,y=430)
    ent[4].place(x=650,y=490)
    nex[4].place(x=619,y=540)
    ent[4].delete(0, END)

def nexa5():
    if ent[4].get().lower()=='a':
        nex6()
    else:
        nex[4].place_forget()   
        nex[14].place(x=619,y=540)
        a11[4].place(x=400,y=600)

def nex6():
    my_label[4].pack_forget()
    op[16].place_forget()
    op[17].place_forget()
    op[18].place_forget()
    op[19].place_forget()
    ent[4].place_forget()
    nex[4].place_forget()

    a11[4].place_forget()
    nex[14].place_forget()

    my_label[5].pack(pady=50)
    op[20].place(x=400,y=310)
    op[21].place(x=400,y=350)
    op[22].place(x=400,y=390)
    op[23].place(x=400,y=430)
    ent[5].place(x=650,y=490)
    nex[5].place(x=619,y=540)
    ent[5].delete(0, END)

def nexa6():
    if ent[5].get().lower()=='b':
        nex7()
    else:
        nex[5].place_forget()   
        nex[15].place(x=619,y=540)
        a11[5].place(x=400,y=600)

def nex7():
    my_label[5].pack_forget()
    op[20].place_forget()
    op[21].place_forget()
    op[22].place_forget()
    op[23].place_forget()
    ent[5].place_forget()
    nex[5].place_forget()

    a11[5].place_forget()
    nex[15].place_forget()

    my_label[6].pack(pady=50)
    op[24].place(x=400,y=310)
    op[25].place(x=400,y=350)
    op[26].place(x=400,y=390)
    op[27].place(x=400,y=430)
    ent[6].place(x=650,y=490)
    nex[6].place(x=619,y=540)
    ent[6].delete(0, END)

def nexa7():
    if ent[6].get().lower()=='c':
        nex8()
    else:
        nex[6].place_forget()  
        nex[16].place(x=619,y=540)
        a11[6].place(x=400,y=600)



def nex8():
    my_label[6].pack_forget()
    op[24].place_forget()
    op[25].place_forget()
    op[26].place_forget()
    op[27].place_forget()
    ent[6].place_forget()
    nex[6].place_forget()

    a11[6].place_forget()
    nex[16].place_forget()

    my_label[7].pack(pady=50)
    op[28].place(x=400,y=310)
    op[29].place(x=400,y=350)
    op[30].place(x=400,y=390)
    op[31].place(x=400,y=430)
    ent[7].place(x=650,y=490)
    nex[7].place(x=619,y=540)
    ent[7].delete(0, END)

def nexa8():
    if ent[7].get().lower()=='a':
        nex9()
    else:
        nex[7].place_forget()
        nex[17].place(x=619,y=540)
        a11[7].place(x=400,y=600)

def nex9():
    my_label[7].pack_forget()
    op[28].place_forget()
    op[29].place_forget()
    op[30].place_forget()
    op[31].place_forget()
    ent[7].place_forget()
    nex[7].place_forget()

    a11[7].place_forget()
    nex[17].place_forget()

    my_label[8].pack(pady=50)
    op[32].place(x=400,y=310)
    op[33].place(x=400,y=350)
    op[34].place(x=400,y=390)
    op[35].place(x=400,y=430)
    ent[8].place(x=650,y=490)
    nex[8].place(x=619,y=540)
    ent[8].delete(0, END)

def nexa9():
    if ent[8].get().lower()=='c':
        nex10()
    else:
        nex[8].place_forget()   
        nex[18].place(x=619,y=540)
        a11[8].place(x=400,y=600)

def nex10():
    my_label[8].pack_forget()
    op[32].place_forget()
    op[33].place_forget()
    op[34].place_forget()
    op[35].place_forget()
    ent[8].place_forget()
    nex[8].place_forget()

    a11[8].place_forget()
    nex[18].place_forget()

    my_label[9].pack(pady=50)
    op[36].place(x=400,y=310)
    op[37].place(x=400,y=350)
    op[38].place(x=400,y=390)
    op[39].place(x=400,y=430)
    ent[9].place(x=650,y=490)
    nex[9].place(x=619,y=540)
    ent[9].delete(0, END)

def ss():
    ans()
def nexa10():
    found=False
    if ent[9].get().lower()=='a':
        nex[9].place_forget()  
        nex[20].place(x=619,y=540)
        ans()
        
    else:
        nex[9].place_forget()   
        z11.place(x=400,y=600)
        nex[19].place(x=619,y=540)

def main():    
    my_label[9].pack_forget()
    op[36].place_forget()
    op[37].place_forget()
    op[38].place_forget()
    op[39].place_forget()
    ent[9].place_forget()
    nex[9].place_forget()

    z11.place_forget()
    nex[20].place_forget()
    
    m[3].place(x=50,y=30)

    m[0].place(x=40,y=500)
    m[1].place(x=430,y=270)
    m[2].place(x=40,y=400)
    m[4].place(x=40,y=580)
    m[5].place(x=380,y=130)


    my_label[11].place(x=900,y=30)
    my_label[12].place(x=50,y=150)
    my_label[13].place(x=930,y=380)
    my_label[10].place(x=0,y=0,relwidth=1,relheight=1)
    
    
z11=Label(win,text='1962 Chevrolet Corvette C1 RS Restomod', fg="black",font=('courier', 20, 'bold'))


nex=(Button(text='Next',bg="blue", fg="yellow",activebackground='black',activeforeground='yellow', relief='solid', font=('courier', 20, 'bold'),command=nexa1),
    Button(text='Next',bg="blue", fg="yellow", activebackground='black',activeforeground='yellow',relief='solid', font=('courier', 20, 'bold'),command=nexa2),
    Button(text='Next',bg="blue", fg="yellow",activebackground='black',activeforeground='yellow', relief='solid', font=('courier', 20, 'bold'),command=nexa3),
    Button(text='Next',bg="blue", fg="yellow",activebackground='black',activeforeground='yellow', relief='solid', font=('courier', 20, 'bold'),command=nexa4),
    Button(text='Next',bg="blue", fg="yellow",activebackground='black',activeforeground='yellow', relief='solid', font=('courier', 20, 'bold'),command=nexa5),
    Button(text='Next',bg="blue", fg="yellow", activebackground='black',activeforeground='yellow',relief='solid', font=('courier', 20, 'bold'),command=nexa6),
    Button(text='Next',bg="blue", fg="yellow", activebackground='black',activeforeground='yellow',relief='solid', font=('courier', 20, 'bold'),command=nexa7),
    Button(text='Next',bg="blue", fg="yellow",activebackground='black',activeforeground='yellow', relief='solid', font=('courier', 20, 'bold'),command=nexa8),
    Button(text='Next',bg="blue", fg="yellow", activebackground='black',activeforeground='yellow',relief='solid', font=('courier', 20, 'bold'),command=nexa9),
    Button(text='Next',bg="blue", fg="yellow",activebackground='black',activeforeground='yellow', relief='solid', font=('courier', 20, 'bold'),command=nexa10),
    Button(text='Next',bg="blue", fg="yellow", activebackground='black',activeforeground='yellow',relief='solid', font=('courier', 20, 'bold'),command=nex2),
    Button(text='Next',bg="blue", fg="yellow",activebackground='black',activeforeground='yellow', relief='solid', font=('courier', 20, 'bold'),command=nex3),
    Button(text='Next',bg="blue", fg="yellow",activebackground='black',activeforeground='yellow', relief='solid', font=('courier', 20, 'bold'),command=nex4),
    Button(text='Next',bg="blue", fg="yellow",activebackground='black',activeforeground='yellow', relief='solid', font=('courier', 20, 'bold'),command=nex5),
    Button(text='Next',bg="blue", fg="yellow",activebackground='black',activeforeground='yellow', relief='solid', font=('courier', 20, 'bold'),command=nex6),
    Button(text='Next',bg="blue", fg="yellow",activebackground='black',activeforeground='yellow', relief='solid', font=('courier', 20, 'bold'),command=nex7),
    Button(text='Next',bg="blue", fg="yellow",activebackground='black',activeforeground='yellow', relief='solid', font=('courier', 20, 'bold'),command=nex8),
    Button(text='Next',bg="blue", fg="yellow",activebackground='black',activeforeground='yellow', relief='solid', font=('courier', 20, 'bold'),command=nex9),
    Button(text='Next',bg="blue", fg="yellow",activebackground='black',activeforeground='yellow', relief='solid', font=('courier', 20, 'bold'),command=nex10),
    Button(text='SCORE',bg="blue", fg="yellow",activebackground='black',activeforeground='yellow', relief='solid', font=('courier', 20, 'bold'),command=ans),
    Button(text='Main',bg="blue", fg="yellow",activebackground='black',activeforeground='yellow', relief='solid', font=('courier', 20, 'bold'),command=main)#,command=ans)
    )
op=(Label(text='a)Ford Mustang GT Premium 2-Door Convertible', fg="black",font=('courier', 20, 'bold')),
    Label(text='b)Jaguar F-Type P300', fg="black",font=('courier', 20, 'bold')),
    Label(text='c)Ares Chevrolet Corvette Stingray', fg="black",font=('courier', 20, 'bold')),
    Label(text='d)Mazda MX-5 Miata Sport', fg="black",font=('courier', 20, 'bold')),
    Label(text='a)Aston Martin DB11 Base V8 Coupe', fg="black",font=('courier', 20, 'bold')),
    Label(text='b)1958 Corvette with C5 Components', fg="black",font=('courier', 20, 'bold')),
    Label(text='c)Audi S5 3.0T Quattro Coupe', fg="black",font=('courier', 20, 'bold')),
    Label(text='d)1962 Corvette Hardtop Restomod', fg="black",font=('courier', 20, 'bold')),
    Label(text='a)Devon GTX', fg="black",font=('courier', 20, 'bold')),
    Label(text='b)Alfa Romeo Zagato TZ3 Stradale', fg="black",font=('courier', 20, 'bold')),
    Label(text='c)Chrysler Firepower', fg="black",font=('courier', 20, 'bold')),
    Label(text='d)Dodge Challenger', fg="black",font=('courier', 20, 'bold')),
    Label(text='a)PositDodge Viper Hennessey Venom 1000 Twin Turbo', fg="black",font=('courier', 20, 'bold')),
    Label(text='b)Mazda MX-5 Miata Sport', fg="black",font=('courier', 20, 'bold')),
    Label(text='c)Mercedes-AMG C 63 2-Door Coupe', fg="black",font=('courier', 20, 'bold')),
    Label(text='d)Nissan GT-R 2-Door All-Wheel Drive Coupe', fg="black",font=('courier', 20, 'bold')),
    Label(text='a)Kellison J6', fg="black",font=('courier', 20, 'bold')),
    Label(text='b)Aston Martin DB11 Base V8 Coupe', fg="black",font=('courier', 20, 'bold')),
    Label(text='c)Kevin Harts 1959 Corvette', fg="black",font=('courier', 20, 'bold')),
    Label(text='d)Audi TT 2.0T 2dr AWD', fg="black",font=('courier', 20, 'bold')),
    Label(text='a)1964 Ford Mustang', fg="black",font=('courier', 20, 'bold')),
    Label(text='b)DeLorean DMC12 Restomod', fg="black",font=('courier', 20, 'bold')),
    Label(text='c)1970 Pontiac Firebird', fg="black",font=('courier', 20, 'bold')),
    Label(text='d)1970 Toyota Celica', fg="black",font=('courier', 20, 'bold')),
    Label(text='a)McLaren Elva: 804 HP', fg="black",font=('courier', 20, 'bold')),
    Label(text='b)SSC Tuatara: 1,750 HP', fg="black",font=('courier', 20, 'bold')),
    Label(text='c)Shelby Cobra V12', fg="black",font=('courier', 20, 'bold')),
    Label(text='d)Pagani Huayra Imola: 827 HP', fg="black",font=('courier', 20, 'bold')),
    Label(text='a)Dodge Viper Hennessey Venom 1000 Twin Turbo', fg="black",font=('courier', 20, 'bold')),
    Label(text='b)Ferrari 12Cilindri: 819 HP', fg="black",font=('courier', 20, 'bold')),
    Label(text='c)1974 Volkswagen Scirocco', fg="black",font=('courier', 20, 'bold')),
    Label(text='d)1976 Porsche 924', fg="black",font=('courier', 20, 'bold')),
    Label(text='a)Audi Q4 e-tron', fg="black",font=('courier', 20, 'bold')),
    Label(text='b)Chevrolet Bolt EUV', fg="black",font=('courier', 20, 'bold')),
    Label(text='c)Ford Mustang Mach 40', fg="black",font=('courier', 20, 'bold')),
    Label(text='d)Koenigsegg Agera: 947 HP', fg="black",font=('courier', 20, 'bold')),
    Label(text='a)1962 Chevrolet Corvette C1 RS Restomod', fg="black",font=('courier', 20, 'bold')),
    Label(text='b)1983 Pontiac Fiero', fg="black",font=('courier', 20, 'bold')),
    Label(text='c)C8 Chevrolet Corvette ZR1: 1,064 HP', fg="black",font=('courier', 20, 'bold')),
    Label(text='d)Hennessey Venom F5: 1,817 HP', fg="black",font=('courier', 20, 'bold'))
    )
ent=(Entry(fg="black", width=1, bg="white", relief='solid', font=('courier', 20, 'bold')),
    Entry(fg="black", width=1, bg="white", relief='solid', font=('courier', 20, 'bold')),
    Entry(fg="black", width=1, bg="white", relief='solid', font=('courier', 20, 'bold')),
    Entry(fg="black", width=1, bg="white", relief='solid', font=('courier', 20, 'bold')),
    Entry(fg="black", width=1, bg="white", relief='solid', font=('courier', 20, 'bold')),
    Entry(fg="black", width=1, bg="white", relief='solid', font=('courier', 20, 'bold')),
    Entry(fg="black", width=1, bg="white", relief='solid', font=('courier', 20, 'bold')),
    Entry(fg="black", width=1, bg="white", relief='solid', font=('courier', 20, 'bold')),
    Entry(fg="black", width=1, bg="white", relief='solid', font=('courier', 20, 'bold')),
    Entry(fg="black", width=1, bg="white", relief='solid', font=('courier', 20, 'bold'))
    )
a11=(Label(text='c)Ares Chevrolet Corvette Stingray', fg="black",font=('courier', 20, 'bold')),
    Label(text='1962 Corvette Hardtop Restomod', fg="black",font=('courier', 20, 'bold')),
    Label(text='Devon GTX', fg="black",font=('courier', 20, 'bold')),
    Label(text='PositDodge Viper Hennessey Venom 1000 Twin Turboion', fg="black",font=('courier', 20, 'bold')),
    Label(text='Kellison J6', fg="black",font=('courier', 20, 'bold')),
    Label(text='DeLorean DMC12 Restomod', fg="black",font=('courier', 20, 'bold')),
    Label(text='Shelby Cobra V12', fg="black",font=('courier', 20, 'bold')),
    Label(text='Dodge Viper Hennessey Venom 1000 Twin Turbo', fg="black",font=('courier', 20, 'bold')),
    Label(text='Ford Mustang Mach 40', fg="black",font=('courier', 20, 'bold')),
    Label(text='1962 Chevrolet Corvette C1 RS Restomod', fg="black",font=('courier', 20, 'bold'))
)
my_pic=(Image.open('C:\\Users\\yunus\\Desktop\\ynus\\solo\\1.jpg'),
    Image.open('C:\\Users\\yunus\\Desktop\\ynus\\solo\\2.jpg'),
    Image.open('C:\\Users\\yunus\\Desktop\\ynus\\solo\\3.jpg'),
    Image.open('C:\\Users\\yunus\\Desktop\\ynus\\solo\\4.jpg'),
    Image.open('C:\\Users\\yunus\\Desktop\\ynus\\solo\\5.jpg'),
    Image.open('C:\\Users\\yunus\\Desktop\\ynus\\solo\\6.jpg'),
    Image.open('C:\\Users\\yunus\\Desktop\\ynus\\solo\\7.jpg'),
    Image.open('C:\\Users\\yunus\\Desktop\\ynus\\solo\\8.jpg'),
    Image.open('C:\\Users\\yunus\\Desktop\\ynus\\solo\\9.jpg'),
    Image.open('C:\\Users\\yunus\\Desktop\\ynus\\solo\\10.jpg'),
    Image.open('C:\\Users\\yunus\\Desktop\\ynus\\solo\\m4.jpg'),
    Image.open('C:\\Users\\yunus\\Desktop\\ynus\\solo\\m2.jpg'),
    Image.open('C:\\Users\\yunus\\Desktop\\ynus\\solo\\m3.jpg'),
    Image.open('C:\\Users\\yunus\\Desktop\\ynus\\solo\\m1.jpg')
    )
my_pic1=Image.open('C:\\Users\\yunus\\Desktop\\ynus\\solo\\pp.jpg')

pic=(my_pic[0].resize((392,220)),
    my_pic[1].resize((392,220)),
    my_pic[2].resize((392,220)),
    my_pic[3].resize((392,220)),
    my_pic[4].resize((392,220)),
    my_pic[5].resize((392,220)),
    my_pic[6].resize((392,220)),
    my_pic[7].resize((392,220)),
    my_pic[8].resize((392,220)),
    my_pic[9].resize((392,220)),
    my_pic[10].resize((1370,900)),
    my_pic[11].resize((392,220)),
    my_pic[12].resize((290,220)),
    my_pic[13].resize((400,198))
    )
new_pic=(ImageTk.PhotoImage(pic[0]),
    ImageTk.PhotoImage(pic[1]),
    ImageTk.PhotoImage(pic[2]),
    ImageTk.PhotoImage(pic[3]),
    ImageTk.PhotoImage(pic[4]),
    ImageTk.PhotoImage(pic[5]),
    ImageTk.PhotoImage(pic[6]),
    ImageTk.PhotoImage(pic[7]),
    ImageTk.PhotoImage(pic[8]),
    ImageTk.PhotoImage(pic[9]),
    ImageTk.PhotoImage(pic[10]),
    ImageTk.PhotoImage(pic[11]),
    ImageTk.PhotoImage(pic[12]),
    ImageTk.PhotoImage(pic[13])
    )

my_label=(Label(win,image=new_pic[0]),
    Label(win,image=new_pic[1] ),
    Label(win,image=new_pic[2] ),
    Label(win,image=new_pic[3] ),
    Label(win,image=new_pic[4] ),
    Label(win,image=new_pic[5] ),
    Label(win,image=new_pic[6] ),
    Label(win,image=new_pic[7] ), 
    Label(win,image=new_pic[8] ),
    Label(win,image=new_pic[9] ),
    Label(win,image=new_pic[10] ),
    Label(win,image=new_pic[11] ),
    Label(win,image=new_pic[12] ),
    Label(win,image=new_pic[13] )
    )
def s():
    import tkinter as tk
    from tkinter import messagebox

    class TicTacToe:
        def __init__(self, root):
            self.root = root
            self.root.title("Tic Tac Toe")
            self.reset_game()

        def reset_game(self):
            self.board = [" " for _ in range(9)]
            self.current_player = "X"
            self.buttons = []
            
            for i in range(3):
                row = []
                for j in range(3):
                    button = tk.Button(self.root, text=" ", font=('normal', 40), width=5, height=2,
                                    command=lambda i=i, j=j: self.make_move(i, j))
                    button.grid(row=i, column=j)
                    row.append(button)
                self.buttons.append(row)

        def make_move(self, i, j):
            index = i * 3 + j
            if self.board[index] == " ":
                self.board[index] = self.current_player
                self.buttons[i][j].config(text=self.current_player)
                if self.check_winner():
                    messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                    self.reset_game()
                elif " " not in self.board:
                    messagebox.showinfo("Game Over", "It's a draw!")
                    self.reset_game()
                else:
                    self.current_player = "O" if self.current_player == "X" else "X"

        def check_winner(self):
            win_conditions = [
                [0, 1, 2], [3, 4, 5], [6, 7, 8],  # horizontal
                [0, 3, 6], [1, 4, 7], [2, 5, 8],  # vertical
                [0, 4, 8], [2, 4, 6]              # diagonal
            ]
            for condition in win_conditions:
                if self.board[condition[0]] == self.board[condition[1]] == self.board[condition[2]] != " ":
                    return True
            return False

    if __name__ == "__main__":
        root = tk.Tk()
        game = TicTacToe(root)
        root.mainloop()

m=(Button(text='M.C.Q of CARS',bg="blue", fg="yellow",activebackground='black',activeforeground='yellow', relief='solid', font=('courier', 30, 'bold'),command=nex1),
   Label(text='Computer Science Department ', bg="lime", fg="black",borderwidth=10,border=10,relief='raised',font=('courier', 40, 'bold')),
   Button(text='Choose your option',bg="black", fg="orange", activebackground='black',activeforeground='yellow',relief='solid', font=('courier', 20, 'bold')),
   Label(text='Welcome', bg="lime", fg="black",borderwidth=10,border=10,relief='sunken',font=('courier', 50, 'bold')),
   Button(text='Tic Tac Toe game',bg="blue", fg="yellow", activebackground='black',activeforeground='yellow',relief='solid', font=('courier', 20, 'bold'),command=s),
   Label(text='To', bg="lime", fg="black",borderwidth=30,border=15,relief='ridge',font=('courier', 50, 'bold')),
   )

main()
win.mainloop()

