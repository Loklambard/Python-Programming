import csv
f=open("stdata.csv","r")
d=csv.reader(f)
next(f)
s=0
for i in d:
     s=s + int(i[2])
print("Total Marks are " ,s)    
f.close( )
