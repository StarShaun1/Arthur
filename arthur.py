import pyfiglet, os
os.system("cls|clear") # "cls" clears the console in windows and "clear" does it in linux.
print(pyfiglet.figlet_format("ARTHUR", font="banner")) # better method of doing the funny text :D

lol = input("squeeze your left nut and beg for mercy (y/n) : ")

if lol == "y":
	print("i spare you")
else:
	if lol == "n":
		print("you die")
	else:
		print("bitch u didnt even say either of those")
