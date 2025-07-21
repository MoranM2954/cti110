# Maria Moran
# July 13, 2025
# P5HW
# Design a game of your own choosing. 

import random

# function to create a player with a given name
def create_player(name):
    return {
        "name": name,
        "gold": 10,
        "inventory": []
    }
# Dictionary with ingredients, emoji's and values
INGREDIENTS = { 
    "Mandrake Root 🫚": 3,
    "Dragon Scale 🐉": 5,
    "Elf Leaf 🍂": 2,
    "Phoenix Feather 🐦‍🔥": 7,
    "Goblin Earwax 👺": 1
}
# function to gather ingredients
def gather_ingredients():
    items = list(INGREDIENTS.keys())
    found = random.choice(items)
    print(f"You found a {found}!")
    return found
# function to craft potion with ingredients in inventory
def craft_potion(inventory):
    if len(inventory) < 2:
        print("You need at least two ingredients to craft potion.")
        return 0
    potion_value = sum(INGREDIENTS.get(item, 1) for item in inventory)
    print(f"🪄 You crafted a potion worth {potion_value} gold! 💰")
    return potion_value

# function is the start of main game, prompts, explains goal and sets parameter of 5 rounds to play.
def main():
    name = input("Welcome, apprentice!🧙 Your goal is to gather as much goal before the end of 5 rounds. What is your name?")
    player = create_player(name)
    rounds = 5
# Loop through each round
    for round_num in range(1, rounds + 1):
        print(f"\n------- 💐 Round {round_num} 💐-------")
        print(f"{player['name']}'s gold: {player['gold']}")
        print(f"Inventory: {player['inventory']}")
        print("Choose an action:")
        print("1. Gather ingredients to add to your inventory.")
        print("2. Craft potion using your ingredients to increase its value.")
        print("3. Sell potion or ingredients to earn the most gold.")

        choice = input("Enter choice (1/2/3): ")

        if choice == "1":
            ingredient = gather_ingredients()
            player["inventory"].append(ingredient)

        elif choice == "2":
            value = craft_potion(player["inventory"])
            if value > 0:
                player["inventory"].clear()

        elif choice == "3":
            if not player["inventory"]:
                print("You have nothing to sell!")
            else:
                value = sum(INGREDIENTS.get(item, 1) for item in player["inventory"])
                print(f"You sold your ingredients for {value} gold! 💰 ")
                player["gold"] += value
                player["inventory"].clear()    
        else:
            print("Invalid choice!")
        
    print(f"\n Game Over! {player['name']} ended with {player['gold']} gold. 💰")

  # call main      
if __name__ == "__main__":
        main()       

        

