#set methods
# add(),clear(),pop(),discard(),update(),union(),intersection(),difference()


names={"hello","hari","kollam","chennai"}

# names.add("kochi")   #add an element to a set object
# print(names)

# names.clear()    #removes all elements from set,empty set remains
# print(names)

# names.pop()      #removes a random element from the list 
# print(names)

# names.discard("hari") #remove an element from a set if it is a member.if element is not a member,do nothing.
# print(names)

new_names={"hp","dell","lenovo","hello"}

# names.update(new_names)   #add elements from any collection to the set
# print(names)

# new_set= names.union(new_names) #returns the combined elements from the two sets and returns as a new set

# new_set=names.intersection(new_names) #return common elements from the two sets and returns as a new set

# new_set=names.difference(new_names)  #returns elements from set names which is not in set new_names as new set

new_set=names.symmetric_difference(new_names)  #combine 2 sets and remove common elements 
print(new_set)
