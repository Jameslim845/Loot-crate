import random
crate_tier = input("Do you want to open a normal or premium crate? ")
loot = int(input("how many loot boxes do you want to open? "))
def tier_1():
  for i in range(loot):
    rarity = random.randint(1,100)
    if rarity <= 50:
      common_items = random.choice(["Lucky ladel", "Shitty spoon", "Sword"])
      print("You have received " + str(common_items) + " - Common")
    elif 50 < rarity < 75:
      uncommon_items = random.choice(["Ak-47", "Minigun", "Ray gun"])
      print("You have received " + str(uncommon_items) + " - Uncommon")

    elif 75 < rarity < 90:
      rare_items = random.choice(["Falchion", "The Stick of Truth", "Sword of Serios"])
      print("You have received " + str(rare_items) + " - Rare")
    elif 90 < rarity < 98:
      epic_items = random.choice(["Sword of the Creator", "BFG", "Estus Flask"])
      print("You have received " + str(epic_items) + " - Epic")

    elif 98 < rarity < 100:
      legendary_items = random.choice(["Excaliber", "Buster Sword", "Gay Hands", "Helicopter blade"])
      print("You have received " + str(legendary_items) + " - Legendary")
def tier_2():
    for i in range(loot):
      rarity = random.randint(1,100)
    if rarity <= 20:
      common_items = random.choice(["Lucky ladel", "Shitty spoon", "Sword"])
      print("You have received " + str(common_items) + " - Common")
    elif 20 < rarity < 40:
      uncommon_items = random.choice(["Ak-47", "Minigun", "Ray gun"])
      print("You have received " + str(uncommon_items) + " - Uncommon")

    elif 40 < rarity < 70:
      rare_items = random.choice(["Falchion", "The Stick of Truth", "Sword of Serios"])
      print("You have received " + str(rare_items) + " - Rare")
    elif 70 < rarity < 90:
      epic_items = random.choice(["Sword of the Creator", "BFG", "Estus Flask"])
      print("You have received " + str(epic_items) + " - Epic")

    elif 90 < rarity < 100:
      legendary_items = random.choice(["Excaliber", "Buster Sword", "Gay Hands", "Helicopter blade"])
      print("You have received " + str(legendary_items) + " - Legendary")
while loot != 0:
  if crate_tier == "normal":
    loot - 1
    tier_1()
  elif crate_tier == "premium":
    loot - 1
    tier_2()
while True:
  crate = input("Do you want to continue? ")
  crate_tier = input("Do you want to open a normal or premium crate? ")
  loot = int(input("how many loot boxes do you want to open? ")) 
  if crate == "normal" and crate == "yes":
    loot = int(input("how many loot boxes do you want to open? "))
    tier_1()  
  elif crate == "premium" and crate == "yes":
    loot = int(input("how many loot boxes do you want to open? "))
    tier_2()
 
