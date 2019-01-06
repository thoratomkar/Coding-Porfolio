n=122
o=n
s=0
t=0
while (n>0):
	#o=n
	s=n
	n=n//10
	s=s%10
	t=t*10+s
#print(n)
if t==o:
	print(f'{t} is a palindrome')
else:
	print(f'{o} is not a palindrome')