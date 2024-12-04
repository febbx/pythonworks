cars=[
    {"id":1,"name":"fronx","price":1200000,"brand":"nexa","colors":["red","blue","white"],"transmissions":["manuel","amt","cvt"]},
    {"id":2,"name":"baleno","price":1100000,"brand":"nexa","colors":["grey","blue","white"],"transmissions":["manuel","amt","cvt"]},
    {"id":3,"name":"3xo","price":900000,"brand":"mahindra","colors":["red","white","black"],"transmissions":["amt","cvt"]},
    {"id":4,"name":"punch","price":700000,"brand":"tata","colors":["red","blue","white","green"],"transmissions":["manuel","cvt"]},
    {"id":5,"name":"nexon","price":1400000,"brand":"tata","colors":["red","white"],"transmissions":["manuel","amt","cvt"]},
    {"id":6,"name":"kiger","price":1000000,"brand":"renault","colors":["blue","white"],"transmissions":["manuel","cvt"]},
    {"id":7,"name":"taigun","price":2300000,"brand":"volkswagon","colors":["red","blue","white"],"transmissions":["manuel","cvt"]},
 ]

# # print(f"total number of cars: {len(cars)}")

# available_colours_of_baleno=[m.get("colors") for m in cars if m.get("name")=="baleno"]
# print(available_colours_of_baleno)

# # print all brands
 
# brands=[m.get("brand") for m in cars]

 
# print(set(brands))

# # print carnames available in amt transmission
 


# car_names=[c.get("name") for c in cars if "amt" in c.get("transmissions")]

# print(car_names)

# # cars in blue color

 
# blue_car=[c.get("name") for c in cars if "blue" in c.get("colors")]

# print(blue_car)

# # print all transmissions



# transmissions=[t for c in cars for t in c.get("transmissions")]

# print(set(transmissions))


# # print all colors

# all_colors=[l for c in cars for l in c.get("colors")]

# print(set(all_colors))


# most popular color

costly_cars=max(cars,key=lambda c:c.get("price"))



costlyCar=costly_cars.get("price")

max_cost=[c.get("name") for c in cars if c.get("price")==costlyCar]

print(f"The highest priced car in the list:{max_cost}")

min_car=min(cars,key=lambda c:c.get("price"))

minCar=min_car.get("price")

MinCar=[c.get("name") for c in cars if c.get("price")==minCar]

print(f"The lowest priced car in thee list:{MinCar}")

car_sort=sorted(cars,key= lambda d:d.get("price"),reverse=True)

print(car_sort)

sorted_car_name={c.get("name"):c.get("price") for c in car_sort}

print(sorted_car_name)