

from json import load

f=open("D:\\PythonWorks\\jsonWorks\\films.json")

movies=load(f)

for m in movies:

    print(m.get("title"))