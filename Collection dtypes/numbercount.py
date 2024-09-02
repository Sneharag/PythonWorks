#take a no. list  and print the count

numbers=[12,45,34,12,45,12,34]

number_count={}

for i in numbers:

    if i in number_count:

        number_count[i]+=1

    else:

        number_count[i]=1

print(number_count)