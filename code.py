import random
import sys
import os

r_max = 2 #ERHÖHEN WENN MEHR REZEPTE ADDED

def title() :
    print(r" ______     ______     ______     __     ______   __  __    ")
    print(r"/\  == \   /\  ___\   /\  ___\   /\ \   /\  == \ /\ \_\ \   ")
    print(r"\ \  __<   \ \  __\   \ \ \____  \ \ \  \ \  _-/ \ \____ \  ")
    print(r" \ \_\ \_\  \ \_____\  \ \_____\  \ \_\  \ \_\    \/\_____\ ")
    print(r"  \/_/ /_/   \/_____/   \/_____/   \/_/   \/_/     \/_____/ ")
    print()




def main() :

    title()

    # GETTING INPUTS

    r_ = str(input("Choose a recipe: "))
    amount = int(input("Choose an amount: "))


    # RECIPE CHECK

    # (0) RANDOM

    if r_ == "" or r_ == "0" or r_ == "random" :
        r_ = str(random.randint(1, r_max))

    # (1) PIZZA

    if r_ == "pizza" or r_ == "1" :
        r_title = "PIZZA"
        r_time = 60
        ingr = ["flour " + str(amount * 110) + "g", "salt " + str(amount * 2) + "g", "baking powder " + str(amount * 2.5) + "g", "water " + str(amount * 60) + "ml", "oil " + str(amount * 10) + "ml"]
        instr = ["mix dry ingredients in a container", "mix fluids in a separate container", "mix mixes to get homogeneous dough", "split in portions, let them rest for 10 mins", "put toppings on", "oven for ~15 mins & 200°C"]

    # (2) PANCAKES

    if r_ == "pancake" or r_ == "pancakes" or r_ == "2" :
        r_title = "PANCAKES (amount 1 = 2 portions)"
        r_time = 30
        ingr = ["flour (sifted) " + str(amount * 250) + "g", "egg " + str(amount * 1), "milk " + str(amount * 350) + "ml", "baking powder " + str(amount * 10) + "g", "oil " + str(amount * 60) + "ml", "salt " + str(amount * 2.5) + "g"]
        instr = ["mix dry ingredients in a container", "mix fluids in seperate container", "pour fluids in dry ingredient container", "mix fast until no clumps are left", "put a little bit oil in a pan", "put two scoops of dough in the pan", "when bubbles pop look whether underside is brown then turn on other side"]

    # (3) 

    # PRINTING RECIPE

    print()
    print(r_title)
    print(" - time : " + str(r_time) + "mins")
    print()
    print("ingredients :")
    print()

    for i in ingr:
        print("  - " + i)

    print()
    print("instructions : ")
    for i in instr :
        print("  - " + i)

    print()


    if str(input("restart? (Y/n) : ")) == "y" or "Y" :
        os.system('cls')
        main()
    else :
        sys.exit()



# EXECUTION

main()    
