#File: CS112_A_1_T2_Game2_20230053.py.
#purpose: 1/Players take turns choosing unique numbers (1-9) until someone scores 15 with any 3, or all numbers are used, resulting in a draw.
#         2/Win by selecting any 3 numbers that add up to 15 before your opponent or before all numbers are depleted.
#Author: Israa Abdelhaq Mohammed El Sayed
#ID: 20230053



print ("                          welcome in Number scrabble                  ")

print (" Each player takes turns picking a number from the list. Once a number has been picked, it cannot be picked again. If a player has picked three numbers that add up to 15, that player wins the game.However, if all the numbers are used and no player gets exactly 15, the game is a draw.")
from itertools import combinations

#define a set to store available number (1 - 9)
available_list = set (range(1 , 10))

#create empty list to store player numbers 
player1_list = []
player2_list = []

#True for player 1 False for player 2
current_turn = True


#function to display the current state of game board 
def state_game ():
    print (" available_list:")
    print ( ",".join(map(str,available_list)))
    print (" player1_list:")
    print ( ",".join(map(str,player1_list)))
    print (" player2_list:")
    print (",".join(map(str,player2_list)))





#function to check the valid number
def valid_input (player):
    while True:
        try:
            choice = int (input(f"player{player},chooce a number from available_list: " ))
        except ValueError:
            print ("invalid input...please enter a number: ")
            continue
        if choice not in available_list:
            print ("number already choosen or not in range.please enter another number: ")
            continue
        return choice





#function Checks if the 3 numbers in a player's choices list sum to 15.
def check_3_num_win (choices):
    for combination in combinations(choices, 3):
        if sum(combination) == 15:
            return True

    return False





#game loop continues until all number are choicen or a player wins
#show the current state of game
while available_list and not check_3_num_win(player1_list) and not check_3_num_win(player2_list):
    state_game()

    #if player 1 turn
    if current_turn:
        #get the valid number from player 1
        choice = valid_input(1)
        #remove the chosen number from available number list
        available_list.remove(choice)
        #add the chosen number to player 1 list
        player1_list.append(choice)
        #switch to player 2
        current_turn = False


    #if player 2 turn
    else:
        choice = valid_input(2)
        available_list.remove(choice)
        player2_list.append(choice)
        current_turn = True

#show the final state games
state_game()




if check_3_num_win(player1_list):
    print ("player 1 is win")
elif check_3_num_win(player2_list):
    print ("player 2 is win")
else:
    print ("the game is a draw")