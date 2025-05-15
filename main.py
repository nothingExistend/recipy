import random

recipe_max = 1 #ERHÖHEN WENN MEHR REZEPTE ADDED

def title() :
  print("  ___ ___ ___ ___ ___ ___")
  print(" | _ \ __/ __|_ _| _ \ __|  _ __ _  _")
  print(" |   / _| (__ | ||  _/ _| _| '_ \ || |")
  print(" |_|_\___\___|___|_| |___(_) .__/\_, |")
  print("                           |_|   |__/")



# PRINTING TITLE

title()

# GETTING INPUTS

r_input = [input("Choose a recipe: "), int(input("Choose an amount: "))]
amount = r_input[1]

# RECIPE CHECK

# (0) RANDOM RECIPE

if r_input[0] == "" or r_input == 0:
  random.randint(0, recipe_max)

# (1) PIZZA
print(r_input)
if r_input[0] == "pizza" or r_input == 1:
  r_title = "Pizza"
  recipe_time = 60
  ingredients = ["Mehl " + str(r_input[1] * 110) + "g", "Salz " + str(r_input[1] * 2) + "g", "Backpulver " + str(r_input[1] * 2.5) + "g", "Wasser " + str(r_input[1] * 60) + "g", "Öl " + str(r_input[1] * 10) + "g"]

# PRINTING RECIPE

print("You'll need:")

for i in ingredients:
  print(i)
  