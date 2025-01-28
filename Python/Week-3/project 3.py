# دریافت ورودی کاربر و تبدیل آن به لیست
input_string = input("plese Enter The number ")
input_list = [int(item) for item in input_string.split()]

unique_list = []
for item in input_list:
    if item not in unique_list:
        unique_list.append(item)

print("The final list : ", unique_list)
