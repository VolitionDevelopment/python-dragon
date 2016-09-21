from dragon import Dragon
from hero import Hero
import menu
import random

dragon = Dragon()
hero = Hero(raw_input("You've encountered a dragon! Quick, what's your name?! "))

main_menu = menu.Menu([
    menu.Option("Fight", lambda: hero.attack(dragon)),
    menu.Option("Use Item", lambda: hero.use_potion()),
    menu.Option("Use Spell", lambda: hero.spell(dragon)),
    menu.Option("Flee", lambda: flee())
])

spell_menu = menu.Menu([

])


def flee():
    print "You flee you COWARD! YOU'RE A CHICKENBUTT!!!"
    exit(0)


def start():
    print "So your name is ", hero.name, ", eh? Not such a heroic name, but whatever. Draw your sword!"

    while hero.health > 0 and dragon.health > 0:
        hero.show_status()
        dragon.show_status()
        get_input(main_menu)

        if dragon.health <= 15 and dragon.mana >= 5 and random.randrange(1, 10) > 7:
            dragon.heal()
        elif dragon.mana >= 5 and random.randrange(1, 10) > 7:
            dragon.breathe_fire(hero)
        else:
            dragon.attack(hero)

    if hero.health <= 0:
        print "You died."
        exit(0)
    else:
        print "You slew the dragon!!"
        exit(0)


def get_input(menu):
    selection = raw_input(menu.print_menu())

    for o, option in enumerate(menu.options):
        if option.title == selection:
            if not option.execute():
                get_input(menu)
            return

    print "You dun messed up A-A-RON!"
    get_input(menu)

start()
