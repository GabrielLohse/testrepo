import os
import readchar
import random

#Main_menu
title = "!Bienvenido a nuestra mazmorra Pikachu vs 5 Charmanders"

print("\n" + title + "\n" + "-" * len(title) + "\n")
print("Recuerda tener las mayusculas activadas para poder jugar...\n")
print("Si quieres salir del juego puedes precionar Q \n")
input("Presiona cualquier tecla para empezar ")

#Constants

MAP_WIDTH = 20
MAP_HEIGHT = 15
POS_X = 0
POS_Y = 1

#Variables

obstacle_definition = """\
####################
#   #####   ####   #
#                  #
#   ######### ##   #
############# ######
############   #####
############   #####
######         #####
###### #############
#####   ############
#####   ############
#####            ###
##############   ###
##############   ###
####################\
"""


my_position = [10,1]
combat_1 = [[2,2],[17,2],[13,6],[6,10],[15,12]]
end_game = False
start_combat = False
end_combat = False
combat_in_cell = None

#create obstacle map
obstacle_definition = [list(row) for row in obstacle_definition.split("\n")]

while not end_game:

    while not start_combat:

        #Draw map

        print("+" + "-" * MAP_WIDTH * 3 + "+")

        for coordinate_y in range(MAP_HEIGHT):
            print("|", end="")

            for coordinate_x in range(MAP_WIDTH):

                char_to_draw = "   "

                for enemies in combat_1:
                    if enemies[POS_X] == coordinate_x and enemies[POS_Y] == coordinate_y:
                        char_to_draw = "(-)"

                if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:
                    char_to_draw = "(^)"

                if obstacle_definition[coordinate_y][coordinate_x] == "#":
                    char_to_draw = "###"

                for combats in combat_1:
                    if my_position[POS_X] == combats[POS_X] and my_position[POS_Y] == combats[POS_Y]:
                        combat_in_cell = combats
                        start_combat = True

                print("{}".format(char_to_draw),end="")

            print("|")

        print("+" + "-" * MAP_WIDTH * 3 + "+")

        #Move

        direction = readchar.readchar()
        new_position = None

        if direction == "W":
            new_position =  [my_position[POS_X],  (my_position[POS_Y] - 1) % MAP_HEIGHT]

        elif direction == "S":
            new_position =  [my_position[POS_X],  (my_position[POS_Y] + 1) % MAP_HEIGHT]

        elif direction == "A":
            new_position =  [(my_position[POS_X] - 1) % MAP_WIDTH,  my_position[POS_Y]]

        elif direction == "D":
            new_position =  [(my_position[POS_X] + 1) % MAP_WIDTH,  my_position[POS_Y]]

        if new_position:
            if obstacle_definition[new_position[POS_Y]][new_position[POS_X]] != "#":
                my_position = new_position

        elif direction == "Q":
            exit()

        os.system("cls")

    #Combat

    TOTAL_HEALTH_CHARMANDER = 80
    TOTAL_HEALTH_PIKACHU = 90

    LONG_OF_HEALTH_BAR = 20

    charmander_health = TOTAL_HEALTH_CHARMANDER
    pikachu_health = TOTAL_HEALTH_PIKACHU

    while not end_combat:

        #Charmander's Turn
        if charmander_health > 0:
            print("Turno de Charmander")
            charmander_attack = random.randint(1, 2)
            if charmander_attack == 1:
                #Placaje Ardiente
                print("Charmander ataca con Placaje Ardiente")
                pikachu_health -= 20
            else:
                #Destrucción Abrasadora
                print("Charmander ataca con Destrucción Abrasadora")
                pikachu_health -= 22

            if pikachu_health < 0:
                pikachu_health = 0

            charmander_life_bar = int(charmander_health * LONG_OF_HEALTH_BAR / TOTAL_HEALTH_CHARMANDER)
            print("Charmander:  [{}{}] ({}/{})".format("*" * charmander_life_bar, " " * (LONG_OF_HEALTH_BAR - charmander_life_bar)
                                                      , charmander_health, TOTAL_HEALTH_CHARMANDER))

            pikachu_life_bar = int(pikachu_health * LONG_OF_HEALTH_BAR / TOTAL_HEALTH_PIKACHU)
            print("Pikachu:     [{}{}] ({}/{})".format("*" * pikachu_life_bar, " " * (LONG_OF_HEALTH_BAR - pikachu_life_bar)
                                                      , pikachu_health, TOTAL_HEALTH_PIKACHU))

            input("Enter para continuar...\n\n")
            os.system("cls")

        #Pikachu's Turn
        if pikachu_health > 0:
            print("Turno Pikachu")

            pikachu_attack = None
            while pikachu_attack not in ["B","R","O","S"]:
                pikachu_attack = input("¿Qué ataque deseas realizar? [B]ola voltio, [R]ayo, [O]nda trueno, [S]altar turno: ")

            if pikachu_attack == "B":
                print("Pikachu ataca con Bola voltio\n")
                charmander_health -= 20
            elif pikachu_attack == "R":
                print("Pikachu ataca con Rayo\n")
                charmander_health -= 24
            elif pikachu_attack == "O":
                print("Pikachu ataca con Onda trueno\n")
                charmander_health -= 18
            elif pikachu_attack == "S":
                print("Pasaste el turno...\n")

            if charmander_health < 0:
                charmander_health = 0

            charmander_life_bar = int(charmander_health * LONG_OF_HEALTH_BAR / TOTAL_HEALTH_CHARMANDER)
            print("Charmander:  [{}{}] ({}/{})".format("*" * charmander_life_bar, " " * (LONG_OF_HEALTH_BAR - charmander_life_bar)
                                                      ,charmander_health,TOTAL_HEALTH_CHARMANDER))

            pikachu_life_bar = int(pikachu_health * LONG_OF_HEALTH_BAR / TOTAL_HEALTH_PIKACHU)
            print("Pikachu:     [{}{}] ({}/{})".format("*" * pikachu_life_bar, " " * (LONG_OF_HEALTH_BAR - pikachu_life_bar)
                                                      ,pikachu_health,TOTAL_HEALTH_PIKACHU   ))

            input("Enter para continuar...\n\n")

        if pikachu_health == 0:
            end_combat = True
            os.system("cls")
            print("Charmander gana el combate! Suerte la proxima vez...")
            input("Presiona Enter para salir...")
            exit()

        elif charmander_health == 0:
            end_combat = True
            os.system("cls")
            print("Pikachu gana el combate!")

    combat_1.remove(combat_in_cell)
    start_combat = False
    end_combat = False

    if not combat_1:
        end_game = True
        os.system("cls")

print("Felicidades ganaste! Has vencido a todos los entrenadores Pokemon\n")
input("Presiona Enter para salir...")
exit()
