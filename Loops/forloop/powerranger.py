#2=>24[2+22]
#3=>369{3+33+333}

num=int(input("Enter number: "))

pattern=0

sum=0

for i in range(1,num+1):

    pattern=pattern*10+num

    sum=sum+pattern

    print(pattern)

print(f"Sum={sum}")
