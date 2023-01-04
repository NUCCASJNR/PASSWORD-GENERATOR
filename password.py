#  STRONG RANDOM PASSWORD GENERATOR

from random import sample
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "01234567890"
signs = "~!@#$%^&*()?><"
use_for = lower_case  + upper_case + number + signs
lengt_for_pass = 10
password = "".join(sample(use_for, lengt_for_pass))
print("Your generated password is:", password)  