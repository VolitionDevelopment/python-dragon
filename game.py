import random

from entities.impl.hero import Hero

import menu
from entities.impl.dragon import Dragon

dragon = Dragon()
hero = Hero(raw_input("You've encountered a dragon! Quick, what's your name?! "))

main_menu = menu.Menu([
    menu.Option("Fight", lambda: hero.attack(dragon, "You struck " + dragon.name + " with your mighty sword!")),
    menu.Option("Use Item", lambda: get_input(item_menu)),
    menu.Option("Use Spell", lambda: get_input(spell_menu)),
    menu.Option("Flee", lambda: flee())
])

spell_menu = menu.Menu([])
item_menu = menu.Menu([])


def flee():
    print "You flee you COWARD! YOU'RE A CHICKENBUTT!!!"
    exit(0)


def start():
    spell_menu.options.append(menu.Option(hero.spells[0].name, lambda: hero.spells[0].fire(hero, dragon)))
    spell_menu.options.append(menu.Option(hero.spells[1].name, lambda: hero.spells[1].fire(hero, dragon)))
    spell_menu.options.append(menu.Option(hero.spells[2].name, lambda: hero.spells[2].fire(hero, dragon)))

    item_menu.options.append(menu.Option(hero.items[0].name, lambda: hero.items[0].use(hero)))
    item_menu.options.append(menu.Option(hero.items[1].name, lambda: hero.items[1].use(hero)))

    print "So your name is %s, eh? Not such a heroic name, but whatever. Draw your sword!\n" % hero.name

    while hero.health > 0:

        hero.show_status()
        print "\n"
        dragon.show_status()
        get_input(main_menu)

        if dragon.health <= 0:
            break
        else:
            dragon.attack(hero, "The Dragon struck you with it's mighty claws!")

    if hero.health <= 0:
        print "You died."
        exit(0)
    else:
        print "You slew the dragon!!"
        exit(0)


def get_input(menu):
    selection = raw_input(menu.print_menu())

    if selection == "back":
        return False

    for o, option in enumerate(menu.options):
        if option.title == selection:
            if not option.execute():
                get_input(menu)
            return True

    print "Sorry, I didn't get that."
    get_input(menu)


start()
