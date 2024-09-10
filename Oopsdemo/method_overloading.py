
class Operations:

    def perform_add(self,*args):

        # total=0

        # for arg in args:

        #     if isinstance(arg,(int,float)):

        #         total=total+arg
        total=sum( [arg for arg in args if isinstance(arg,(int,float))])

        return total
    
    def get_max_num(self,*args):

        return max(args)
    
math=Operations()

print(math.perform_add(10,20,80.5,"hello",True))

print(math.get_max_num(100,500))


# *args => arguments tuple
# **kwargs => keyword arguments dictionary

def get_person(**kwargs): #args("hari","tvm","kakkanad")

    print(kwargs.get("name"))
    print(kwargs.get("w_place"))

get_person(name="hari",w_place="tvm",n_place="kakkanad")




def flat_list(*args):

    flat=[]

    for arg in args:

        if isinstance(arg,list):

            flat.extend(flat_list(*arg))

        else:

            flat.append(arg)

    return flat

print(flat_list(1,2,[10,20],[10,[100,200]]))