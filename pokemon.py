#pokemon names have capital letters
#element names don't have capital letters

import random



z = 0 

pokemon = input("Choose the name of your pokemon: ")
print("Your pokemon is", pokemon)

element = input("Choose the element of your pokemon (fire, water, grass): ")

if element == "fire":

    element == "fire"

elif element == "water":

    element == "water"

elif element == "grass":

    element == "grass"

else: 
    print("Capital letters sensitive")
    exit()

pokemonH = 100
pokemonAtk = 100
pokemonDef = 50

print("Your pokemon will start with 100 hp, 100 attack, 50 defense.")
stats = random.randrange(10, 21)
print("You have", stats, "stats, you can upgrade", stats, "time")


while stats != 0:
    upg = input("What do you want to upgrade (def, atk, hp)?")

    if upg == "def":
        pokemonDef = pokemonDef + 10
        print("Your defense is now", pokemonDef)
        stats = stats - 1
        print("you have", stats, "stats left")

    elif upg == "atk":
        pokemonAtk = pokemonAtk + 10
        print("Your attack is now", pokemonAtk)
        stats = stats - 1
        print("you have", stats, "stats left")

    elif upg == "hp":
        pokemonH = pokemonH + 10
        print("Your hp is now", pokemonH)
        stats = stats - 1
        print("you have", stats, "stats left")

    else:
        print("Please input def, atk, or hp. This is case sensitive. ")



class Pokemon:
    def __init__(self, name, types, health, attack, defense):
        self.name = name
        self.types = types
        self.health = health
        self.attack = attack
        self.defense = defense 

    def getPokemon(self):
        print("Name:", int(self.name))
        print("Type:", int(self.types))
        print("Health:", int(self.health))
        print("Attack: ", int(self.attack))
        print("Defense: ", int(self.defense))

p1 = Pokemon("Bulbasaur", "grass", 45, 49, 49)
p4 = Pokemon("Charmander", "fire", 39, 52, 43)
p7 = Pokemon("Squirtle", "water", 44, 48, 65)



attackName = input("input your pokemon's attack name: ")

print("You will now fight the first boss, Bulbasaur")
print(pokemon, "fights", "Bulbasaur")

while p1.health > 0:
    b1Fight = input("Do you want to attack or increase your health by 50? (atk, hp)? ")

    if b1Fight == "atk":
        p1.health = p1.health - pokemonAtk
        print("Bulbasaur's health is now", p1.health)

    elif b1Fight == "hp":
        pokemonH = pokemonH + 50
        print("your pokemon's health is now", pokemonH)
    else:
        print("Please input valid option. This is case sensitive. ")












