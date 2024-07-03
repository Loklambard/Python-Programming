mydict={}
mydictnew={}
def Fun1():
    n=int(input("Enter total number of students="))
    global mydict
    for a in range(n):
        name=input("Enter name=")
        rno=int(input("Enter roll no.="))
        mydict[name]=rno
    return mydict

def Fun2():
    global mydictnew
    for a in mydict:
        x=(a,mydict[a])
        print("Enter cgpa of",a,"=")
        cgpa=float(input())
        mydictnew[x]=cgpa
    return mydictnew

def Fun3():
    name=input("Enter name=")
    flag=0
    for a in mydictnew:
        if a[0]==name:
            print("cgpa=",mydictnew[a])
            flag=1
    if flag==0:
        print("Record not found!")

def Fun4():#Display cgpa as per roll no. inputted by the user
    rno=int(input("Enter roll no.="))
    flag=0
    for a in mydictnew:
        if a[1]==rno:
            print("cgpa=",mydictnew[a])
            flag=1
    if flag==0:
            print("Record not found!")

def Fun5():#Descending order
    k=list(mydictnew.keys())
    k.sort(reverse=True)
    for a in k:
        print("Name=",a[0],"Roll no.=",a[1],"cgpa=",mydictnew[a])
