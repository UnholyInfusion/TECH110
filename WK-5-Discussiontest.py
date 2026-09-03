# Dinner Planner Program

print("=== Dinner Planner ===")

# User inputs
meal = input("What are you making for dinner? ")
protein = input("What is the main protein? ")
vegetable = input("What vegetable are you cooking? ")
side = input("What side dish are you making? ")

print("\nLet's start making dinner!")

# Step 1
ready = input("Have you gathered all of the ingredients? (yes/no): ").lower()

while ready != "yes":
    print("Please gather all of your ingredients before continuing.")
    ready = input("Are all the ingredients ready now? (yes/no): ").lower()

print("\nStep 1: Wash your hands.")

# Step 2
print(f"Step 2: Prepare the {protein}, {vegetable}, and {side}.")

# Step 3
cook = input(f"Is the {protein} fully cooked? (yes/no): ").lower()

while cook != "yes":
    print(f"Continue cooking the {protein}.")
    cook = input(f"Is the {protein} fully cooked now? (yes/no): ").lower()

print(f"\nStep 4: Cook the {vegetable}.")
print(f"Step 5: Prepare the {side}.")

taste = input("Does the meal need more seasoning? (yes/no): ").lower()

if taste == "yes":
    seasoning = input("What seasoning would you like to add? ")
    print(f"Add {seasoning} and stir well.")
else:
    print("No additional seasoning needed.")

print("\nStep 6: Plate the food.")

hungry = input("Is everyone ready to eat? (yes/no): ").lower()

if hungry == "yes":
    print(f"\nDinner is served! Enjoy your {meal}!")
else:
    print("\nKeep the food warm until everyone is ready.")

print("\nThanks for using the Dinner Planner!")