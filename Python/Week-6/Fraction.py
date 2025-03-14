import math

class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def _fcd(self, other):
        lcm = math.lcm(self.denominator, other.denominator)
        multiplier_self = lcm // self.denominator
        numerator1 = self.numerator * multiplier_self
        denominator1 = self.denominator * multiplier_self
        
        multiplier_other = lcm // other.denominator
        numerator2 = other.numerator * multiplier_other

        return numerator1, denominator1, numerator2

    def show(self):
        print(f"{self.numerator}/{self.denominator}")

    def add(self, other):
        print(f"{self.numerator}/{self.denominator} + {other.numerator}/{other.denominator} = ", end="")
        if self.denominator != 0 and other.denominator != 0:
            numerator1, denominator1, numerator2 = self._fcd(other)
            print(f"{numerator1 + numerator2}/{denominator1}")
        else:
            print("Cannot Divide by Zero")

    def subtract(self, other):
        print(f"{self.numerator}/{self.denominator} - {other.numerator}/{other.denominator} = ", end="")
        if self.denominator != 0 and other.denominator != 0:
            numerator1, denominator1, numerator2 = self._fcd(other)
            print(f"{numerator1 - numerator2}/{denominator1}")
        else:
            print("Cannot Divide by Zero")

    def multiply(self, other):
        if self.denominator != 0 and other.denominator != 0:
            print(f"{self.numerator}/{self.denominator} × {other.numerator}/{other.denominator} = {self.numerator * other.numerator}/{self.denominator * other.denominator}")
        else:
            print(f"{self.numerator}/{self.denominator} × {other.numerator}/{other.denominator} = Cannot Divide by Zero")

    def divide(self, other):
        if self.numerator != 0 and self.denominator != 0 and other.numerator != 0 and other.denominator != 0:
            print(f"{self.numerator}/{self.denominator} ÷ {other.numerator}/{other.denominator} = {self.numerator * other.denominator}/{self.denominator * other.numerator}")
        else:
            print(f"{self.numerator}/{self.denominator} ÷ {other.numerator}/{other.denominator} = Cannot Divide by Zero")


fraction1 = Fraction(1, 1)
fraction2 = Fraction(1, 1)

while True:
    try:
        print("Menu:\n1. Enter Fraction\n2. Show Fractions\n3. Add Fractions\n4. Subtract Fractions\n5. Multiply Fractions\n6. Divide Fractions")
        choice = input("Enter your choice: ")
        print("------------------------------")
        if choice == "1":
            print("Which Fraction to Change?\n1. First Fraction\n2. Second Fraction\n3. Close")
            fc = input("Enter your choice: ")
            if fc == "1":
                num = int(input("Enter a numerator: "))
                denom = int(input("Enter a denominator: "))
                fraction1 = Fraction(num, denom)
            elif fc == "2":
                num = int(input("Enter a numerator: "))
                denom = int(input("Enter a denominator: "))
                fraction2 = Fraction(num, denom)
            elif fc == "3":
                pass
            else:
                print("Invalid choice")
        elif choice == "2":
            print(f"First Fraction : ", end="")
            fraction1.show()
            print(f"Second Fraction : ", end="")
            fraction2.show()
        elif choice == "3":
            fraction1.add(fraction2)
        elif choice == "4":
            fraction1.subtract(fraction2)
        elif choice == "5":
            fraction1.multiply(fraction2)
        elif choice == "6":
            fraction1.divide(fraction2)
        else:
            print("Invalid choice")
        print("------------------------------")
    except:
        print("Invalid input")
