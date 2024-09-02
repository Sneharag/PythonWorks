
from json import load

f=open("D:\\PythonWorks\\jsonWorks\\countries.json",encoding="UTF-8")

countries=load(f)

#q1 total countries
#print(len(countries))

#q2 prints out the name and capital of each country
country={c.get("name"):c.get("capital") for c in countries}
# print(country)

#q3 highest populated country
max_population=max(countries,key=lambda c:c.get("population"))
# print(max_population.get("name"))

#q4 sorts a list of countries based on their population
country_sort=sorted(countries,key=lambda c:c.get("population"))
sort={c.get("name"):c.get("population") for c in country_sort}
# print(sort)

#q5 print countries in asia
asia_sort=[c.get("name") for c in countries if c.get("region")=="Asia"]
# print(asia_sort)

#q6 takes a country name and returns its region, capital, and population.
# name=input("Enter country name: ")
# for c in countries:
#     if name==c.get("name"):
#         capital=c.get("capital")
#         population=c.get("population")
#         region=c.get("region")
# print(f"{capital}\n {population}\n {region}")

#q7 filters countries with a population less than 1000
country_less=[c.get("name") for c in countries if c.get("population")<1000] 
# print(country_less)

#q8 print independent countries
independent=[c.get("name") for c in countries if c.get("independent")==True]
# print(independent)

#q9 reads a country and returns a list of countries that share a border with it
# name=input("enter country name: ")
# border=[c.get("borders") for c in countries if name==c.get("name")]
# print(border)

#q10  find countries with a population range(1000-3000).
population_range=[c.get("name") for c in countries if c.get("population")>1000 and c.get("population")<3000]
# print(population_range)

#q11 reads a country name and print currency names
# for c in countries:
#     if "currencies" in c:
#        block_data=c.get("currencies")[0]
#        if "name" in block_data:
#           name=block_data.get("name")
#           curr={c.get("name"):name}
#           print(curr)

#q12 reads a country name and prints its other names
# if "regionalBlocs" in country_data:
#     block_data=country_data.get("regionalBlocs")[0]
#     if "otherNames" in block_data:
#         others=block_data.get("otherNames")
#         print(others)
#     else:
#         print(country_data.get("name"))

#q13 biggest country area
def get_area(dic):
   
   if "area" in dic:
      
      return dic.get("area")
   else:
      return 0
biggest_country=max(countries,key=get_area)
# print(biggest_country.get("name"))

#q14 countries which has a language english
# for c in countries:
#    for l in c.get("languages"):
#       if l.get("name")=="English":
#          print(c.get("name"))

#q15 print all regions
all_regions={c.get("region") for c in countries}
# print(all_regions)

#q16 largest region by area
region_summary={}
for c in countries:
   region_name=c.get("region")
   if "area" in c:
       area=c.get("area")
       if region_name in region_summary:
           region_summary[region_name]+=c.get("area",0)
       else:
          region_summary[region_name]=c.get("area",0)

key_value=[(v,k) for k,v in region_summary.items()]
print(max(key_value))