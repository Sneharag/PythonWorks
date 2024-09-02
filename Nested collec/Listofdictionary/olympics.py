
olympics= [
    {"country": "United States", "gold": 39, "silver": 41, "bronze": 33},
    {"country": "China", "gold": 38, "silver": 32, "bronze": 18},
    {"country": "Japan", "gold": 27, "silver": 14, "bronze": 17},
    {"country": "Great Britain", "gold": 22, "silver": 21, "bronze": 22},
    {"country": "Russia", "gold": 20, "silver": 28, "bronze": 23},
    {"country": "Australia", "gold": 17, "silver": 7, "bronze": 22},
    {"country": "Netherlands", "gold": 10, "silver": 12, "bronze": 14},
    {"country": "France", "gold": 10, "silver": 12, "bronze": 11},
    {"country": "Germany", "gold": 10, "silver": 11, "bronze": 16},
    {"country": "Italy", "gold": 10, "silver": 10, "bronze": 20}
]

#q1 country with most no. of gold medals
gold_max=max(olympics,key=lambda m:m.get("gold"))
# print(gold_max.get("country"))

#q2 medal count of each countries
medal_count={o.get("country"):o.get("gold")+o.get("silver")+o.get("bronze") for o in olympics}
# print(medal_count)

#q3 country with least no. of medals
medal_min=min(olympics,key=lambda o:o.get("gold")+o.get("silver")+o.get("bronze"))
# print(medal_min.get("country"))

#q4 sort countries with medal count
medal_sort=sorted(olympics,key=lambda o:o.get("gold")+o.get("silver")+o.get("bronze"))
sorted_medal=[o.get("country") for o in medal_sort]
# print(sorted_medal)

#q5 country with most no. of medals
medal_max=max(olympics,key=lambda o:o.get("gold")+o.get("silver")+o.get("bronze"))
# print(medal_max.get("country"))

#q6 average number of gold medals won by the countries 
sum=0
for o in olympics:
    sum=sum+o.get("gold")
gold_avg=sum/len(olympics)
# print(gold_avg)

#q7 average number of total medals won by the countries
medal_count={o.get("country"):o.get("gold")+o.get("silver")+o.get("bronze") for o in olympics}
print(medal_count)
for v in medal_count.values():
    v=v/len(olympics)
print(medal_count)
# How many countries won at least 100 medals in total?
# Which countries won more than 10 gold medals?

