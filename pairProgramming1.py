#github repo for Pair Programming Session 1 on April 16, 2024
import os
import random
#each player takes a turn rolling dice, the goal is to get the highest number after
# a few turns.
#each player rolls dice three times during one turn

die_sides = (1, 2, 3, 4, 5, 6)
# above is a variable containing the sides of the die that can be rolled
roll_counter = {1 : 0, 2 : 0, 3 : 0, 4: 0, 5 : 0, 6 : 0}
# above is a counter to count the roll results depending on the number rolled
win_total = 10 
#above is the total for winning the game. It should be 50 
random.choice(die_sides)

roll_results = []

print("Hello. Please start your turn by entering yes.")
question1 = ("Enter yes to start, no to  wait")
if question1 == "yes":
    this_roll = random.choice(die_sides)
    roll_results.append(this_roll)
    print(roll_results)


# April 11 INST 126 Practice (Die_Roll code)
# Topic: 

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