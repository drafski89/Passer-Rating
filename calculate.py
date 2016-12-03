# Calculate the passer rating of a quarterback
# Python 3, but cover the option for 2.6+
from __future__ import print_function

# Manually change these numbers
# Note: These must be floats
completions = 30.0
attempts = 39.0
passingYards = 313.0
touchdowns = 2.0
interceptions = 0.0

# Do the calculation here:
# 	There are 5 parts
#	Part 1: ((Completions / Attempts) - 0.3) * 5
part1 = ((completions / attempts) - 0.3) * 5

#	Part 2: ((Passing Yards / Attempts) - 3) * 0.25
part2 = ((passingYards / attempts) - 3) * 0.5

# 	Part 3: (Touchdowns / Attempts) * 20
part3 = (touchdowns / attempts) * 20

# 	Part 4: 2.375 - ((Interceptions / Attempts) * 25)
part4 = 2.375 - ((interceptions / attempts) * 25)

# 	Part 5: Final Calculation
#	((Part1 + Part2 + Part3 + Part4) / 6) * 100
finalCalculation = ((part1 + part2 + part3 + part4) / 6) * 100

#	Print the result to the user
print("The passer rating is: " + str(finalCalculation))