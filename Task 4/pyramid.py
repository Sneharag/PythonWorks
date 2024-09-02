#        *
#      *   *
#     *  *  *
#   *  *   *  *
#  *  *  *  *  *  
# *  *  *  *  *  *


for row in range(0,6):

    for col in range(1,7-row-1):

        print(end=" ")
   
    for col in range(0,row+1):

        print("*",end=" ")

    print()