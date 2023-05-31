import mysql.connector

mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='Pass@MySQL',
    port='3306',
    database='SEVENTHSEMATTN'
)

mycursor=mydb.cursor()

#name=[]


#name=mycursor.execute('SELECT student_details.Student_Name FROM student_details')

#for x in mycursor:
#    print(x)