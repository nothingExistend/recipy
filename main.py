import random, time, os, itertools

r_max = 2 #ERHÖHEN WENN MEHR REZEPTE ADDED
spinner = itertools.cycle(['|', '/', '-', '\\'])

def title() :
    print(r" ______     ______     ______     __     ______   __  __    ")
    print(r"/\  == \   /\  ___\   /\  ___\   /\ \   /\  == \ /\ \_\ \   ")
    print(r"\ \  __<   \ \  __\   \ \ \____  \ \ \  \ \  _-/ \ \____ \  ")
    print(r" \ \_\ \_\  \ \_____\  \ \_____\  \ \_\  \ \_\    \/\_____\ ")
    print(r"  \/_/ /_/   \/_____/   \/_____/   \/_/   \/_/     \/_____/ ")
    print()

def ERROR(error): #
    if error == "no_recipe":
        error_text = f"\r ERROR: 'no_recipe' couldn't find recipe with name: {recipe}, please check your spelling"
        
    if error == "test":
        error_text = f"this is a TEST-ERROR: recipe: {recipe}; amount: {amount}; r_title: {r_title}; r_time: {r_time}"
        
    print("if the ERROR keeps ocuring open an issue under: 'github.com/nothingExistend/recipy'")


def main() :

    title()

    # GETTING INPUTS

    recipe = str(input("Choose a recipe: "))
    amount = int(input("Choose an amount: "))


    # RECIPE CHECK

    # (0) RANDOM

    if recipe in ["", "0", "random"]:
        recipe = str(random.randint(1, r_max))

    # (1) PIZZA

    if recipe in ["pizza", "1"]:
        r_title = "PIZZA"
        r_time = 60
        ingr = [f"flour {amount * 110} g", f"salt {amount * 2} g", f"baking powder {amount * 2.5} g", f"water {amount * 60} ml", f"oil {amount * 10} ml"]
        instr = ["mix dry ingredients in a container", "mix fluids in a separate container", "mix mixes to get homogeneous dough", "split in portions, let them rest for 10 mins", "put toppings on", "oven for ~15 mins & 200°C"]

    # (2) PANCAKES

    if recipe in ["pancake", "pancakes", "2"]:
        r_title = "PANCAKES (amount 1 = 2 portions)"
        r_time = 30
        ingr = [f"flour (sifted) {amount * 250} g", f"egg {amount * 1}", f"milk {amount * 350} ml", f"baking powder {amount * 10} g", f"oil {amount * 60} ml", f"salt {amount * 2.5} g"]
        instr = ["mix dry ingredients in a container", "mix fluids in seperate container", "pour fluids in dry ingredient container", "mix fast until no clumps are left", "put a little bit oil in a pan", "put two scoops of dough in the pan", "when bubbles pop look whether underside is brown then turn on other side"]    
        
    # PRINTING RECIPE

    print()
    print(r_title)
    print(f" - time : {r_time} mins")
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

    restart = input("restart? (Y/n) : ")
    if restart in ["y","Y"]:
        os.system('cls')
        main()
    else:
        for _ in range(20):
            print(f'\r closing {next(spinner)}', end='', flush=True)
            time.sleep(0.1)



# EXECUTION

main()    
