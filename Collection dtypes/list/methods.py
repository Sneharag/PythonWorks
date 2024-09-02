#list is a class
#list class has methods that can do operations

#list methods
#append(),insert(),count(),pop(),remove(),extend(),sort(),reverse()

num=[1,2,3,4]

num.append(5)  #add element to the end of the list 
print(num)

num.insert(1,6)  #insert(index,value)-add element to the specific position
print(num)

print(num.count(6))  #returns the count of an element

print(num.pop())  #pop(index)-remove last element/specified position of the list and return that value

num.remove(3)   #removes the specific element in the first occurance of the value and return the remaining list
print(num)

num.extend([9,8,7,6])  #add a collection of elements to a list
print(num)

num=[3,4,6,8,1]
num.sort()        #arrange the integers in ascending order and chars in alphabetical order
print(num)#ascending order

num.sort()
num.reverse()#descending order    #reverse the list
print(num)

name=['t','h','o','m','a','s']
name.sort()
print(name)

