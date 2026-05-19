import random

# Tuple (Game Rules)
rules = ("There are 3 boxes: A, B, C", "Only one box has treasure", "Choose wisely to win", "You cannot choose the same box twice")

print("🎮 Welcome to Treasure Box Challenge!") 
print("\nGame Rules:") 
for rule in rules: 
    print("-", rule)

# List (Boxes)
boxes = ["A", "B", "C"]

# Secret Treasure Box (String)
secret_box = random.choice(boxes)

# Set (Store chosen boxes)
chosen_boxes = set()

# Dictionary (Game conditions)
conditions = {"valid_choice": False, "already_chosen": False, "win": False}

# Game Loop
while True: 
    choice = input("\nChoose a box (A/B/C): ").upper()
    
    # Reset conditions
    conditions["valid_choice"] = False
    conditions["already_chosen"] = False
    conditions["win"] = False
    
    # Check valid choice
    if choice in boxes:
        conditions["valid_choice"] = True
    else:
        print("Invalid choice! Choose A, B, or C.")
        continue
        
    # Check already chosen
    if choice in chosen_boxes:
        conditions["already_chosen"] = True
        print(" You already opened this box!")
        continue
    else:
        chosen_boxes.add(choice)
        
    # Check win
    if choice == secret_box:
        conditions["win"] = True
        
    # Decision
    if conditions["win"]:
        print("💎 Congratulations! You found the treasure!")
        print("Treasure was in box:", secret_box)
        break
    else:
        print("💀 Oh no! This box had a trap!")
        
        # If all boxes opened
        if len(chosen_boxes) == 3:
            print("💀 Game Over! All boxes opened.")
            print("Treasure was in box:", secret_box)
            break
            
        print("Opened boxes so far:", chosen_boxes)