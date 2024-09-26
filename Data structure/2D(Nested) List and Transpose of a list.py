#Create 2d list
def myfun():
    lst=[[a for a in range (1,4)] for b in range(1,4)]
    return lst

#Traverse from 2d list
def myfun1(lst):
    for a in lst:
        for b in a:
            print(b,end=" ")
        print()

#Traversing with the help of indices
def myfun2(lst):
    p=len(lst)
    for a in range(p):
        t=len(lst[a])
        for b in range(t):
            print(lst[a][b],end=" ")
        print()    

#Transpose of a list
def myfun3(lst):
    p=len(lst)
    for a in range(p):
        t=len(lst[a])
        for b in range(t):
            print(lst[b][a],end=" ")
        print()
        
