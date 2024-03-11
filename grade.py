#If a text file with address is given as input, it will grade the numbers as per the condition

def grading(file):
	
	
	
	with open(file, "r") as values:
		marks = values.read()
		n = marks.split()
		
		
		numbers = [int(numbers) for numbers in n]
		
		step = 1
		
		
		for value in numbers:
			
			if value in range(0, 49 + step, step):
				print("F")
			
			elif value in range(50, 59 + step, step):
				print("E")
			
			elif value in range(60, 69 + step, step):
				print("D")
			
			elif value in range(70, 79 + step, step):
				print("C")
				
			elif value in range(80, 89 + step, step):
				print("B")
				
			elif value in range(90, 100 + step, step):
				print("A")
		
			else:
				print("None")

while True:
	
    file = input("Enter a file name with its address : ")
			
    grading(file)