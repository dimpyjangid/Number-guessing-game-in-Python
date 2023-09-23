# Number-guessing-game-in-Python
# Welcome to the Number Guessing Game! This exciting game challenges you to guess a number within a given range. Simply enter your guess, and you'll be given a certain number of chances to get it right. To start, enter a number within the specified range. Then, put your guessing skills to the test and try to find the hidden number! Good luck! 
import random
import math

lower= int(input("enter the lower bound  :" ))
upper = int(input(" enter the upper bound :"))

x = random.randint(lower , upper)
print(round(math.log(upper - lower +1 , 2)))
print("chance to get guess!\n")

count =0
while count < math.log(upper - lower +1 , 2):
  count +=1

  guess = int(input(" guessing the no. :"))

  if x == guess:
    print("congrats you guess right !")
    break

  elif x < guess:
    print("sorry the number is too small , try again ")
  

  elif x> guess:
    print("sorry the number is to big , try again ")

if count >= math.log(upper - lower +1 , 2):
  print("\nThe number is %d" % x)
  print("\tBetter Luck Next time!")
    
    

