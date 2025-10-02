# FILE NAME - coin_toss.py

# NAME: Michael Carney
# DATE: Wednesday October 2, 2025
# BRIEF DESCRIPTION: Random Coin Toss

# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience

########## ENTER YER CODE BELOW THIS LINE ##########
# Don't forget to import random!!!!!
import random
print("===== Coin Flipper =====")
toss = random.randint(1,100)
if 1 <= toss <= 50:
        print("Heads")
else:
      print("Tails")

########### END YER CODE ABOVE THIS LINE ###########

########################################
#          SAMPLE OUTPUT
########################################
'''
===== Coin Flipper =====
Heads
'''

'''
===== Coin Flipper =====
Tails
'''

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What was the hardest part of completing this lab?
   Trying to figure out how to have random choose from a sequence of strings,
   "heads" and "tails". I couldn't figure it out.
'''