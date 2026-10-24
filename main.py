# main.py
# Name: Wasif Islam
# Description: Runs a turn-based battle between the player's Hero and a Monster

import random
from characters import Hero, Monster

MONSTERS = [
    Monster("Goblin", "A sneaky little thief with a rusty dagger.", 60, "Rusty Dagger", 12),
    Monster("Troll", "Huge, slow, and very angry.", 100, "Club", 18),
    Monster("Dragon", "Breathes fire. Run if you can.", 140, "Fire Breath", 24),
]


def showHealth(hero, monster):
    print(hero.getName() + ": " + str(hero.getHealth()) + "/" + str(hero.getMaxHealth())
          + " HP  |  " + monster.getName() + ": " + str(monster.getHealth())
          + "/" + str(monster.getMaxHealth()) + " HP")


def heroTurn(hero, monster):
    while True:
        print("\nYour move: (a)ttack, (d)efend, (p)otion [" + str(hero.getPotions()) + " left]")
        choice = input("> ").strip().lower()
        if choice == "a":
            damage = hero.attack(monster)
            print(hero.getName() + " hits " + monster.getName() + " with the "
                  + hero.getWeaponName() + " for " + str(damage) + " damage!")
            return
        elif choice == "d":
            hero.setDefending(True)
            print(hero.getName() + " raises a shield. The next hit will do half damage.")
            return
        elif choice == "p":
            if hero.drinkPotion():
                print(hero.getName() + " drinks a potion and heals up.")
                return
            print("You're out of potions!")
        else:
            print("Type a, d, or p.")


def monsterTurn(monster, hero):
    if monster.chooseMove() == "attack":
        damage = monster.attack(hero)
        print(monster.getName() + " attacks with its " + monster.getWeaponName()
              + " for " + str(damage) + " damage!")
    else:
        monster.setDefending(True)
        print(monster.getName() + " is bracing for your next attack.")


def battle(hero, monster):
    print("\n=== A wild " + monster.getName() + " appears! ===")
    print(monster.getDescription())

    # Coin flip decides who goes first
    heroGoesFirst = random.choice([True, False])
    if heroGoesFirst:
        print(hero.getName() + " goes first.")
    else:
        print(monster.getName() + " goes first.")
        monsterTurn(monster, hero)

    while hero.isAlive() and monster.isAlive():
        print()
        showHealth(hero, monster)
        heroTurn(hero, monster)
        if monster.isAlive():
            monsterTurn(monster, hero)

    print()
    showHealth(hero, monster)
    if hero.isAlive():
        print("You defeated the " + monster.getName() + "!")
        return True
    print("The " + monster.getName() + " defeated you...")
    return False


def main():
    print("Welcome to Monster Battle!")
    name = input("What's your hero's name? ").strip() or "Hero"
    hero = Hero(name, "A brave adventurer.", 120, "Sword", 20)

    # Fight the monsters in order, from weakest to strongest
    for monster in MONSTERS:
        if not battle(hero, monster):
            print("\nGame over.")
            return
        hero.heal(25)
        print(hero.getName() + " rests and recovers a little health.")

    print("\nYou beat every monster. You win!")


if __name__ == "__main__":
    main()
