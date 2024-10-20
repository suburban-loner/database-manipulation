# Importing the sqlite3 modules.
import sqlite3

# This is creating a database called programming_db and a cursor to interact with the database.
db = sqlite3.connect('student_db')
cursor = db.cursor()

# This is creating a table called python_programming with three columns: id, name, and grade.
cursor.execute('''create table if not exists python_programming(id INTEGER PRIMARY KEY, name TEXT, grade INTEGER)''')
db.commit()

# This is inserting multiple rows into the table.
students = [(55, "Carl Davis", 61), (66, "Dennis Fredrickson", 88), (77, "Jane Richards", 78), (12, "Peyton Sawyer", 45), (2, "Lucas Brooke", 99)]
cursor.executemany('''insert into python_programming(id, name, grade) values(?,?,?)''', students)
db.commit()

num = 60
num2 = 80
# This is selecting all the rows from the table python_programming where the grade is between 60 and 80 and assigning
# them to the variable students2.
cursor.execute('''select id, name, grade from python_programming where grade between ? and ?''', (num, num2))
students1 = cursor.fetchall()
db.commit()
# Printing the variable students2.
print(students1)

stu_name1 = "Carl Davis"
new_grade = 65
# This is updating the grade of Carl Davis to 65.
cursor.execute('''update python_programming set grade = ? where name = ?''', (new_grade, stu_name1))
db.commit()
print("Carl Davis' grade has been changed to 65.")

stu_name2 = "Dennis Fredrickson"
# Deleting the row where the name is Dennis Fredrickson.
cursor.execute('''delete from python_programming where name = ?''', (stu_name2,))
db.commit()
print("The row for Dennis Fredrickson has been deleted.")

new_grade2 = 80
stu_id = 55
# Updating the grade of all the students with an id less than 55 to 80.
cursor.execute('''update python_programming set grade = ? where id < ?''', (new_grade2, stu_id))
db.commit()
print("Changed the grade for all students with an id below 55 to 80.")

# Closing the database.
db.close()
print("Closed the database")
