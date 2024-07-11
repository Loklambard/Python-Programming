import pickle as pk
def append():
    aobj=open("phonedir.dat","ab")
    d={}
    name=input("Enter name=")
    no=input("Enter phone no.=")
    d[name]=no
    #write in the file
    pk.dump(d,aobj)
    aobj.close()

def read():
    robj=open("phonedir.dat","rb")
    try:
        while True:
            data=pk.load(robj)
            print(data)
    except:
        print("Thank you")
    robj.close()

def searchname():
    robj=open("phonedir.dat","rb")
    n=input("Enter name to search=")
    flag=0
    try:
        while True:
            data=pk.load(robj)
            if n in data:
                    print(data)
                    flag=1
    except:
        if flag==0:
            print("Record not found!")
        print("Thank you")
    robj.close()
    
def searchno():
    robj=open("phonedir.dat","rb")
    n=input("Enter no. to search=")
    flag=0
    try:
        while True:
            data=pk.load(robj)
            for a in data:
                if n==data[a]:
                    print(data)
                    flag=1
    except:
        if flag==0:
            print("Record not found!")
        print("Thank you")
    robj.close()

    
#Main program
while True:
   print("""1.Append new record in the form name and phone no
2.Read all the records
3.Search by name and print the record
4.Search by phone no and print the record
5.Exit""")
   choice=int(input("Enter the choice:"))
   if choice==1:
       append()
   if choice==2:
       read()     
   if choice==3:
       searchname()
   if choice==4:
       searchno()
   if choice==5:
       print("Exited")
       break    
