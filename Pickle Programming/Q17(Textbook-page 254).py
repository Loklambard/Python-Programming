import pickle as pk
robj=open("company.dat","rb")
staff={}
flag=0
try:
    while True:
        st=pk.load(robj)
        for a in st:
            if st[a]=="1005":
                print(st)
                flag=1
except:
    if flag==0:
        print("No record found!")
    print("Thank you")    
            
