lst = list(map(int, input("Please enter a list of numbers separated by spaces: ").split()))
n = int(input("Enter the number of rotations: "))

# Simple list slicing for rotation
result = lst[-n:] + lst[:-n]

print(result)
