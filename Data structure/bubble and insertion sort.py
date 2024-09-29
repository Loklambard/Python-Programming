#Bubble Sort
def bubble():
    lst=eval(input("Enter list="))
    p=len(lst)
    for x in range(p-1):
        for y in range(p-x-1):
            if lst[y]>lst[y+1]:
                lst[y],lst[y+1]=lst[y+1],lst[y]
        print(lst)

#Insertion sort
def insertsort():
    lst=eval(input("Enter the list="))
    for x in range(1,len(lst)):
        temp=lst[x]
        p=x-1
        while p>=0 and temp<lst[p]:
            lst[p+1]=lst[p]
            p=p-1
        else:
            lst[p+1]=temp
        print(lst)
        
            
        
