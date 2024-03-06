string = "Abuzer"

list = []


vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

for vowel in string:
	
    if vowel in vowels:
		
	    list += vowel


noOfVowels = len(list)
print(noOfVowels)