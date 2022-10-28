#############################################################################
## 									   ##
##	Title : Celsius <====> Fahrenheit Converter			   ##
##									   ##
##	Author : Ernest Odhiambo Elnino					   ##
##									   ##
##	Github : https://github.com/ProtocolWhisperer01 		   ##
#############################################################################

# User to enter the degree celsius or Fahrenheit


print("This is a tool to convert degrees Celsius to Fahrenheit vice versa!")

choose_opt = input("Please choose 1 or 2 to pick a mode:  ")

try:

	valid_opt = float(choose_opt)
	
	if valid_opt == 1:

		print("You are entering Celsius to Fahrenheit mode 🛑️! ")
	
		deg_celcius = float(input("Enter the degrees celcius :\n"))
	
		to_fahrenheit = (deg_celcius * 9)/5 + 32
	
		print(deg_celcius, " celcius to fahrenheit is ", to_fahrenheit)
	
		print("Thanks and see you later!")
	
	elif valid_opt == 2:

		print("You are entering Fahrenheit to Celcius mode 🧿️! ")
	
		deg_fahren = float(input("Enter the degrees fahrenheit:\n"))
	
		to_celcius = ((deg_fahren - 32) * 5)/9
	
		print(deg_fahren, " fahrenheit to celcius is ", to_celcius)
	
		print("Thanks and see you later!")
	
	else:

		print("Invalid input 😅️!")

except:

	print("Please enter a number 🤔️, because I don't know what you are trying to do ! ")


