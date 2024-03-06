
import math
import sys

while True:
	
	print("#######################")
	
	print(" ")
	
	print("Calculate the Area's of different Shapes:")
	
	print(" ")
	
	print(" * * * * * * * * ")
	
	s = print("1.Square")
	re = print("2.Rectangle")
	c = print("3.Circle")
	tr = print("4.Triangle")
	t = print("5.Trapezium")
	r = print("6.Rhombus")
	
	print(" * * * * * * * * ")
	
	print(" ")
	
	q = print("Press 'q' to exit the program!")
	
	print(" ")
	
	print("#######################")
	
	s = 1
	re = 2
	c = 3
	tr = 4
	t = 5
	r = 6
	
	
	options = input("Choose an option: ")
	
	if options == '1':
		length = int(input("Enter length: "))
		
		def squareArea(length):
			area = length ** 2
			return area
		
		areaOfSquare = squareArea(length)
		print("Area of Square :",areaOfSquare)
	
	elif options == '2':
		length = int(input("Enter length :"))
		breadth = int(input("Enter breadth :"))
		
		def rectangleArea(length, breadth):
			area = length * breadth
			return area
		
		areaOfRect = rectangleArea(length, breadth)
		print("Area of Rectangle :",areaOfRect)
	
	elif options == '3':
		radius = int(input("Enter radius :"))
		
		def circleArea(radius):
			pi = math.pi
			area = pi * radius ** 2
			return area
		
		areaOfCir = circleArea(radius)
		print("Area of Circle :",areaOfCir )
	
	elif options == '4':
		base = float(input("Enter base :"))
		height = float(input("Enter height :"))
		
		def triangleArea(base, height):
			area = 0.5 * base * height
			return area
			
		areaOfTri = triangleArea(base, height)
		print("Area of Triangle :",areaOfTri)
		
	elif options == '5':
		base1 = int(input("Enter base 1: "))
		base2 = int(input("Enter base 2: "))
		height = int(input("Enter height: "))
		
		def trapeziumArea(base1, base2, height):
			area = ((base1 + base2) / 2) * height
			return area
			
		areaOfTrap = trapeziumArea(base1, base2, height)
		print("Area of Trapezium: ",areaOfTrap)
		
	elif options == '6':
		diagonal1 = int(input("Enter diagonal 1: "))
		diagonal2 = int(input("Enter diagonal 2: "))
		
		def rhombusArea(diagonal1, diagonal2):
			area = (diagonal1 * diagonal2)/2
			return area
			
		areaOfRhom = rhombusArea(diagonal1, diagonal2)
		print("Area of Rhombus: ",areaOfRhom)
		
	elif options == 'q':
		print("Thanks for using the program!")
		sys.exit()
	
	else:
		print("Choose a proper option!!")
		
	print("#######################")