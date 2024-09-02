
#print sum of numbers

arr=[[10,20],[20,30],[40,50]]

numbers=[num for lst in arr for num in lst]

print(sum(numbers))