from json import load

f=open("C:\\Users\\HP\\Desktop\\python works\\datasets\\employee.json", "r")

data=load(f)

for emp in data:

    print(emp)