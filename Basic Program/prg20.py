import csv as cv
#Write contents in a csv file
def write():
    aobj=open("stdata.csv","a",newline="")
    name=input("Enter name=")
    Class=input("Enter class=")
    marks=float(input("Enter marks="))
    record=[name,Class,marks]#Creating the record
    wobj=cv.writer(aobj)#Creating a writer object
    wobj.writerow(record)#Writing single record in the file
    aobj.close()

#Read all contents of csv file in the form of list
def read():
    robj=open("stdata.csv","r")
    record=cv.reader(robj)#Creating the reader object
    #Printing the records
    for a in record:
        print(a)
    robj.close()

#Display alll contents of the csv file in the form of comma separated values
def sep():
    robj=open("stdata.csv","r")
    record=cv.reader(robj)#Creating the reader object
    #Printing the records
    print("Comma seperated values")
    for a in record:
        print(a[0],a[1],a[2],sep=",")
    robj.close()

#Main program
while True:
   print("""1.Write contents in a csv file
2.Read all the contents of csv file in form of list.
3.Display all contents of the csv file in the form of comma seperated values.
4.Exit.""")
   choice=int(input("Enter the choice:"))
   if choice==1:
       write()
   if choice==2:
       read()     
   if choice==3:
       sep()
   if choice==4:
       print("Exited")
       break        



