
import random

die_faces = (1, 2, 3, 4, 5, 6)
# die_faces = [1, 2, 3, 4, 5, 6]

random.choice(die_faces)

#making a list to save choices and add new things
roll_results = []

#making keys for a dictionary variable to store information
#in this case of rolling a die, you can make one side a key
roll_counts = {1 : 0, 2 : 0, 3 : 0, 4 : 0, 5 : 0, 6 : 0}

# for loop to record roll information
for index in range(10):
    #run a random die roll and provide it to the reusults list
    this_roll = random.choice(die_faces)
    roll_results.append(this_roll)
    #updating the roll dictionary to confirm the new role addition
    roll_counts[this_roll] += 1
print(roll_results)
print(roll_counts)

#Restrictions:
#Game will have one or more players
#Players take turns rolling dice to score points or reach score
#Each turn, one player rolls three dice
#IF all dice are rolled with same number, "tupled out", ends turn
#If two dice have same value, they are fixed and are not rolled again
#Player can reroll any dice that is not fixed, until they stop or tuple out
#When player stops, score points equal to total of three dice and end turn
#If tupled out, turn ends and they get no points
#Limit is 50 score or five turns
#Display current score
#Record scores for each game
#Record high score/consistent score
#Implement AI
#Ability to change number of sides
#Add rules for special scoring

practice_results = []
practice_dictionary = {1: 0, 2 : 0}
two_sided_die = (1, 2)

#turn 1 for player 1
turn = 0
players = [1]

for index in range(3):
    current_roll = random.choice(two_sided_die)
    practice_results.append(current_roll)
    practice_dictionary[current_roll] += 1
print(practice_dictionary)
print(practice_results)

#Testing player count
#question1 = int(input("How many players are playing?"))

#for index in range(question1):
#    players.append(1)
#print(players)

player_results = []
player_dict = {1: 0, 2 : 0}
for player in players:
    #rolling for a player during one turn
    for index in range(3):
        current_roll = random.choice(two_sided_die)
        player_results.append(current_roll)
        player_dict[current_roll] += 1
    
print(players)
print(player_results)
print(player_dict)

#Testing tupled out
for index in range(3):
    current_roll = random.choice(two_sided_die)
    practice_results.append(current_roll)
    practice_dictionary[current_roll] += 1
    if practice_results[0] == practice_results[1]:
        print("The first two rolls are the same")

