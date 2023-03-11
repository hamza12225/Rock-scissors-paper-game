import random 

user_wins = 0
computer_wins = 0


options = ["rock","scissors","paper"]

name = input("enter your name to start the game!").lower()


while True:
    user_input = input("Enter rock / scissors / paper (Q for quit!)").lower()
    if user_input =="q":
        break
    
    if user_input not in options:
        continue

    random_number = random.randint(0,2)

    pick_comptuer = options[random_number]
    print("comptuer pick : "+ pick_comptuer)

    if user_input == "rock" and pick_comptuer == "scissors":
         user_wins +=1
         print(name + " win  win ! , score ", user_wins)
    elif user_input == "scissors" and pick_comptuer == "rock":
        computer_wins += 1 
        print("comptuer win ! , score ", computer_wins)
   

    elif user_input == "rock" and pick_comptuer == "paper":
        computer_wins += 1 
        print("comptuer win ! , score ", computer_wins)
    elif user_input == "paper" and pick_comptuer == "rock":
         user_wins +=1
         print(name + " win  win ! , score ", user_wins)



    elif user_input == "paper" and pick_comptuer == "scissors":
        computer_wins += 1 
        print("comptuer win ! , score ", computer_wins)
        
    elif user_input == "scissors" and pick_comptuer == "paper":
         user_wins +=1
         print(name + " win  win ! , score ", user_wins)

    else:
        print("the same option !")
        user_wins +=1
        computer_wins += 1 



print("computer scores is  : " + str(computer_wins) )
print(name +" scores is  : " + str(user_wins) )
if user_wins>computer_wins:
    print(name +" win  : ")
else:
    print("Comptuer win  : ")



  
print("Good bay!")



