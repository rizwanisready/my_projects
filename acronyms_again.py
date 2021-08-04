# phrase = input("Enter the phrase: ")
# text = phrase.split()
# a = ""
# for i in text:
#     a = a + str(i[0]).upper()
# b = "."
# print(b.join(a))
#first step is user input 
phrase = input("Enter any phrase: ")
text = phrase.split()
a = ""
for i in text:
    a += str(i[0]).upper()
b = "."
print(b.join(a))