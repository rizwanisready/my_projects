#for generating password we will use the random module in samples:
#firstly we will import random
import random
password_lenght = int(input("Enter the length of your password: "))
s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890+_)(*&^%$#@!"
p = "".join(random.sample(s, password_lenght))
print(p)