import random
import string
import os

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

def load_passwords(file_path):
	# Gathers all current passwords saved in the txt file
	passwords = {}
	if os.path.exists(file_path):
		with open(file_path, "r") as file:
			for line in file:
				key, password = line.strip().split(":")  # Splits keys and password by their ":" i.e "Steam:xxxxxxxx"
				passwords[key.lower()] = password  # Take the lowercase of the key, i.e. 'Steam' and 'steam' will be the same
	return passwords

def save_passwords(file_path, passwords):
	# Saves the generated password to the text file
	with open(file_path, "w") as file:
		for key, password in passwords.items():
			file.write(f"{key}:{password}\n")

def get_desktop_path():
	# Where your desktop is! In my case I use wsl and save to windows like this. 
	# Change ~ to your username
	home = os.path.expanduser("/mnt/c/Users/~")
	desktop_path = os.path.join(home, "Desktop")
	return desktop_path

def get_user_input():
	desktop_path = get_desktop_path()
	file_path = os.path.join(desktop_path, "passwords.txt")

	passwords = load_passwords(file_path)

	while True:
		try:
			key = input("What is this password for?: ").strip().lower()

			if key in passwords:
				overwrite = input(f"A password for '{key}' already exists, do you want to overwrite it? (y/n): ").strip().lower()
				if overwrite != 'y':
					print("Skipping password generation.")
					break

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

			# Save the password in the dictionary
			passwords[key] = password

			# Save the password to the file
			save_passwords(file_path, passwords)

			print(f"Password for '{key}' saved to {file_path}")
			break

		except ValueError as e:
			print("Invalid input:", e)
			print("Please try again.\n")
get_user_input()

