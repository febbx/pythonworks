
f=open("C:\\Users\\HP\\Desktop\\python works\\qstns\\qst4.txt","r")

string=""

for i in f:

    string+=i

word=string.split("\n")

count=0

for l in word:

    count+=1

print(count)



