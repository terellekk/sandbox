import random 

def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors):")
    computer_choice = ["rock","paper","scissors"]
    randomizer = random.choice(computer_choice)
    choices = {"player": player_choice,
    "computer": randomizer}
    return choices
 
def checkWin(player, computer):
    if player == computer:
        return "It's a tie!"
    elif player == "rock":
        if computer == "scissors":
            return "Rock beats scissors...You win!"
        else:
            return "Paper beats rock...You lose."
    elif player == "paper":
        if computer == "rock":
            return "Paper beats rock...You win!"
        else:
            return "Scissors beats paper...You lose."
    elif player == "scissors":
        if computer == "paper":
            return "Scissors beats paper...You win!"
        else:
                return "Rock beats scissors...You lose."


choices2 = get_choices()
result = checkWin(choices2["player"], choices2["computer"])  

print(result)

    
