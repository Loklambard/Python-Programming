#importing sqlconnector 
import mysql.connector as con 
#establishing the connection 
mydb=con.connect(host="localhost",user="root",password="",database="csmysql") 
#creating cursor object 
mycur=mydb.cursor()

#a.To show all information about the teacher of History department. 
print("To show all information about the teacher of History department.") 
st="select * from teacher where department='history'" 
mycur.execute(st) 
for a in mycur: 
    print(a)
    
#b.To list the name of female teachers who are in History department. 
print("To list the name of female teachers who are in History department.") 
st="select name from teacher where department='history' and sex='F'" 
mycur.execute(st) 
for a in mycur: 
    print(a) 

#c.To list the names of all the teachers with their date of joining in ascending  order. 
st="select name from teacher order by dateofjoin" 
print("To list the names of all the teachers with their date of joining in ascending  order.") 
mycur.execute(st) 
for a in mycur: 
    print(a) 

#d.To display Teachers Name, Salary, Age for male teachers only. 
print("To display Teachers Name, Salary, Age for male teachers only.") 
st="select name,salary,age from teacher where sex='M'" 
mycur.execute(st) 
for a in mycur: 
    print(a)
    
#e.To count the number of teachers with age > 23. 
print("To count the number of teachers with age > 23.") 
st="select count(*) from teacher where age>23" 
mycur.execute(st) 
for a in mycur: 
    print(a) 

#f.To insert a new row in the Teacher table with the following data.   
    #  9, “Raja”, 26, “Computer”, {13/05/95}, 2300, "M" 
print("To insert a new row in the Teacher table with the following data. ") 
st="insert into teacher values({},'{}',{},'{}','{}',{},'{}')".format(9,'RAJA',26,'COMPUTER','1995-05-13',2300,'M') 
mycur.execute(st) 
mydb.commit() 
st="select * from teacher" 
mycur.execute(st) 
for a in mycur: 
    print(a) 

#g.To display total count of teachers department wise 
print("To display total count of teachers department wise") 
st="select department, count(*) from teacher group by department" 
mycur.execute(st) 
for a in mycur: 
    print(a) 

#h.To display age of eldest female employee. 
print("To display age of eldest female employee.") 
st="select min(age) from teacher where sex='F'" 
mycur.execute(st) 
for a in mycur: 
    print(a) 

#i.To display average salary of all male teachers 
print("To display average salary of all male teachers") 
st="select avg(salary) from teacher where sex='M'" 
mycur.execute(st) 
for a in mycur: 
    print(a) 

#j. To display total salary of all teachers who joined before 12-07-1996  
print("To display total salary of all teachers who joined before 12-07-1996") 
st="select sum(salary) from teacher where dateofjoin<'1996-07-12'" 
mycur.execute(st) 
for a in mycur: 
    print(a) 

  
