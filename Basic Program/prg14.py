def separate():
    readobj=open("data3.txt","r")
    copyobj=open("separatefile.txt","w")   
    lst=[]
    for x in readobj:
        print(x)
        if "a" in x:
            copyobj.write(x)
        else:
            lst.append(x)
    readobj.close()
    copyobj.close()
    obj=open("data3.txt","w")
    obj.writelines(lst)
    obj.close()
    
