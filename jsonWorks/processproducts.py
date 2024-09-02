

from json import load

f=open("D:\\PythonWorks\\jsonWorks\\products.json",encoding="UTF-8")

products=load(f)

# print(len(products))

# products_title=[p.get("title") for p in products]
# print(products_title)

# jewelry_products=[p.get("title") for p in products if p.get("category")=="jewelery"]
# print(jewelry_products)

# products_100=[p.get("title") for p in products if p.get("price")>100]
# print(products_100)

# product_range=[p.get("title") for p in products if p.get("price")>=100 and p.get("price")<=150]
# print(product_range)

max_rating=max(products,key=lambda p:p.get("rating").get("count"))
print(max_rating.get("title"),max_rating.get("rating").get("count"))