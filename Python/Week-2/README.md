# Python Class ( Week 2 )
| In Python Week 2, I created projects on interesting topics.
---
* 1 . About a decision-making device.
```
favorite_movie = input("your favorite_movie is In theaters (True/False) :  ")
cheap_ticket = input("your favorite_movie is cheap ?? (True/False) : ")
free_time = input("do you have free time (True/False) : ")

if favorite_movie == "True" and cheap_ticket == "True" and free_time == "True":
    print("\nyou can go to see movie")
else:
    print("i am sorry you can't go to see movie ")
```
---
* 2 . In my second exercise, I created a password guessing game in which you have three chances to guess correctly.
```
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
```
---
* 3 . In my third project, I wrote a program that guides the person waiting behind the traffic light on what to do based on the light's color.
```
Traffic_Light = input("Enter The color of Traffic Light (red , yellow , green ) :")

if Traffic_Light == "red" :
    print("stop")
elif Traffic_Light == "yellow" :
    print("Ready to move")
elif Traffic_Light == "green" :
    print("Go")
else:
    print("please Choice ( red , yellow , green )")
```
---
* 4 . In the fourth and final project of the second week, I wrote a program that helps teachers organize the grades of the students in the class.
```
score = int(input("Enter your score (0 ta 100): "))

if score >= 90 :
    print("very good")
elif 90 > score >= 70 :
    print("good")
elif 70 > score >= 50 :
    print("Need to try harder")
else :
    print("you You didn't pass")
```

## Thanks to [Ilya Zangeneh](https://github.com/Eiliya-Zanganeh), my teacher in Python.

                               **The End**