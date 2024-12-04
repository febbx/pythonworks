#lambda fnction:used to consize the normal function.

#lambda function for adding 2 nums.
add=lambda n1,n2:n1+n2
print(add(10,2))

#lambda function to subtract a num.
sub=lambda n1,n2:n1-n2
print(sub(30,20))

#lambda function to fine cube of a num.
cube=lambda n1:n1**3
print(cube(9))

#max of two strings
max_two=lambda str1,str2:str1 if len(str1) > len(str2) else str2
print(max_two("good","morning"))

#min of two strings
min_two=lambda str1,str2:str1 if len(str1) < len(str2) else str2
print(min_two("good","morning"))

#smart sub
smart_sub=lambda num1,num2:num1-num2 if num1>num2 else num2-num1
print(smart_sub(500,900))

