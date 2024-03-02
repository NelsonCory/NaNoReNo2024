# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
init python:
    #init python is run at initialization time, before the game loads.
    # use this for defining classes, functions, config variables, or persistent data
    class CharacterStats:
        def __init__(self, name, health, atkDamage, sprite):
            self.name = name
            self.health = health
            self.atkDamage = atkDamage
            self.sprite = sprite

        def attack(self,target):
            target.health -= self.atkDamage
    
    class Encounter:

        def __init__(self,playerList,enemyList):
            self.playerList = playerList
            self.enemyList = enemyList

       


    ThrokChar = CharacterStats(name="Throk",health=5,atkDamage=1,sprite="friend1.png")
    
    EnemyChar = CharacterStats(name="BadThrok",health=5,atkDamage=1,sprite="enemy1.png")
    EnemyChar2 = CharacterStats(name="BadThrok",health=5,atkDamage=1,sprite="enemy2.png")


define e = Character("Eileen")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    
    #jump debug

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.
    $friendList = [ThrokChar]
    $enemyList = [EnemyChar, EnemyChar2]
    call screen combat_screen

    return



label debug:

    call screen debug_screen