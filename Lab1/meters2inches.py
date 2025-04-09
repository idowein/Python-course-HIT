# Meters, Centimeters, and Inches

# input
# str to float
# M, CM, inch
# print (f-string)

meters = input("Please enter the length in meters: ")
meters = float(meters)
centimeters = meters * 100
inches = centimeters / 2.54
print(f"{meters} meters equals to {centimeters:.2f} centimeters.") ## will write 2 numbers after the dot
print(f"{meters} meters equals to {inches:.2f} inches.")