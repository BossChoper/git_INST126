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