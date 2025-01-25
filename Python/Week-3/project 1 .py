Usere_number = input("Enter your list : ")

Usere_number = Usere_number.split()

evennum = []

for num in Usere_number:
    num = int(num)
    if num % 2 == 0:
        evennum.append(num)
    else:
        print(f"'{num}' is not a valid number and will be ignored.")
   

print("even number is : " , evennum)