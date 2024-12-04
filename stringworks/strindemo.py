# class - blueprints or templates to create an object
# objects- real world entities

# class str = attributes and methods

# methods:
# capitalize
# casefold
# isalpha
# isdigit
# isalnum
# startswith(str)
# endswith(str)
#split
#strip- lstrip(),rstrip()
#slice
#index



# text="hellopython"
# print(text.capitalize())


# text="HELLopython "
# print(text.casefold())


# text="helloworld"
# print(text.isalpha())


# text="helloworld12"
# print(text.isalpha())


# text="1234"
# print(text.isdigit())


# text="1234hi"
# print(text.isdigit())


# text="123hello"
# print(text.isalnum())


# text="hellopython"
# print(text.startswith("He"))
# print(text.endswith("on"))


#to print each characters:
# text="hellopython"
# for ch in text:
#     print(ch)



#print vowels
# for ch in text:
#     if ch =="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u":
#         print(ch)
    

#split function-to split the string:
# text="hello,world,python"
# words=text.split(",")
# print(words)



#next
# text="\t this is \ta line\t" #remove\t
# new_text=text.strip("\t")
# print(new_text)


# text="\t this is \ta line\t" #remove\t
# new_text=text.rstrip("\t")
# print(new_text)


#next
# text="hello world program"
# new_text=text.replace("o","a",2)
# print(new_text)


#next
# text="python programming"
     #012345678901234567(indexing)
     #string_object[start:end:step]

# print(text[0:6]) #python
# print(text[7:18]) #programming
# print(text[::2]) #pto rgamn

# string="hello"
# reversed_text=string[::-1]
# print(reversed_text) #olleh



