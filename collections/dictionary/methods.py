#employee id,name,department,age,salary

employee={"id":100012, "name": "ayan","department":"it","age":24,"salary":25000,}

# print(employee.get("salary"))

# employee.pop("salary")
# print(employee)

#to return all keys:
    # for k in employee.keys():
    #     print(k)

#to return all values
    # for v in employee.values():
    #     print(v)

#to fetch keys and values
for k,v in employee.items():
    print(k,v)