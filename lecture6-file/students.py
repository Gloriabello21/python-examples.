#ejemplo1
with open("students.csv") as file:
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]} is in {row[1]}")
        
#ejemplo2
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")
        
#ejemplo3
students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append(f"{name} is in {house}")

for student in sorted(students):
    print(student)

#ejemplo4
students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)

def get_name(student):
    return student["name"]


for student in sorted(students, key=get_name):
    print(f"{student['name']} is in {student['house']}")

#ejemplo5
students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)

def get_name(student):
    return student["name"]


for student in sorted(students, key=get_name, reverse=True):
    print(f"{student['name']} is in {student['house']}")

#ejemplo6primero imprime slythering y luego los gryffindor
students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)

def get_house(student):
    return student["house"]


for student in sorted(students, key=get_house, reverse=True):
    print(f"{student['name']} is in {student['house']}")

#ejemplo7primero imprime gryffindor y luego slythering
students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)

def get_house(student):
    return student["house"]


for student in sorted(students, key=get_house):
    print(f"{student['name']} is in {student['house']}")

#ejemplo8 
students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['house']}")

#ejemplo9
import csv

students = []

with open("students.csv") as file:
    reader = csv.reader(file)
    for name, home in reader:
        students.append({"name": name, "home": home})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")

#ejemplo10
import csv

students = []

with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")
    
#11 lo que hace es que guarda los datos que pones en la terminal y los guarda en students.csv
import csv  

name = input("what's your name? ") 
home = input("what's your home? ")

with open ("students.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, home])

#ejemplo12
import csv  

name = input("what's your name? ") 
home = input("what's your home? ")

with open ("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})
