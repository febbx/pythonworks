#create a dictionary product with keys id,title,price,brand
product={"id": 1001, "title": "perfume", "price": 325,"brand": "plum"}
print(product["title"])

#update product price as 330
product["price"]=330
print(product)

#update brand as wottagirl
product["brand"]="wottagirl"
print(product)

#add a field
product["use_by_date"]="10.06.2028"
print(product)

#add offer as 10 if offer exist else add offer as 20
if "offer" in product:
    product["offer"]=10

else:
    product["offer"]=20

print(product)