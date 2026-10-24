# characters.py
# Name: Wasif Islam
# Description: Hero and Monster classes for a turn-based battle game

import random


class Character:
    """Shared stats and actions for anyone who can fight."""

    def __init__(self, name, description, maxHealth, weaponName, weaponDamage):
        self.__name = name
        self.__description = description
        self.__maxHealth = maxHealth
        self.__health = maxHealth
        self.__weaponName = weaponName
        self.__weaponDamage = weaponDamage
        self.__defending = False

    def getName(self):
        return self.__name

    def getDescription(self):
        return self.__description

    def getHealth(self):
        return self.__health

    def getMaxHealth(self):
        return self.__maxHealth

    def getWeaponName(self):
        return self.__weaponName

    def getWeaponDamage(self):
        return self.__weaponDamage

    def isDefending(self):
        return self.__defending

    def setDefending(self, value):
        self.__defending = value

    def isAlive(self):
        return self.__health > 0

    def takeDamage(self, damage):
        # Defending cuts the hit in half, then the shield drops
        if self.__defending:
            damage = damage // 2
            self.__defending = False
        self.__health -= damage
        if self.__health < 0:
            self.__health = 0
        return damage

    def heal(self, amount):
        self.__health += amount
        if self.__health > self.__maxHealth:
            self.__health = self.__maxHealth

    def attack(self, other):
        # Damage varies a little each hit so fights don't play out the same
        damage = random.randint(self.__weaponDamage // 2, self.__weaponDamage)
        return other.takeDamage(damage)


class Hero(Character):
    """The player. Can attack, defend, or drink a potion."""

    def __init__(self, name, description, maxHealth, weaponName,
                 weaponDamage, potions=2):
        super().__init__(name, description, maxHealth, weaponName, weaponDamage)
        self.__potions = potions

    def getPotions(self):
        return self.__potions

    def drinkPotion(self):
        if self.__potions == 0:
            return False
        self.__potions -= 1
        self.heal(30)
        return True


class Monster(Character):
    """The enemy. Picks its own move each turn."""

    def chooseMove(self):
        # Mostly attacks, sometimes defends
        if random.random() < 0.75:
            return "attack"
        return "defend"
