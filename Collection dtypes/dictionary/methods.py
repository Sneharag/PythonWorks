#dictionary methods
# get(key),values(),keys(),items(),pop(key)

mobile={"name":"motoedge","brand":"moto","price":22000,"is_available":True}

# print(mobile.get("name"))  #if the key is invalid,it returns None
# print(mobile["name"])     

# all_keys=mobile.keys()   #return all keys in the dictionary
# print(all_keys)

# all_values=mobile.values()   #return all values in the dictionary
# print(all_values)

# mobile.pop("is_available")   #remove the specific element if it is present in dict
# print(mobile)

# for k,v in mobile.items():     #return the key,value pairs

#     print(k,v)

mobile["offer"]=500      #overwrites the value if the key is present else add as a new pair
print(mobile)

if "offer" in mobile:

    selling_price=mobile.get("price")-mobile.get("offer")
    print(selling_price)

else:

    selling_price=mobile.get("price")
    print(selling_price)
    