# # user_input = (input("Enter any phrase"))
# text = user_input.split()
# print(text)
# a = " "
# # for i in text:
# #     a = a+str(i[0]).upper()
# user_input.capitalize
# print(a)
# txt = "welcome to the jungle"

# x = txt.split()

# print(x)

#generating password with python:
import random
passlen = int(input("enter the length of password"))
s="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
p = "".join(random.sample(s,passlen ))
print(p)