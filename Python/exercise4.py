#LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd
def compare(a,b):
	if(a%2==0) and (b%2==0):
		return min(a,b)
	else:
		return max(a,b)

result=compare(2,4)
print(result)

#ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
def animal(s):
	lst=[]
	mylist=s.split()
	for x in mylist:
		lst.append(x[0])
	if lst[0]==lst[1]:
		return True
	else:
		return False
result=animal('my Monkey')
print(result)

#MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
def makes_twenty(a,b):
	if (a+b)==20 or ((a==20) or (b==20)):
		return True
	else: 
		return False
result=makes_twenty(0,10)
print(result)

#OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
def old_macdonald(name):
	mylist=[]
	mylist=name.split()

	for i,v in enumerate(mylist):

		if(len(v)>=4):
			v=v[:3].capitalize()+v[3:].capitalize()
			mylist[i]=v
			return " ".join(mylist)
		else:
			return "Name is too short"
result=old_macdonald("i am a masters student at ub")
print(result)

#Given a sentence, return a sentence with the words reversed
def reverseWords(s):
        """
        :type s: str
        :rtype: str
        """
        myList=[]
        mainList=[]
        count=0
        mainList=s.split()
        if(s==""):
        	return s
        else:
        	mainList.reverse()
        	for words in mainList:
        		myList.append(words[::])
        		myList.append(" ")
        	myList.pop()
        
        return ''.join(myList)
print(reverseWords('I am home'))

#ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
def almost_there(n):
	return abs(n-100)<=10 or abs(n-200)<=10
print(almost_there(90))