
from json import load

f=open("C:\\Users\\HP\\Desktop\\python works\\datasets\\countries.json",encoding="utf-8")

data=load(f)

# print(len(data)) #print no of countries.

all_country_names=[country.get("name") for country in data]
# print(all_country_names)

all_regions=[country.get("region") for country in data]
# print(set(all_regions))

region_count={region:all_regions.count(region) for region in all_regions}
# print(region_count)

max_region_count=max(region_count,key=lambda k:region_count.get(k))
# print(max_region_count,region_count.get(max_region_count))

capital_of_a_country=[country.get("capital") for country in data if country.get("name")=="India"]
# print(capital_of_a_country)

country_border_count={country.get("name"):len(country.get("borders",[0])) for country in data}
# print(country_border_count)

max_border_country=max(data,key=lambda country:len(country.get("borders",[]))).get("name")
# print(max_border_country)

# most_populated_cntry=max(data,key=lambda country:country.get("population").get("name"))
# print(most_populated_cntry)

alpha3code=[country.get("borders") for country in data if country.get("name")=="India"][0]

for code in alpha3code:

    for country in data:

        if country.get("alpha3Code")==code:

            print(country.get("name"))

