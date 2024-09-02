#find second largest num in the list

num=[3,2,5,7,1,9,10,4]

#num.sort()  #[1,2,3,4,5,7,9,10]

smallest_num=num[-1]   

second_smallest=num[0]     

for i in num:

    if i < second_smallest and i < smallest_num:   

        second_smallest=smallest_num

        smallest_num=i

    elif i < second_smallest and i > smallest_num:  

        second_smallest=i

print(second_smallest)
