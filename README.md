# ⚔️ Monster Battle

> 🎓 Made during lab for **CS 172** at **Drexel University**

A turn-based battle game in the terminal. You name your hero, then fight your way through a Goblin, a Troll, and a Dragon, each tougher than the last. Pick your moves carefully: potions are limited, and the Dragon hits hard.

## How to play

Each turn you choose one move:

| Move | What it does |
|---|---|
| **(a)ttack** | Hit the monster with your sword. Damage varies a little each swing. |
| **(d)efend** | Raise your shield, so the next hit you take does half damage |
| **(p)otion** | Heal 30 HP (you start with 2) |

A coin flip decides who goes first in each fight. Monsters mostly attack, but sometimes they brace and block your next hit. After each win you rest and recover a bit of health before the next monster shows up.

## Sample run

```
=== A wild Goblin appears! ===
A sneaky little thief with a rusty dagger.
Goblin goes first.
Goblin is bracing for your next attack.

Wasif: 120/120 HP  |  Goblin: 60/60 HP

Your move: (a)ttack, (d)efend, (p)otion [2 left]
> a
Wasif hits Goblin with the Sword for 8 damage!
Goblin attacks with its Rusty Dagger for 6 damage!
```

## How it's built

- **`Character`**: the base class with health, a weapon, attacking, defending, and taking damage. All stats are private with getters.
- **`Hero`** extends `Character` and adds potions.
- **`Monster`** extends `Character` and picks its own move each turn.

`main.py` runs the fights one after another and handles the turn loop.

## Run it

```bash
python main.py
```

No extra libraries needed.

## Built with

Python · classes and inheritance
