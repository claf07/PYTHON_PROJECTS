import random

def userin():
    user_input=input("Enter your choice: [rock,paper,scissors]")
    print(f'Your choice is {user_input}')
    return user_input

def computerin():
    choice=["rock","paper","scissors"]
    computer_choice =random.choice(choice)
    print(f"The computer chose {computer_choice}")
    return computer_choice

def check_win(player1,player2):
    if player1==player2:     
        print("Its a Tie!")
    elif (player1=="rock" and player2=="scissors") or (player1=="paper"and player2=='rock') or (player1=="scissors" and player2=='paper'): 
        print("Congratulations! You win this round.")
    else:    
        print("Computer wins this round.")

while True:
    user_in=userin()
    computer=computerin()
    check_win(user_in,computer)
    play_again=input("Do you want to play again? [y/n]")
    if play_again.lower()!='y':
        break

    
