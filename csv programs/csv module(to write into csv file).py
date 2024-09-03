import csv as cv 
#write a record  
def myfun1(): 
          aobj=open("data.csv","a",newline="") 
          writerobj=cv.writer(aobj) 
          rno=int(input("Enter rollno=")) 
          name=input("Enter name=") 
          rec=[rno,name] 
          writerobj.writerow(rec) 
          aobj.close()        

def myfun2(): 
          aobj=open("data.csv","a",newline='') 
          writerobj=cv.writer(aobj) 
          listofrec=[] 
          while True: 
                    rno=int(input("Enter rollno="))
                    name=input("Enter name=") 
                    rec=[rno,name] 
                    listofrec.append(rec)                    
                    ch=int(input("Enter 1 to input more=")) 
                    if ch!=1: 
                              break 
          writerobj.writerows(listofrec) 
          aobj.close()

def myfun3():# to read 
          robj=open("data.csv","r") 
          data=cv.reader(robj) 
          cnt=0 
          for a in data: 
                    cnt+=1 
                    print(a) 
          print(cnt) 



          
