def sep():
    obj=open("data1.txt","r")
    d=obj.read()
    print("Original file:")
    print(d)
    n=d.replace(" ","#")
    print("Corrected file:",n)
    obj.close()
             
