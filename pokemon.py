from enum import Enum
import random

# https://docs.python.org/3.11/howto/enum.html
# TODO add more pokemons
class Pokedex(Enum):
    Bulbasaur = 1
    Ivysaur = 2
    Venusaur = 3
    Charmander = 4
    Charmeleon = 5
    Charizard = 6
    Squirtle = 7
    Wartortle = 8
    Blastoise = 9
    Caterpie = 10
    Metapod = 11
    Butterfree = 12 

# There are 18 official types of Pokémons:
# https://pokemon.fandom.com/wiki/Types
class PokeTypes(Enum):
    NORMAL = 0
    FIRE = 1
    WATER = 2 
    GRASS = 3
 
# Ref https://www.w3schools.com/python/python_classes.asp
# Ref https://docs.python.org/3.11/howto/enum.html
# Ref https://blog.glugmvit.com/oops/
class Pokemon:
    def __init__(self, name, types, health, attack, defence):
        self.name = name
        # version 1: One pokemon can get only ONE type
        # TODO version 2: One pokemon can get more than one type
        self.types = types
        self.health = health

        # TODO add energy (for charged moves)
        # TODO add fast move, 1st, 2nd charged moves
        self.attack = attack
        self.defence = defence 

    def printPokemon(self):
        print("Name:", self.name)
        print("Type:", self.types)
        print("Health:", self.health)
        print("Attack: ", self.attack)
        print("Defence: ", self.defence)
    
    def getName(self):
        return self.name 
    def getType(self):
        return self.types
    def getHealth(self):
        return self.health
    def getAttack(self):
        return self.attack
    def getDefence(self):
        return self.defence

    def setName(self, x):
        self.name = x 
    def setTypes(self, x):
        self.types = x
    def setHealth(self, x):
        self.health = x
    def setAttack(self, x):
        self.attack = x
    def setDefence(self, x):
        self.defence = x 

    def isAlive(self):
        return self.health > 0
    def isDead(self):
        return not self.isAlive()

    # TODO Pokemon 1 attack pokemon 2 until one of them is out of health
    # def attack(Pokemon p1, Pokemon p2)

# pokemon 1 attacks pokemon 2 ONE time
# version 1: without considering Pokemon type effectiveness
# TODO version 2: consider Pokemon type effectiveness https://pokemondb.net/type
# TODO consider p1 health >= 0. Is it dead?
# def singlePokeFight(Pokemon p1, Pokemon p2):
def singlePokeFight(p1, p2):
    p1.pokeTYPES = self.types
    p2.pokeTYPeS = self.types 

    if p1.pokeTYPES == "FIRE" and p2.pokeTYPES == "GRASS":
        gross_damage1 = gross_damage1*2
        gross_damage2 = gross_damage2/2

    elif p1.pokeTYPES == "FIRE" and p2.pokeTYPES == "FIRE":
        gross_damage1 = gross_damage1/2
        gross_damage2 = gross_damage2/2

    elif p1.pokeTYPES == "FIRE" and p2.poketypes == "WATER":
        gross_damage1 == gross_damage1/2
        gross_damage2 == gross_damage2*2

    elif p1.pokeTYPES == "WATER" and p2.pokeTYPES == "FIRE":
        gross_damage1 = gross_damage1*2
        gross_damage2 = gross_damage2/2

    elif p1.pokeTYPES == "WATER" and p2.pokeTYPES == "WATER":
        gross_damage1 = gross_damage1/2
        gross_damage2 = gross_damage2/2

    elif p1.pokeTYPES == "WATER" and p2.pokeTYPES == "GRASS":
        gross_damage1 = gross_damage1/2
        gross_damage2 = gross_damage2*2

    elif p1.pokeTYPES == "GRASS" and p2.pokeTYPES == "WATER":
        gross_damage1 = gross_damage1*2
        gross_damage2 = gross_damage2/2

    elif p1.pokeTYPES == "GRASS" and p2.pokeTYPES == "GRASS":
        gross_damage1 = gross_damage1/2
        gross_damage2 = gross_damage2/2

    elif p1.pokeTYPES == "GRASS" and p2.pokeTYPES == "FIRE":
        gross_damage1 = gross_damage1/2
        gross_damage2 = gross_damage2*2

    else:
        gross_damage1 = gross_damage1
        gross_damage2 = gross_damage2
        
    gross_damage1 = p2.getAttack() - p1.getDefence()
    if gross_damage1 > 0:
        poke1health = p1.getHealth() - gross_damage1
    else:
        poke1health = p1.getHealth() - 1
    
    gross_damage2 = p1.getAttack() - p2.getDefence()
    if gross_damage2 > 0:
        poke2health = p2.getHealth() - gross_damage2
    else:
        poke2health = p2.getHealth() - 1 
    
    if poke1health > 0:
        p1.setHealth(poke1health)
    else:
        p1.setHealth(0)
    
    if poke2health > 0:
        p2.setHealth(poke2health)
    else:
        p2.setHealth(0)
    
    print("Attacker Health | Defender Health : " + str(p1.getHealth()) + "|" + str(p2.getHealth()))
    return 0

def PokeFight(p1, p2):

    
    while p1.isAlive() and p2.isAlive():
        singlePokeFight(p1, p2)

    
    if p1.isAlive() and p2.isAlive():
        # draw
        print(p1.getName() + " draws " + p2.getName())
        return 2
    elif p1.isAlive():
        # p1 won
        print(p1.getName() + " won " + p2.getName())
        return 0
    else:
        # p2 won
        print(p2.getName() + " won " + p1.getName())
        return 1

class PokemonVillains:
    teamName = 'siu'
    def __init__(self, Name):
        self.Name = Name
    def __init__(self, Name, boss1, boss2, boss3):
        self.Name = Name 
        self.boss1 = boss1 
        self.boss2 = boss2
        self.boss3 = boss3 

# Villains fight
def singleVillainFight(v1, v2):
    return 

# Villains fight
def VillainFight(v1, v2):
    return 

#counter



yourPokemonName = input("input your pokemon name ")
yourPokemonElement = random.choice("FIRE", "WATER", "GRASS")








boss1 = Pokemon("Charmander", pokeTYPES.FIRE, 50, 50, 50)
boss2 = Pokemon("Squirtle", pokeTYPES.WATER, 60, 60, 60)
boss3 = Pokemon("Bulbasaur", pokeTYPES.GRASS, 100, 100, 100)
