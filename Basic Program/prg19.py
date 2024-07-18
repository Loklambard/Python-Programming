import pickle as pk
def append():
    obj=open("book.dat","ab")
    bookno=input("Enter book number=")
    bookname=input("Enter book name=")
    pub=input("Enter name of the publications=")
    record=[bookno,bookname,pub]
    pk.dump(record,obj)
    obj.close()

def read():
    robj=open("book.dat","rb")
    try:
        while True:
            rec=pk.load(robj)
            print("Book no=",rec[0],"Book names=",rec[1],"Publications=",rec[2])
    except:
        print("Thank you")
    robj.close()

def delrec():
    robj=open("book.dat","rb")
    bno=input("Enter book no to delete=")
    flag=0
    lst=[]
    try:
        while True:
            rec=pk.load(robj)
            if rec[0]==bno:
                print(rec)
                print("Deleting this record")
                flag=1
            else:
                lst.append(rec)  #Appending those records which are to be used
    except:
        print("Thank you")
    robj.close()
    if flag==0:
        print("Record not found")
    else:#Writing all records to the file
        wobj=open("book.dat","wb")
        for a in lst:
            pk.dump(a,wobj)
        wobj.close()
        print("Updated files=")
        read()#Reading the contents of the file

def delbook():
    robj=open("book.dat","rb")
    bname=input("Enter book name to delete=")
    flag=0
    lst=[]
    try:
        while True:
            rec=pk.load(robj)
            if rec[1]==bname:
                print(rec)
                print("Deleting this record")
                flag=1
            else:
                lst.append(rec)  #Appending those records which are to be used
    except:
        print("Thank you")
    robj.close()
    if flag==0:
        print("Record not found")
    else:#Writing all records to the file
        wobj=open("book.dat","wb")
        for a in lst:
            pk.dump(a,wobj)
        wobj.close()
        print("Updated files=")
        read()#Reading the contents of the file

#Main program
while True:
   print("""1.Append a new record.
2.Read all the contents.
3.Delete only a record with book no given by user.
4.Delete a record with name given by the user.
5.Exit.""")
   choice=int(input("Enter the choice:"))
   if choice==1:
       append()
   if choice==2:
       read()     
   if choice==3:
       delrec()
   if choice==4:
       delbook()
   if choice==5:
       print("Exited")
       break    

    
        
        
