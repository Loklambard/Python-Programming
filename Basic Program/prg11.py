def vowel():
    readobj=open("data1.txt","r")
    copyobj=open("data2.txt","a")
    data=readobj.read().split()
    for a in data:
        if a[0] in "AEIOUaeiou":
            copyobj.write(a+"\n")
    readobj.close()
    copyobj.close()
    






