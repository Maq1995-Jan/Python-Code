import math as m

pi = m.pi

def radToDeg(value):
	result = value * (180/pi)
	print("The degree is :",result)
	return result
	

def degToRad(value):
	result = value * (pi/180)
	print("The radian is :",result)
	return result


while True:
        
        option = input("Choose and option of r (or) d?:")
        
        
        if option == 'r':
        	
        	temp = input("Enter radian :")
        	
        	value = int(temp)
        	
        	radToDeg(value)
        	
        elif option == 'd':
        	
        	temp = input("Enter degree :")
        	
        	value = int(temp)
        	
        	degToRad(value)
        	
        else:
        	
        	print("Enter a valid value")