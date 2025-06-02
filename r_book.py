import random
import sys

recipe_max = 1 #ERHÖHEN WENN MEHR REZEPTE ADDED

def title() :
  print("  ___ ___ ___ ___ ___ ___")
  print(" | _ \ __/ __|_ _| _ \ __|  _ __ _  _")
  print(" |   / _| (__ | ||  _/ _| _| '_ \ || |")
  print(" |_|_\___\___|___|_| |___(_) .__/\_, |")
  print("                           |_|   |__/")


# PRINTING TITLE

title()

def main() :

  # GETTING INPUTS

  r_ = str(input("Choose a recipe: "))
  amount = int(input("Choose an amount: "))

  # RECIPE CHECK

  # (0) RANDOM RECIPE

  if r_ == "" or r_ == "0":
    r_ = random.randint(0, recipe_max)

  # (1) PIZZA

  if r_ == "pizza" or r_ == "1":
    r_title = "Pizza"
    r_time = 60
    ingredients = ["Mehl " + str(amount * 110) + "g", "Salz " + str(amount * 2) + "g", "Backpulver " + str(amount * 2.5) + "g", "Wasser " + str(amount * 60) + "g", "Öl " + str(amount * 10) + "g"]

  # PRINTING RECIPE

  print()
  print(r_title)
  print("time : " + str(r_time))
  print("ingredients :")
  print()

  for i in ingredients:
    print("  - " + i)
    
    
  if str(input("restart? (y/n) : ")) == "" or "y" or "Y" :
    main()
  else : 
    sys.exit()
    
main()    