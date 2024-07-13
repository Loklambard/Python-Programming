import pickle as pk 
def append(): 
    obj=open("student.dat","ab") 
    rno=int(input("Enter roll no=")) 
    name=input("Enter name=") 
    marks=float(input("Enter mark=")) 
    record=[rno,name,marks] 
    pk.dump(record,obj) 
    obj.close() 
  
def read(): 
    robj=open("student.dat","rb") 
    try: 
        while True: 
            rec=pk.load(robj) 
            print(rec) 
    except: 
        print("Thank u") 
    robj.close() 

def modname(): 
    robj=open("student.dat","rb") 
    listofrec=[] 
    flag=0 
    rno=int(input("Enter roll no whose name is to be modified=")) 
    try: 
        while True: 
            rec=pk.load(robj) 
            if rec[0]==rno: 
                newname=input("Enter new name=") 
                rec[1]=newname 
            listofrec.append(rec)
    except:
        print("Thank u") 
    robj.close() 
    wobj=open("student.dat","wb") 
    for a in listofrec: 
        pk.dump(a,wobj) 
    wobj.close() 
    print("Updated file=") 
    read()

def modmarks(): 
    robj=open("student.dat","rb") 
    listofrec=[] 
    flag=0 
    rno=int(input("Enter roll no whose marks is to be modified=")) 
    try: 
        while True: 
            rec=pk.load(robj) 
            if rec[0]==rno: 
                newmarks=float(input("Enter new marks=")) 
                rec[2]=newmarks 
            listofrec.append(rec) 
    except: 
        print("Thank u") 
    robj.close() 
    wobj=open("student.dat","wb") 
    for a in listofrec: 
        pk.dump(a,wobj) 
    wobj.close() 
    print("Updated file=") 
    read()

#Main program
while True:
   print("""1.Append record.
2.Read all therecords.
3.Modify name also display message if record not present.
4.Modify marks also display message if record not present.
5.Exit.""")
   choice=int(input("Enter the choice:"))
   if choice==1:
       append()
   if choice==2:
       read()     
   if choice==3:
       modname()
   if choice==4:
       modmarks()
   if choice==5:
       print("Exited")
       break    


            
