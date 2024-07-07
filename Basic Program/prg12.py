def mini():
    obj=open("data1.txt","r")
    d=obj.read()
    wlst=d.split()
    clst=[]
    for a in wlst:
        i=wlst.count(a)
        clst.append(i)
    mc=min(clst)
    for a in wlst:
        i=wlst.count(a)
        if i==mc:
            print(a,mc,sep=":")
    obj.close()        
        
