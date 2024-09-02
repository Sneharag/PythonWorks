#find secondlargest no. in the list

num=[3,2,5,7,1,11,10,4]

# num.sort()

# print(num[-2])

#without using methods

largest_num=num[0]         # 3

second_largest=num[0]      # 3

for i in num:              # 10

    if i > largest_num and i > second_largest:   # 5>3and5>3   7>5and7>3   11>7and11>5  10>11and10>7

        second_largest=largest_num               #3            5           7

        largest_num=i                            #5            7           11

    elif i > second_largest and i < largest_num: #10>7and10<11

        second_largest=i                          #10

print(second_largest)

