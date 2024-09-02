#find count of object in expenses
#print all expenses
#print expenses > 15000
#print total objects
#print average expense

expenses=[12000,13000,14000,15000,21000,22000,13000]

expense_count=len(expenses)
print(expense_count)


for i in range(0,expense_count):

    print(expenses[i])


for i in range(0,expense_count):

    if expenses[i]>15000:

        print(expenses[i])


sum=0
for i in range(0,expense_count):

    sum=sum+expenses[i]
print(sum)

avg=sum/expense_count
print(avg)
