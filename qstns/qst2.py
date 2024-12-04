input=input("enter the string:")

f=open("C:\\Users\\HP\\Desktop\\python works\\qstns\\qst2.txt","a")

words=input.split(" ")

for i in words:

    f.write(i+"\n")

f.close()