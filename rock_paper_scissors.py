import random 

player = input("Hello! rock, paper or scissors?").lower()

if player == "rock" or player == "paper" or player == "scissors":
    print(f"You've picked: {player}")
else:
    pass 
    

if player == "rock" :
    print("""   
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)    """)
    
elif player == "paper": 
    print("""   
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)""")

elif player == "scissors":
    print("""  
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)""")

else:
    print("Invalid Choice! Try again.")


choice = random.choice(["rock", "paper", "scissors"])

print("The computer picked:")

if choice == "rock" :
    print("""    
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

elif choice == "paper":
    print("""  
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
""")

else:
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)""")


if choice == player :
    print("It's a tie!")
    
elif choice == "paper" and player == "rock" :
    print("The computer has won!")
    
elif choice == "paper" and player == "scissors" :
    print("You've won!")
    
elif choice == "rock" and player == "scissors" :
    print("The computer has won!")
    
elif choice == "rock" and player == "paper" :
    print("You've won!")
    
elif choice == "scissors" and player == "rock" :
    print("You've won!")    
    
elif choice == "scissors" and player == "paper" :
    print("The computer has won!")
    
