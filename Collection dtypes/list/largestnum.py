#find largest no. in the list

num=[1,3,2,5,7,9,10,4]

# num.sort()

# print(num[-1])

#without using methods

largest_num=num[0]

for i in num:

    if i > largest_num:

        largest_num=i

print(f"Largest no is {largest_num}")
