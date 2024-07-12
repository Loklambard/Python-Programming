import pickle as pk
def append():
    obj=open("emp.dat","ab")
    empno=input("Enter employeeno=")
    ename=input("Enter name=")
    age=int(input("Enter age="))
    salary=float(input("Enter salary="))
    record=[empno,ename,age,salary]
    pk.dump(record,obj)
    obj.close()
    
def read():
    robj=open("emp.dat","rb")
    try:
        while True:
            rec=pk.load(robj)
            print(rec)
    except:
        print("Thank you")
    robj.close()

def display():
    x=int(input("Enter value of age="))
    robj=open("emp.dat","rb")
    flag=0
    try:
        while True:
            rec=pk.load(robj)
            if rec[2]>=x:
                print(rec)
                flag=1
    except:
        if flag==0:
            print("No relevant records!")
            print("Thank you")
    robj.close()

#Main program
while True:
   print("""1.Append a new record
2.Read all the contents
3.Display only those records whose age is more than x
4.Exit""")
   choice=int(input("Enter the choice:"))
   if choice==1:
       append()
   if choice==2:
       read()     
   if choice==3:
       display()
   if choice==4:
       print("Exited")
       break    
