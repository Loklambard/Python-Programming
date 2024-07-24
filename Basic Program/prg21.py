import csv as cv
def write():
    wobj=open("stdata.csv","a",newline="")
    writerobj=cv.writer(wobj)
    name=input("Enter name:")
    clas=int(input("Enter class:"))
    marks=float(input("Enter marks:"))
    record=[name,clas,marks]
    writerobj.writerow(record)
    wobj.close()
    
def count():
    robj=open("stdata.csv","r")
    read=cv.reader(robj)
    print(len(list(read)))
    return len(list(read))
    robj.close()
    
def search():
    robj=open("stdata.csv","r")
    read=cv.reader(robj)
    lstrec=list(read)
    print(lstrec)
    name=input("Enter name to be searched[first letter capital]:")
    for i in lstrec:
        if i[0]==name:
            print(i)
    robj.close()
    
#Main program
while True:
   print("""1.Write contents in a csv file.
2.To count all records in a file.
3.To search a given record.
4.Exit.""")
   choice=int(input("Enter the choice:"))
   if choice==1:
       write()
   if choice==2:
       count()
   if choice==3:
       search()
   if choice==4:
       print("Exited")
       break        

