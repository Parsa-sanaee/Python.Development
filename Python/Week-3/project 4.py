grades = []

while True:
    grade = input("Please enter a grade (or type 'done' to finish): ")
    if grade.lower() == 'done':
        break
    elif grade.replace('.', '', 1).isdigit():  
        grades.append(float(grade))
    else:
        print("Invalid input. Please enter a valid number or type 'done' to finish.")

if grades:
    average = sum(grades) / len(grades)
    print(f"The average grade is: {average:.2f}")
else:
    print("No grades were entered.")
