#create a function is_prime(number) to return true if the no. is prime and false if not


def is_prime(num):

    for i in range(2,num):

      if num%i==0:

         return False

         break
    
    return True

print(is_prime(13))
      
    