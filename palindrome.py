import sys


def palindrome(x):
	
	r = x[::-1]
	
	print(r)
	
	if x == r:
		
		print("Its a Palindrome!")
		
	else:
		
		print("Its not a Palindrome.")
		
		
while True:
	
	
	x = input("Enter a string: ").lower()
	
	if x == 'q':
		sys.exit()
		
	palindrome(x)