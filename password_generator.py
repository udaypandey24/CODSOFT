import random
import string

print(" PASSWORD GENERATOR ")

password_length = int(input("Enter desired password length: "))

include_special = input("Do you want special characters? (yes/no): ").lower()

character_pool = string.ascii_letters + string.digits

if include_special == "yes":
    character_pool += string.punctuation

generated_password = ""

for i in range(password_length):
    generated_password += random.choice(character_pool)

print("\nGenerated Password:")
print(generated_password)

if password_length >= 12:
    print("Password Strength : Strong")
elif password_length >= 8:
    print("Password Strength : Medium")
else:
    print("Password Strength : Weak")

print("Thank you for using Password Generator!")
