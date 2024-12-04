#create a dictionary employee with keys eid,name,salary,department,exp

employee={"eid":100012, "name": "ayan","salary":25000,"department":"it","exp":2}
print(employee)

#add contact
employee["contact"]=1234567
print(employee)

#if exp>5 update employee salary as current salary+10000 else current salary+5000
if employee["exp"]>5:

    employee["salary"]+=10000

else:
    employee["salary"]+=5000

print(employee)

#add role as SDE if exp>5 else add role as JDE
if employee["exp"]>5:
    employee["role"]="SDE"
else:
    employee["role"]="JDE"
print(employee)