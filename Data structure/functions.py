#swaps first half of the list with second half
def fun1(mylist):
    p=len(mylist)
    newlist=mylist[p//2:p+1]+mylist[0:p//2]
    print(newlist)

# takes two lists as parameter and returns a list that contains elements which are common
#both the lists are of different sizes
def fun2(mylist1,mylist2):
    p=[]
    for a in mylist1:
        if a in mylist2:
            p.append(a)
    print("Elements in common:",p)
    
    

        
