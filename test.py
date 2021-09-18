print("Welcome to Circle calculator\n\n")

pi = 22/7

def arus(radius):
	area = radius * radius * pi
	return area
def circum(radius):
	circum = 2 * radius * pi
	return circum

while True:
	start = input("Press Y to start or N to exit\n>").lower()

	if start == "y" or start == "yes":
		selecto = input("What do you want to calculate?\n 1 - Area\n 2 - Circumference\n [use serial number only]")
		if selecto == "1":
			r = int(input("Enter the radius of the circle\n>"))
			print(arus(r))
		elif selecto == "2":
			r = int(input("Enter the radius\n>"))
			print(circum(r))
		else:
				print("Incorrect input! Try again. [use serial number of the function only]! ")
	elif start == "n" or start == "no":
		exit()
	else:
		print("Incorrect input [please use Y(es) or N(o)]!")
