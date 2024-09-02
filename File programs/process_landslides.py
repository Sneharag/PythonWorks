
f=open("D:\\PythonWorks\\File programs\\land_slides.txt","r")

data=[]
for line in f:
    lst=line.rstrip("\n").split(" ")
    dict={"state":lst[0],"year":lst[1],"death_count":int(lst[2])}
    data.append(dict)
# print(data)

death_per_state={}
for d in data:
    state=d.get("state")
    death_count=d.get("death_count")
    if state in death_per_state:
        death_per_state[state]+=death_count
    else:
        death_per_state[state]=death_count
print(death_per_state)


# most death count year
death_year={}
for d in data:
    year=d.get("year")
    death=d.get("death_count")
    if year in death_year:
        death_year[year]+=death
    else:
        death_year[year]=death
print(death_year)
most_death_year=max(death_year,)
# print(most_death_year)