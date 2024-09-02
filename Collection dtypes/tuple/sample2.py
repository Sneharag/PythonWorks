#input=[1,2,[3,(100,200,300),4],5,6]
#output=[1,2,[3,4,(100,150,200,300)],5,6]

numbers=[1,2,[3,(100,200,300),4],5,6]

num=numbers[2][1]   

new_num=list(num)   

new_num.insert(1,150)   

print(tuple(new_num))

numbers[2][1]=numbers[2][2]

numbers[2][2]=tuple(new_num)

print(numbers)