"""WRITE A FUNCTION PUSH(ARR) , WHERE ARR IS A LIST OF NUMBERS.
FROM THIS LIST PUSH ALL NUMBERS DIVISIBLE BY 5
INTO A STACK IMPLEMENT BY USING A LIST.
DISPLAY THE STACK IF IT HAS AT LEAST ONE ELEMENT,
OTHERWISE DISPLAY APPROPRIATE MESSAGE"""
stack=[]
top=None
def push(Arr):
    global stack
    global top
    for x in Arr:
        if x%5==0:
            stack.append(x)
            top=len(stack)-1

def display():
    x=top
    if top==None:
        print("Stack is empty!")
    else:
        while x>=0:
            print(stack[x])
            x=-1
            
