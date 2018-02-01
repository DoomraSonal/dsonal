### Author: Sonal Doomra
### UMID: 88529245
### Purpose: 507 Waiver

### Part 2: Create a Simple Database application
import sys
import sqlite3

conn=sqlite3.connect("Northwind_small.sqlite")
conn_cursor=conn.cursor()

def main(argv):
    what_to_print = argv[1].lower() #for string comparison, not case sensitive
    

#print the list of all cusomters 
    if what_to_print == 'customer':
        conn_cursor.execute('SELECT Id,ContactName from Customer')
        print('ID \t Customer Name')
        for item in conn_cursor.fetchall():
            Id, Name = item
            print(Id+"\t"+Name)

#print the list of all employees
    elif what_to_print == 'employees':
        conn_cursor.execute('SELECT Id,FirstName,LastName from Employee')
        print('ID \t Employee Name')
        for item in conn_cursor.fetchall():
            Id, FirstName, LastName = item
            print(str(Id)+" \t "+FirstName+"  "+LastName)

#print the list of order dates for all orders placed for the specified customer. 
    if what_to_print == 'orders' :
        custId = argv[2].split('=')
        if custId[0] == 'cust':
            conn_cursor.execute("SELECT OrderDate from  [Order] where [Order].CustomerId='"+custId[1]+"'")
            print('Order Dates')
            for item in conn_cursor.fetchall():
                date = item[0]
                print(date)

#print the list of order dates for all orders managed by the specified employee    
    if what_to_print == 'orders' :
        
        empId = argv[2].split('=') 
        if empId[0] == 'emp':
            conn_cursor.execute("SELECT [Order].OrderDate,Employee.LastName from [Order] INNER JOIN Employee where [Order].EmployeeId = Employee.Id and Employee.LastName='"+empId[1]+"'")
            print('Order Dates')
            for item in conn_cursor.fetchall():
                date = item[0]
                print(date)

    conn.close()

if __name__ == '__main__':
    main(sys.argv)
