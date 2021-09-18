
print("Welcome to Circle calculator\n\n")

pi = 22/7

def arus(radius):
	area = radius**2 * pi
	return area
def circum(radius):
	circum = 2 * radius * pi
	return circum
def vol(radius):
	volume = (4 * pi * radius**3)/3
	return volume
def sarus(radius):
	surarus = 4 * pi * radius**2
	return surarus

while True:
	start = input("Press Y to start or N to exit\n>").lower()

	if start == "y" or start == "yes":
			selecto = input("do you want to calculate...\n1: Circle\n2: Sphere\n[use serial numbers only]\n>")
			if selecto == "1":
				selecto = input("What do you want to calculate?\n 1 - Area\n 2 - Circumference\n [use serial number only]\n>")
				if selecto == "1":
					r = int(input("Enter the radius\n>"))
					print(arus(r))
				elif selecto == "2":
					r = int(input("Enter the radius\n>"))
					print(circum(r))
				else:
						print("Incorrect input! Try again. [use serial number of the function only]! ")
			elif selecto == "2":
				selecto = input("What do you want to calculate?\n 1 - Voulume\n 2 - Surface area\n [use serial number only]\n>")
				if selecto == "1":
						r = int(input("Enter the radius\n>"))
						print(vol(r))
				elif selecto == "2":
					r = int(input("Enter the radius\n>"))
					print(sarus(r))
				else:
						print("Incorrect input! Try again. [use serial number of the function only]! ")
	elif start == "n" or start == "no":
		exit()
	else:
		print("Incorrect input [please use Y(es) or N(o)]!")
