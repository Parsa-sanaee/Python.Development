input_count = int(input("please Enter the number of scores : "))

li = []

for i in range(1, input_count + 1):
    while True:
            user_score = float(input(f"Enter the score number {i}: "))
            if user_score >= 0 and user_score <= 20:
                li.append(user_score)
                break
            else:
                print("score should be between 0 to 20...")
Avg = 0

for x in li:
    Avg += x

Avg = Avg / len(li)

print(f"The average of the scores is: {Avg}")