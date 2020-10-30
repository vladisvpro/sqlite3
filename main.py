
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

while n < salary:
    print("")
    print("")
    print("")

    if n > salary:
        print("This is first check--------All ok")
    
    else:
        print("Oh....Sry you have Error-----you cant increase")
        

        
    salary = int(input("Enter little less: "))



    if n >= salary:
        print("This is second check-------All ok")

    else:
        print("Pls enter", " ", salary)

        break

salary = input("Enter previous number or enter some number which was less previous for salary: ")

adduser(name, surname, salary)

print("User list: \n")
c.execute("select * from users")
ulist = c.fetchone()


while ulist is not None:
    print("id: "+str(ulist[0]) + " Name: "+str(ulist[1]) + " Surname: "+str(ulist[2]) + " Salary: "+str(ulist[3]))
    ulist = c.fetchone()


c.close()
conn.close()