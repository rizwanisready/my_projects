while(True):
    user_input = input("Convert F to C or C to F: ")
    if user_input == "q":
        print("Bye")
        break
    if user_input == "f" or "F":
        x = int(input("Enter the degree: "))
        c = (x-32)*5/9
        print(c)
    elif user_input == "c" or "C":
        y = int(input("Enter the degree: "))
        f = (y*9/5)+32
        print(f)
    else:
        print("Enter the correct alphabet")   
