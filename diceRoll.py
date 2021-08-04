#importing module for random number generation
import random

#range of the values of a dice
# min_val = 1
# max_val = 6
User_1 = random.randint(1, 6)
User_2 = random.randint(1, 6)

#to loop the rolling through user input
roll_again = "yes"
turns = 0
sum_user_1 = []
sum_user_2 = []

#loop
while roll_again == "yes" or roll_again == "y":
    print("Rolling The Dices...")
    print("The Values are :")
    
    #generating and printing 1st random integer from 1 to 6
    print(f"Value for User First is {User_1}")
    
    #generating and printing 2nd random integer from 1 to 6
    print(f"Value for User Second is {User_2}")
    
    #asking user to roll the dice again. Any input other than yes or y will terminate the loop
    roll_again = input("Roll the Dices Again?") 
    #giving 5 turns to complete the task
    turns = turns + 1
    if turns == 5:
        break
    #making list to know the numbers
    sum_user_1.append(User_1)
    sum_user_2.append(User_2)
    print(sum_user_1)
    print(sum_user_2)
#adding elements to find who win who loose
if sum(sum_user_1) > sum(sum_user_2):
    print(f"the Total User 1 is {sum(sum_user_1)} n Total User 2 is {sum(sum_user_2)} thats why User 1 Wins!")
if sum(sum_user_2) > sum(sum_user_1):
    print("User 2 Wins!")
if sum(sum_user_1) == sum(sum_user_2):
    print("Its a Tie!")
    
    
    