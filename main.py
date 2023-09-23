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
    
    
