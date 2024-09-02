
mobiles=[

    {"id":100,"title":"s23 ultra","brand":"samsung","price":125000,"network":"5g"},
    {"id":101,"title":"s23","brand":"samsung","price":54000,"network":"4g"},
    {"id":102,"title":"edge14pro","brand":"moto","price":25000,"network":"5g"},
    {"id":103,"title":"edgeneo","brand":"moto","price":22000,"network":"4g"},
    {"id":104,"title":"redminote13pro","brand":"mi","price":25000,"network":"5g"},
    {"id":105,"title":"redmi13","brand":"mi","price":12000,"network":"4g"},
]

#print all mobile names
mobile_names=[m.get("title") for m in mobiles]

# print(mobile_names)


#print all mobile brands
mobile_brands={m.get("brand") for m in mobiles}

# print(mobile_brands)


#print mobile names where brand=samsung
names=[m.get("title") for m in mobiles if m.get("brand")=="samsung"]

# print(names)


# print mobile names where price in range 23000-40000
rate=[m.get("title") for m in mobiles if m.get("price") in range(23000,40000)]

# print(rate)


# print mobile name of highest price

def get_price(mob):

    return mob.get("price")

costly_mob=max(mobiles,key=get_price)

#               or
# costly_mob=max(mobiles,key=lambda mob:mob.get("price"))
# print(costly_mob)

cheapest_mobile=min(mobiles,key=get_price)
# print(cheapest_mobile)

#sort the mobiles 

sorted_mobiles=sorted(mobiles,key=get_price,reverse=True)
# print(sorted_mobiles)

total_cost=sum([mob.get("price") for mob in mobiles])
# print(total_cost)