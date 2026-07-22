import random
target=random.randint(1,100)
while True:
    user_choice=int(input("pick a number OR Quit:"))
    if(user_choice==quit):
        break
    if (target==user_choice):
        print("your guess is right!\n congragulation!!")
        break
    elif (user_choice<target):
        print("oops! your guess is wrong\n your guess is less than target")
    else:
            print("oops! your guess is wrong\n your guess is greater than target")  
print("----------GAME OVER----------")              
