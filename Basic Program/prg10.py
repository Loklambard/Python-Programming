def puretext():
    obj=open("mynotes.txt","r")
    d=obj.read()
    a=d.replace("k","c")
    obj.close()
    print("Original data:")
    print(d)
    print("Corrected data:")
    print(a)
    
    


