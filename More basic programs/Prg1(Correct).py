mydict={}
stack=[]
top=None

#Push
def push():
    global top
    for a in mydict:
        if mydict[a]>49:
            stack.append(a)
    top=len(stack)-1
    
#Pop
def popelement():
    global top
    if stack==[]:
        print("Stack is empty!!")
    else:
        stack.pop()
        if stack==[]:
            top=None
        else:
            top=len(stack)-1

#Display
def display():
    if stack==[]:
        print("Stack is empty!!")
    else:
        print(top)
        a=top
        print("top",end="-->")
        while a>=0:
            print(stack[a],end="-->")
            a=a-1
            
#Create a dictionary
n=int(input("Enter how many records you want to enter="))
for a in range(n):
    name=input("Enter name=")
    runs=int(input("Enter runs="))
    mydict[name]=runs
print(mydict)

#Menu
while True:
    menu=int(input("1.Push\n2.Pop\n3.Display\n4.Exit"))
    if menu==1:
        push()
    elif menu==2:
        popelement()
    elif menu==3:
        display()
    else:
        break
