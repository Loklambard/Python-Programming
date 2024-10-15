stack=[]
top=None
n=eval(input("Enter list of numbers="))

#Push
def push():
    global top
    for a in n:
        if a%2!=0:
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
            print("Last element deleted")
        else:
            top=len(stack)-1

#Display
def display():
    if stack==[]:
        print("Stack is empty!!")
    else:
        a=top
        print("top",end="-->")
        while a>=0:
            print(stack[a],end="-->")
            a=a-1
            
#Menu
while True:
    menu=int(input("\n1.Push \n2.Pop \n3.Display \n4.Exit"))
    if menu==1:
        push()
    elif menu==2:
        popelement()
    elif menu==3:
        display()
    else:
        break

