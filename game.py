from dragon import Dragon
from hero import Hero
import menu
import random

dragon = Dragon()
hero = Hero(raw_input("You've encountered a dragon! Quick, what's your name?! "))

main_menu = menu.Menu([
    menu.Option("Fight", lambda: hero.attack(dragon)),
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
    for spell in hero.spells:
        spell_menu.options.append(menu.Option(spell.name, lambda: spell.fire(hero, dragon)))

    for item in hero.inventory:
        item_menu.options.append(menu.Option(item.name, lambda: item.use(hero)))

    print "So your name is ", hero.name, ", eh? Not such a heroic name, but whatever. Draw your sword!"

    spell_menu.options[0].execute()
    print spell_menu.options[0].title

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
                print "Didn't work"
                get_input(menu)
            return True

    print "You dun messed up A-A-RON!"
    get_input(menu)

start()
