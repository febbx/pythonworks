
f=open("C:\\Users\\HP\\Desktop\\python works\\datasets\\names.txt","w")

languages = ["Python", "java", "c#", "javascript"]

for l in languages:

    f.write(l + "\n")

f.close()