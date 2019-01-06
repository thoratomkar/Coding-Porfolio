mylist=[1,2,3,4,5,6,7,8,9,10]

for num in mylist:
	if num%2==0:
		print(f'{num} is a even number')
	else:
		print(f'{num} is a odd number')


d={'k1':123,'k2':456,'k3':789}

for k,v in d.items():
	print(k,v)


l=[(1,2,3),(4,5,6),(7,8,9)]

for i,j,k in l:
	print(k)


string='Hello World'
#i=0
#print(string[4])
#for i in string:
print(string[::2])
	