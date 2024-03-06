def removeVowels(string):
    vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    result = " "

    for char in string:
        if char not in vowel:
            result += char
    return result

while True:
	
    string = input("Enter a string: ")

    removeVowels(string)

    print("Removed string is:",removeVowels(string))