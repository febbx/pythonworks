input=input("enter the string:")

f=open("C:\\Users\\HP\\Desktop\\python works\\qstns\\qst1.txt","w")

for i in input:

    f.write(i)

f.close()

f1=open("C:\\Users\\HP\\Desktop\\python works\\qstns\\qst1.txt","r")

for word in f1:

    print(word)

f1.close()