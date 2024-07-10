import pickle as pk
def write():
    wobj=open("j15.dat","ab")
    while True:
        data=input("Enter the string=")
        pk.dump(data,wobj)
        print("""Press "1" if you wish to continue,press "2"  if you want to exit program""")
        ch=int(input("Enter a input="))
        if ch==1:
            continue
        else:
            print("Thank you")
            break
    wobj.close()

def read():
    robj=open("j15.dat","rb")
    try:
        while True:
            data=pk.load(robj)
            print(data)
    except:
        print("END OF FILE")
    robj.close()
    
