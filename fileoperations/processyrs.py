f1=open("C:\\Users\\HP\\Desktop\\python works\\datasets\\years.txt","r")
f2=open("C:\\Users\\HP\\Desktop\\python works\\datasets\\centryyrs.txt","w")
f3=open("C:\\Users\\HP\\Desktop\\python works\\datasets\\leapyear.txt","w")

def is_century_year(year):
    return True if year%100==0 else False

def is_leap_year(year):
    return True if year%100 ==0 and year%400==0 or year%100!=0 and year%4==0 else False

for year in f1:

    year=int(year)
    
    if year%100==0:

        f2.write(str(year)+"\n")

    if year%100 ==0 and year%400==0 or year%100!=0 and year%4==0:

        f3.write(str(year)+"\n")

f1.close()
f2.close()
f3.close()