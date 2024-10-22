import random
import string

def generate_password(length=16, use_special_chars=False):
	# Basic character set: digits and letters using string library
	characters = string.digits + string.ascii_letters  # 1-9, a-z, A-Z
			        
	# If user wants special characters they are appended to char set
	if use_special_chars:
		special_characters = ['!', '?', '@', '#', '$', '%', '&']  
		characters += ''.join(special_characters)  
							     
	# For loop of password length will choose a random char out of large char set 
	password = ''
	for x in range(length):
		password += random.choice(characters) 

	return password

def get_user_input():
	while True:
		try:
			length = int(input("Enter desired password length between 16-24: "))
			if not 16 <= length <= 24:
				raise ValueError("Password length must be between 16 and 24.")

			use_special_chars = input("Would you like to include special characters? (y/n): ").strip().lower()
			if use_special_chars == 'y':
				use_special_chars = True
			elif use_special_chars == 'n':
				use_special_chars = False
			else:
				raise ValueError("Must be y or n.")

			password = generate_password(length, use_special_chars)
			print("Generated password:", password)
			break

		except ValueError as e:
			print("Invalid input:", e)
			print("Please try again.\n")
get_user_input()
