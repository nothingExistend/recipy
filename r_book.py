import random
import sys
import os
import requests
import importlib.util

url = ""
#test



r_max = 1 #ERHÖHEN WENN MEHR REZEPTE ADDED

def title() :
  print(r"  ___ ___ ___ ___ ___ ___")
  print(r" | _ \ __/ __|_ _| _ \ __|  _ __ _  _")
  print(r" |   / _| (__ | ||  _/ _| _| '_ \ || |")
  print(r" |_|_\___\___|___|_| |___(_) .__/\_, |")
  print(r"                           |_|   |__/")


def main() :

  title()
  
  # GETTING INPUTS

  r_ = str(input("Choose a recipe: "))
  amount = int(input("Choose an amount: "))
  

  # RECIPE CHECK

  # (0) RANDOM
  
  if r_ == "" or r_ == "0" :
    r_ = str(random.randint(1, r_max))
    
    
  # (1) PIZZA

  if r_ == "pizza" or r_ == "1" :
    r_title = "PIZZA"
    r_time = 60
    ingredients = ["flour " + str(amount * 110) + "g", "salt " + str(amount * 2) + "g", "baking powder " + str(amount * 2.5) + "g", "water " + str(amount * 60) + "g", "oil " + str(amount * 10) + "g"]

        
        
  # PRINTING RECIPE

  print()
  print(r_title)
  print("time : " + str(r_time) + "minutes")
  print("ingredients :")
  print()

  for i in ingredients:
    print("  - " + i)
  
  print()
    
  if str(input("restart? (Y/n) : ")) == "" or "y" or "Y" :
    os.system('cls||clear')
    main()
  else : 
    sys.exit()
      
   
   
# EXECUTION
 
main()    