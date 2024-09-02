#print numbers greater than 15

arr=[[10,20],[21,30],[40,53]]

greater=[num for lst in arr for num in lst if num>15]

print(greater)