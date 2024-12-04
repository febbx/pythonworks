# syntax=[return iteration condition]

arr=[2,3,4,5,6,7]
# squares=[num**2 for num in arr]
# print(squares)


# add_ten=[num+10 for num in arr]
# print(add_ten)

odd_numbers=[num for num in arr if num%2!=0]
print(odd_numbers)

even_numbers=[num for num in arr if num%2==0]
print(even_numbers)

number_gt_five=[num for num in arr if num<5]
print(number_gt_five)

text=["apple","iphone","orange","potato"]
