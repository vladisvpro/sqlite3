
import sqlite3

conn = sqlite3.connect('db.sqlite')
c = conn.cursor()

def adduser(name, surname, salary):
    c.execute("insert into users (name, surname, salary) values ('%s', '%s', '%s')" %(name, surname, salary)) 
    conn.commit()


n = int(input("Write a sum of money which dont take: "))
q = n-1;
a = n+1;

name = input("Enter user name: ")
surname = input("Enter user surname: ")
salary = int(input("Enter user salary: "))


if n < salary:
    print("Error, you cant increase")
             
else:
    print("All ok")

    
salary = int(input("Pls little less then you specified: "))

if n < salary:
    print("Enter LITTLE LESS")
             
else:
    print("All ok")


salary = input("Enter little less: ")

adduser(name, surname, salary)

print("User list: \n")
c.execute("select * from users")
ulist = c.fetchone()


while ulist is not None:
    print("id: "+str(ulist[0]) + " Name: "+str(ulist[1]) + " Surname: "+str(ulist[2]) + " Salary: "+str(ulist[3]))
    ulist = c.fetchone()


c.close()
conn.close()