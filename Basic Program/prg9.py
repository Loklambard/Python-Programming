def append():
    obj=open("data2.txt","r")
    obj1=open("file1.txt","a")
    for a in obj:
        obj1.write(a)
    obj.close()
    obj1.close()
    print("Contents of file1.txt after appending=")
    nobj=open("file1.txt","r")
    d=nobj.read()
    print(d)
    nobj.close()

def it():
     obj=open("data2.txt","r")
     lines=obj.read()
     lines=lines.lower()
     words=lines.split()
     print("Frequency of 'it'is=",words.count("it"))
     obj.close()
    
def display():
    obj=open("data2.txt","r")
    lines=obj.readlines()
    for i in lines:
        if i[0]!='i':
            print(i)
    obj.close
    
def e():
    obj=open("data2.txt","r")
    c=0
    d=obj.read()
    w=d.split()
    for j in w:
        if j[-1]=="e":
            c+=1
            print(j)
    obj.close()
    print("Number of words ending with 'e'=",c)
    
#Main program
while True:
   print("""1.Append content of data2.txt to another file file1.txt,
and display contents of file1.txt after appending.
2.Count the frequency of word ‘it’ in file1.txt.
3. Display all lines of file1.txt barring the lines beginning with ‘i’.
4.Count and display all words ending with letter ‘e’.
5.Exit""")
   choice=int(input("Enter the choice:"))
   if choice==1:
       append()
   if choice==2:
       it()      
   if choice==3:
       display()
   if choice==4:
       e()
   if choice==5:
       print("Exited")
       break
    
    
