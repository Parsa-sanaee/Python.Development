numbers = input("Enter a list of numbers separated by spaces: ").split()
numbers = [int(num) for num in numbers]

rotations = int(input("Enter the number of rotations: "))

rotations = rotations % len(numbers)

numbers.reverse()

first_part = numbers[:len(numbers) - rotations]
first_part.reverse()

second_part = numbers[len(numbers) - rotations:]
second_part.reverse()

rotated_list = first_part + second_part

print("Rotated list:", rotated_list)
