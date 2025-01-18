password = "123456789"
attempts = 0

while attempts < 3:
    guess = input("guess The password: ")
    if guess == password:
        print("yes password is Right")
        break
    else:
        attempts += 1
        print(f"the pass is inCorrect {3 - attempts} you have ")

if attempts == 3:
    print("you are cant guess The password")
