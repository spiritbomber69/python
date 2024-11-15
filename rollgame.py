import random

def roll():
    min_value = 1
    max_value = 6

    roll = random.randint(min_value,max_value)

    return roll


min_players = 2
max_players = 5
while True:
    players = input("Enter the number of players(2-5): ") 

    if players.isdigit():
        players = int(players)
        if min_players <= players <= max_players:
            break
        else:
            print("Invalid number of players!!!")
        
    else:
        print("Enter a valid input(number)!!!")

max_score =  50

players_scores = list(0 for _ in range(players))

while max(players_scores) < max_score:
    
    for player_index in range(players):
        print("\nPlayer ",player_index + 1," your turn has started!\n")

        current_score = 0

        while True:
            roll_choice = input("Do you wish to roll(y): ")

            if roll_choice.lower() == 'y':
                value = roll()

                if value == 1:
                    print("You have rolled a 1,you are done!")
                    break
                else:
                    current_score += value
                    print("You have rolled a ",value,"and your current score is ",current_score)

            else:
                break

        players_scores[player_index] += current_score


print(list(players_scores))
        


                
        
    
      
        
   
            
           
       
            


    
    
