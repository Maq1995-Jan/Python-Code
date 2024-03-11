def grading(file):
	
	with open(file, 'r') as values:
	   	marks = values.read()
	   	n = marks.split()
	   	numbers = [int(numbers) for numbers in n]
	
	with open(file, 'w') as result:
		
		result.write('\n')
		
		step = 1
		
		
		for value in numbers:
			
			if value in range(0, 49 + step, step):
				result.write(f'{value} = F' + '\n')
			
			elif value in range(50, 59 + step, step):
				result.write(f'{value} = E' + '\n')
			
			elif value in range(60, 69 + step, step):
				result.write(f'{value} = D' + '\n')
			
			elif value in range(70, 79 + step, step):
				result.write(f'{value} = C' + '\n')
				
			elif value in range(80, 89 + step, step):
				result.write(f'{value} = B' + '\n')
				
			elif value in range(90, 100 + step, step):
				result.write(f'{value} = A' + '\n')
		
			else:
				result.write(f'{value} = None' + '\n	')

while True:
	
    file = input("Enter a file name with its address : ")
    
    grading(file)