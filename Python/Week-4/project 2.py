students_name = [
    {"name": "mamad", "family": "Rezaei", "class_number": 301},
    {"name": "mohsen", "family": "Karimi", "class_number": 301},
    {"name": "Hossein", "family": "Rostami", "class_number": 303},
]


def findStudent():
    found = False
    user_search = input("Enter the name of student: ")
    for i in students:
        if i["name"] == user_search:
            found = True
            print("student found!")
            print("info:")
            print(f"name: {i['name']}")
            print(f"family: {i['family']}")
            print(f"class number: {i['class_number']}")
            break
        else:
                found = False
        if found == False:
            print("student not found...")

findStudent()