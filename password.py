#  STRONG RANDOM PASSWORD GENERATOR
import random
from random import sample
import string
print("Generate random password")
length = int(input("Enter length of your password :"))
chars = string.ascii_letters + string.digits + string.punctuation
password = "".join(sample(chars, k = length))
print("Your generated password is:", password)