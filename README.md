# python-dragon
The dragon game written in Python

## Features
- Easily extendable code; make more items and spells quickly!
- Conforms to PEP8 standards
- Sarcasm
- Cool menu system
- Infinite potions! (Bug)

## How did I do this?
I tried to abstract all possible behavior. Each item inherits the Item class. Each entity inherits the Entity class. Each spell inherits the Spell class. When spells need custom behavior, I override the superclass's method. Simple and clean.
