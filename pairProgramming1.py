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
