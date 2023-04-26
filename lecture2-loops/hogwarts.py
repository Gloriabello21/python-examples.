#ejemplo1
students = ["Hermione", "Harry", "Ron"]

print(students[0])
print(students[1])
print(students[2])

#ejemplo2
students = ["Hermione", "Harry", "Ron"]

for student in students:
    print(student)

#ejemplo3
students = ["Hermione", "Harry", "Ron"]

for i in range(len(students)):
    print(students[i])

#ejemplo4
students = ["Hermione", "Harry", "Ron"]

for i in range(len(students)):
    print(i,students[i])

#ejemplo5
students = ["Hermione", "Harry", "Ron"]

for i in range(len(students)):
    print(i + 1, students[i])

#ejemplo6
students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}

print(students["Hermione"])
print(students["Harry"])
print(students["Rom"])
print(students["Dra2co"])

#ejemplo7
students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}

for student in students:
    print(student)

"""    
"""
#ejemplo8
students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}

for student in students:
    print(student, students[student], sep=",")

#ejemplo9

students = [
 {"name": "Hermione", "house": "Gryffindor","patronus": "otter"},
 {"name": "Harry", "house": "Gryffindor","patronus": "Stag"},
 {"name": "Ron", "house": "Gryffindor","patronus": "Jack Russell terrier"},
 {"name": "Draco", "house": "Gryffindor","patronus": "None"}
 ]

for student in students:
    print(student,["name"], student["house"])


#ejemplo10
students = [
 {"name": "Hermione", "house": "Gryffindor","patronus": "otter"},
 {"name": "Harry", "house": "Gryffindor","patronus": "Stag"},
 {"name": "Ron", "house": "Gryffindor","patronus": "Jack Russell terrier"},
 {"name": "Draco", "house": "Gryffindor","patronus": "None"}
 ]

for student in students:
    print(student,["name"], student["house"], student["patronus"], sep=",")






    






