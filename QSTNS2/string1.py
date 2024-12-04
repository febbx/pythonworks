text = "On June 5th, 2024, we will celebrate @ our annual event: 'Tech Innovations 2024!'"

alphabet_count = 0
space_count = 0
special_count = 0
number_count = 0

for char in text:
    if char.isalpha():         
        alphabet_count += 1
    elif char.isspace():       
        space_count += 1
    elif char.isdigit():       
        number_count += 1
    else:                     
        special_count += 1

print("Alphabets:", alphabet_count)
print("Spaces:", space_count)
print("Special Characters:", special_count)
print("Numbers:", number_count)