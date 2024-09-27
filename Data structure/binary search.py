def Bsearch(LIST,n,item):
    LB=0
    UB=n-1
    while LB<=UB:
        mid=int((LB+UB)/2)
        if item<LIST[mid]:
            UB=mid-1
        elif item>LIST[mid]:
            LB=mid+1
        else:
            return mid
    else:
        return-1
L=eval(input("Enter the elements in sorted order:"))
size=len(L)
element=int(input("Enter the element that your want to search:"))
found=Bsearch(L,size,element)
if found>=0:
    print(element,"Found at the position:",found+1)
else:
    print("Element not present in the list")
    
