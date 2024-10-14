#Write functions to work on a linear list that contains data of
#Students in form of dictionaries(list of dictionaries)
def list():
    lst=[]
    n=int(input("Enter how many records to be entered="))
    for a in range(n):
        d={}
        rno=int(input("Enter roll no.="))
        name=input("Enter name=")
        d[rno]=name
        lst.append(d)
    return(lst)

def position():
    pos=int(input("Enter position="))
    ele={}
    rno=int(input("Enter roll no.="))
    name=input("Enter name=")
    ele[rno]=name
    mylist.insert(pos,ele)
    return(mylist)

def bubble():#Sort as per name using bubble sort
    for i in range(len(mylist)):                  
        for j in range(len(mylist)-i-1):
            p=list=(mylist[j].values())
            q=list(mylist[j+1].values())
            print(p,q)
            if p[0]>q[0]:
                   mylist[j],mylist[j+1]=mylist[j+1],mylist[j]
        print(mylist)
    return(mylist)

def insertion():#Sort as per roll no.s using insertion sort
    print("Before")
    print(mylist)
    print("After sort")
    n=len(mylist)
    for j in range(1,n):
        temp=mylist[j]
        pos=j-1
        while pos>=0 and list(temp.keys())[0]<list(mylist[pos].keys())[0]:
            mylist[pos+1]=mylist[pos]
            pos=pos-1
        else:
            mylist[pos+1]=temp
        print(mylist)

def insertsort():#Insertion in sorted list
    print(mylist)
    print("Input record to insert")
    d={}
    rno=int(input("Enter roll no.="))
    name=input("Enter name=")
    d[rno]=name
    mylist.append(d)
    bubble()
    print(mylist)

def delete():#Delete a record
    rno=int(input("Enter roll no. to delete="))
    flag=0
    p=0
    for a in mylist:
        if rno in a:
            flag=1
            t=a            
            break
    if flag==0:
        print("Record not found!")
    else:
        mylist.remove(t)
        display()
            
def display():#Display all records
    for a in mylist:
        print(a,end=",")

def lsearch():#Linear search
    ch=int(input("""Enter 1 to search as per roll no. ,2 to search as per name"""))
    flag=0
    if ch==1:
        rno=int(input("Enter roll no.="))
        for a in mylist:
            flag=1
            print("Record found",a)
    elif ch==2:
        name=input("Enter name=")
        for a in mylist:
            for x in a:
                if a[x]==name:
                    flag=1
                    print("Record found",a)
    else:
        print("Invalid choice")
    if flag==0:
        print("Record not found!")

def bsearch():#Binary Search
    bg=0
    end=len(mylist)-1
    x={}
    a=int(input("Enter roll no. to search="))
    while bg<=end:
        mid=(bg+end)//2
        #Check if a is present at mid
        if list(mylist[mid].keys())[0]==a:
            return mid,mylist[mid]
        #If a is greater,ignore left half
        elif list(mylist[mid].keys())[0]<a:
            bg=mid+1
        #If a is smaller,ignore right half
        else:
            end=mid-1
    #If we reach here,then the element wasn't present
    print("Out of loop")
    return 'p'
result=bsearch()
if result=='p':
    print("Element is not present in list")
else:
    print("Element is present at index",result)
        
    
            
          
                   
                   
    
