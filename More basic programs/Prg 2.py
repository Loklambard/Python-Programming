stack=[]
top=None
n=int(input("Enter the capacity of stack="))

def push():
    global stack
    global top
    if top==n-1:
        print("Stack is ful!")
    else:
        bookno=int(input("Enter book no.="))
        bookname=input("Enter book name=")
        t=(bookno,bookname)
        stack.append(t)
        top=len(stack)-1

def pop():
    global top
    global stack
    if top==None:
        print("Stack is empty!")
    else:
        stack,pop()
        if top==0:
            top=None
        else:
            top=len(stack)-1

def peek():
    print("Element at the top=",stack[top])

def display():
    if top==None:
        print("Stack is empty!")
    else:
        x=top
        print("Top-->",end=" ")
        while(x>=0):
            print(stack[x],end=" ")
            x-=1
            
            
        
