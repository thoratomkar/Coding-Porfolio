def myfunc(*args):
    '''
    creating list of even numbers from the arguments
    '''
    mylist=[]
    #x=0
    for x in args:
        if x%2==0:
            mylist.append(x)
            #x=x+1
        else:
        	#x=x+1
            continue
    return mylist

mylist=myfunc(100,1,2,3,45,67,8)
print(mylist)
