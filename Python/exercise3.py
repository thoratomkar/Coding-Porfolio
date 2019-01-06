def myfunc(s):
    mylist = []
    for x in range(0,len(s)):
        if x%2==0:
            mylist.append(s[x].upper())
        else:
            mylist.append(s[x].lower())
    return ''.join(mylist)
    
result=myfunc('vhasdvhgsaddfsgddgdhdhd')
print(result)