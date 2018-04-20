from tkinter import *
pragya=Tk()
count=0
def addrec():
    f=open('opendb.txt','a')
    pid=s1.get()
    pname=s2.get()
    phn_no=s3.get()
    fees=s4.get()
    doc=s5.get()
    f.writelines(pid.ljust(20)+pname.ljust(10)+phn_no.ljust(30)+fees.ljust(15)+doc.ljust(15)+"\n")
    f.close()
def nextrec():
    global count
    print(count)
    f=open('opendb.txt','r')
    tr=len(f.readlines())
    tr=tr-1
    f.seek(0)
    i=0
    while(i<=count):
        l=f.readline()
        i=i+1
    l1=l.split()
    # print(l1[0],l1[1])	# If we want to print on console screen
    s1.set(l1[0])	
    s2.set(l1[1])
    s3.set(l1[2])
    s4.set(l1[3])
    s5.set(l1[4])
    if(count!=tr):
        count=count+1
    f.close()
def prev():
    f=open('opendb.txt','r')
    i=0
    global count
    while(i<=count):
        l=f.readline()
        i=i+1
    l1=l.split()
    # print(l1[0],l1[1])	# If we want to print on console screen
    s1.set(l1[0])	
    s2.set(l1[1])
    s3.set(l1[2])
    s4.set(l1[3])
    s5.set(l1[4])
    if (count!=0):
        count=count-1
    f.close()  
def update():
    pid=s1.get()
    pname=s2.get()
    phn_no=s3.get()
    fees=s4.get()
    doc=s5.get()
    f=open("opendb.txt","r")
    h=f.readlines()
    f.close()
    f=open("opendb.txt","w")
    flag=0
    for i in h:
        j=i.split()
        if(j[0]!=pid):
            f.writelines(j[0].ljust(20)+j[1].ljust(10)+j[2].ljust(30)+j[3].ljust(15)+j[4].ljust(15)+"\n")
        else :
            f.writelines(pid.ljust(20)+pname.ljust(10)+phn_no.ljust(30)+fees.ljust(15)+doc.ljust(15)+"\n")
            flag=1
    f.close()
def delete():
    k=[s1.get(), s2.get(), s3.get(), s4.get(), s5.get()]
    f=open("opendb.txt","r")
    h=f.readlines()
    f.close()
    f=open("opendb.txt","w")
    for i in h:
        j=i.split()
        if(j!=k):
            f.writelines(j[0].ljust(20)+j[1].ljust(10)+j[2].ljust(30)+j[3].ljust(15)+j[4].ljust(15)+"\n")
    f.close()
def search():
    k=s1.get()
    f=open("opendb.txt","r")
    h=f.readlines()
    for i in h:
        j=i.split()
        if(j[0]==k):
            print(k)
            s1.set(j[0])
            s2.set(j[1])
            s3.set(j[2])
            s4.set(j[3])
            s5.set(j[4])
    f.close()
def lr():
    f=open("opendb.txt",'r')       
    de=sum(1 for i in open("opendb.txt"))-1
    print(de)
    k=f.readlines()[de]
    j=k.split()
    s1.set(j[0])
    s2.set(j[1])
    s3.set(j[2])
    s4.set(j[3])
    s5.set(j[4])
    f.close()
def fr():
    global count
    count = 1
    f=open('opendb.txt','r')
    k=f.readlines()[0]
    j=k.split()
    print(j)
    s1.set(j[0])
    s2.set(j[1])
    s3.set(j[2])
    s4.set(j[3])
    s5.set(j[4])
    f.close()
s1=StringVar()
s2=StringVar()
s3=StringVar()
s4=StringVar()
s5=StringVar()
l0=Label(pragya,text="---------PRAGYA'S HOSPITAL--------")
l1=Label(pragya,text="PATIENT'S ID")
l2=Label(pragya,text="PATIENT'S NAME")
l3=Label(pragya,text="PHONE NO")
l4=Label(pragya,text="FEES")
l5=Label(pragya,text="CONSULTANT DOCTOR")
t1=Entry(pragya,textvariable=s1)
t2=Entry(pragya,textvariable=s2)
t3=Entry(pragya,textvariable=s3)
t4=Entry(pragya,textvariable=s4)
t5=Entry(pragya,textvariable=s5)
l0.grid(row=1,column=2)
l1.grid(row=2,column=1)
l2.grid(row=3,column=1)
l3.grid(row=4,column=1)
l4.grid(row=5,column=1)
l5.grid(row=6,column=1)
t1.grid(row=2,column=2)
t2.grid(row=3,column=2)
t3.grid(row=4,column=2)
t4.grid(row=5,column=2)
t5.grid(row=6,column=2)
b1=Button(pragya,text="Next", command=nextrec)
b2=Button(pragya,text="Insert", command=addrec)
b3=Button(pragya,text="Delete", command=delete)
b4=Button(pragya,text="Search", command=search)
b5=Button(pragya,text="Update", command=update)
b7=Button(pragya,text="Last Record", command=lr)
b6=Button(pragya,text="First Record", command=fr)
b8=Button(pragya,text="Previous", command=prev)
b1.grid(row=2,column=4)
b2.grid(row=4,column=4)
b3.grid(row=4,column=3)
b4.grid(row=5,column=4)
b5.grid(row=5,column=3)
b6.grid(row=7,column=1)
b7.grid(row=7,column=2)
b8.grid(row=2,column=3)
pragya.mainloop()
