# necessary imports
import secrets
import string

# define the alphabet
letters = string.ascii_letters
digits = string.digits
special_chars = "!#$%&()*+:;<=>?@_"
#print(string.punctuation)
print("What type of Password do you want? ")
userInput = input()

# fix password length
pwd_length = int(input("What is the length : "))

# generate a password string
pwd = ''
if userInput == "Simple":
    alphabet = letters + digits
    for i in range(pwd_length):
      pwd += ''.join(secrets.choice(alphabet))
else:
    alphabet = letters + digits + special_chars
    for i in range(pwd_length):
      pwd += ''.join(secrets.choice(alphabet))
# print the password
print(pwd)
