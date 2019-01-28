def checkMagicVowel(input_string):
	#The Answer Variable 
	counter = 0

	#Check if all vowels exist
	if ('a' in input_string) and ('e' in input_string) and ('i' in input_string) and ('o' in input_string) and ('u' in input_string):

		vowel_string = 'aeiou'
		input_string_voweslOnly = ''

		#Keeping only vowels in the string i.e user string MINUS NON vowels
		for letter in input_string:
			if letter in 'aeiou':
				input_string_voweslOnly = input_string_voweslOnly + letter
		#aaeiaaioooaauuaeiou
		magic = ''
		index_on_vowel_string = 0
		current_vowel = vowel_string[index_on_vowel_string]
		#i is index on the current Character besing tested
		i = 0
		for current_char in input_string_voweslOnly:
			
			if current_char == current_vowel:
				counter = counter + 1
				magic = magic + current_char

			if (i < len(input_string_voweslOnly)-1):
				next_char = input_string_voweslOnly[i+1]

				if(index_on_vowel_string != 4):
					next_vowel = vowel_string[index_on_vowel_string+1]
				else:
					next_vowel = vowel_string[index_on_vowel_string]

				#next character should be the next new vowel only to count++
				if (current_char != next_char and next_char == next_vowel):
						if(index_on_vowel_string != 4):
							index_on_vowel_string = index_on_vowel_string + 1
						current_vowel = vowel_string[index_on_vowel_string]

			i = i + 1
		
	else:
		counter = 0
	return counter

print(checkMagicVowel('aaeiaaioooaauuaeiou'))