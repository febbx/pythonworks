f1=open("C:\\Users\\HP\\Desktop\\python works\\datasets\\words.txt","r")
f2=open("C:\\Users\\HP\\Desktop\\python works\\datasets\\palindrome.txt","w")

for line in f1:

    word=line.rstrip("\n")

    reversed_words=word[::-1]

    if word==reversed_words:

        f2.write(word+"\n")

f1.close()

f2.close()