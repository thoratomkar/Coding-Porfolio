
def pig_latin(word):
	if word[0].lower() in'aeiou':
		return word+'ay'
		#print(word[0])
	else:
		x=word[0]
		word=word[1:]+x+'ay'
		return word

value=pig_latin('Gun')
print(value)