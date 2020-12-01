from time import sleep
import os
import random

class Battleship():
    def __init__(self):
        self.ship_counter_player_1 = 0
        self.ship_counter_player_2 = 0
        self.player_1_main_field =  [['~','~','~','~','~','~','~','~','~','~'],
                                    ['~','~','~','~','~','~','~','~','~','~'],
                                    ['~','~','~','~','~','~','~','~','~','~'],
                                    ['~','~','~','~','~','~','~','~','~','~'],
                                    ['~','~','~','~','~','~','~','~','~','~'],
                                    ['~','~','~','~','~','~','~','~','~','~'],
                                    ['~','~','~','~','~','~','~','~','~','~'],
                                    ['~','~','~','~','~','~','~','~','~','~'],
                                    ['~','~','~','~','~','~','~','~','~','~'],
                                    ['~','~','~','~','~','~','~','~','~','~'],
                                    ]
        self.player_1_shot_field = [['~','~','~','~','~','~','~','~','~','~'],
                                    ['~','~','~','~','~','~','~','~','~','~'],
                                    ['~','~','~','~','~','~','~','~','~','~'],
                                    ['~','~','~','~','~','~','~','~','~','~'],
                                    ['~','~','~','~','~','~','~','~','~','~'],
                                    ['~','~','~','~','~','~','~','~','~','~'],
                                    ['~','~','~','~','~','~','~','~','~','~'],
                                    ['~','~','~','~','~','~','~','~','~','~'],
                                    ['~','~','~','~','~','~','~','~','~','~'],
                                    ['~','~','~','~','~','~','~','~','~','~'],
                                    ]


        self.player_2_main_field = [['~','~','~','~','~','~','~','~','~','~'],
                                    ['~','~','~','~','~','~','~','~','~','~'],
                                    ['~','~','~','~','~','~','~','~','~','~'],
                                    ['~','~','~','~','~','~','~','~','~','~'],
                                    ['~','~','~','~','~','~','~','~','~','~'],
                                    ['~','~','~','~','~','~','~','~','~','~'],
                                    ['~','~','~','~','~','~','~','~','~','~'],
                                    ['~','~','~','~','~','~','~','~','~','~'],
                                    ['~','~','~','~','~','~','~','~','~','~'],
                                    ['~','~','~','~','~','~','~','~','~','~'],
                                    ]
        self.player_2_shot_field = [['~','~','~','~','~','~','~','~','~','~'],
                                    ['~','~','~','~','~','~','~','~','~','~'],
                                    ['~','~','~','~','~','~','~','~','~','~'],
                                    ['~','~','~','~','~','~','~','~','~','~'],
                                    ['~','~','~','~','~','~','~','~','~','~'],
                                    ['~','~','~','~','~','~','~','~','~','~'],
                                    ['~','~','~','~','~','~','~','~','~','~'],
                                    ['~','~','~','~','~','~','~','~','~','~'],
                                    ['~','~','~','~','~','~','~','~','~','~'],
                                    ['~','~','~','~','~','~','~','~','~','~'],
                                    ]

    def tittle_battleship(self):
        print('╔══╗─╔══╗╔════╗╔════╗╔╗──╔═══╗╔══╗╔╗╔╗╔══╗╔═══╗')
        sleep(0.5)
        print('║╔╗║─║╔╗║╚═╗╔═╝╚═╗╔═╝║║──║╔══╝║╔═╝║║║║╚╗╔╝║╔═╗║')
        sleep(0.5)
        print('║╚╝╚╗║╚╝║──║║────║║──║║──║╚══╗║╚═╗║╚╝║─║║─║╚═╝║')
        sleep(0.5)
        print('║╔═╗║║╔╗║──║║────║║──║║──║╔══╝╚═╗║║╔╗║─║║─║╔══╝')
        sleep(0.5)
        print('║╚═╝║║║║║──║║────║║──║╚═╗║╚══╗╔═╝║║║║║╔╝╚╗║║')
        sleep(0.5)
        print('╚═══╝╚╝╚╝──╚╝────╚╝──╚══╝╚═══╝╚══╝╚╝╚╝╚══╝╚╝')
        sleep(2)

    def interface(self, field):
        print(' ', end=' ')
        for i in range(10):
            print(i, end=' ')
        print()
        for i in range(10):
            print(i, end=' ')
            for j in range(10):
                print(field[i][j], end=' ')
            print()


    def field_availability(self, field, coordinate_x, coordinate_y):
        #conors
        #left_upper
        if (coordinate_x == 0 and coordinate_y == 0):
            if (field[coordinate_x][coordinate_y] == '~' and
            field[coordinate_x][coordinate_y+1] == '~' and
            field[coordinate_x+1][coordinate_y] == '~' and
            field[coordinate_x+1][coordinate_y+1] == '~'):
                return True
        #right_upper
        elif (coordinate_x == 0 and coordinate_y == 9):
            if (field[coordinate_x][coordinate_y] == '~' and
            field[coordinate_x][coordinate_y-1] == '~' and
            field[coordinate_x+1][coordinate_y-1] == '~' and
            field[coordinate_x+1][coordinate_y] == '~'):
                return True
        #right_down
        elif (coordinate_x == 9 and coordinate_y == 9):
            if (field[coordinate_x][coordinate_y] == '~' and
            field[coordinate_x-1][coordinate_y] == '~' and
            field[coordinate_x-1][coordinate_y-1] == '~' and
            field[coordinate_x][coordinate_y-1] == '~'):
                return True
        #left_down
        elif (coordinate_x == 9 and coordinate_y == 0):
            if (field[coordinate_x][coordinate_y] == '~' and
            field[coordinate_x-1][coordinate_y] == '~' and
            field[coordinate_x-1][coordinate_y+1] == '~' and
            field[coordinate_x][coordinate_y+1] == '~'):
                return True
        #between_connors
        #up
        elif coordinate_x == 0 and coordinate_y >= 1 and coordinate_y <=9:
            if (field[coordinate_x][coordinate_y] == '~' and
            field[coordinate_x][coordinate_y-1] == '~' and
            field[coordinate_x][coordinate_y+1] == '~' and
            field[coordinate_x+1][coordinate_y-1] == '~' and
            field[coordinate_x+1][coordinate_y] == '~' and
            field[coordinate_x+1][coordinate_y+1] == '~'):
                return True
        #right
        elif coordinate_y == 0 and coordinate_x >= 1 and coordinate_x <=9:
            if (field[coordinate_x][coordinate_y] == '~' and
            field[coordinate_x][coordinate_y-1] == '~' and
            field[coordinate_x-1][coordinate_y] == '~' and
            field[coordinate_x-1][coordinate_y-1] == '~' and
            field[coordinate_x+1][coordinate_y] == '~' and
            field[coordinate_x+1][coordinate_y-1] == '~'):
                return True
        #down
        elif coordinate_x == 0 and coordinate_y >= 1 and coordinate_y <=9:
            if (field[coordinate_x][coordinate_y] == '~' and
            field[coordinate_x][coordinate_y-1] == '~' and
            field[coordinate_x][coordinate_y+1] == '~' and
            field[coordinate_x-1][coordinate_y-1] == '~' and
            field[coordinate_x-1][coordinate_y] == '~' and
            field[coordinate_x-1][coordinate_y+1] == '~'):
                return True
        #left
        elif coordinate_y == 0 and coordinate_x >= 1 and coordinate_x <=9:
            if (field[coordinate_x][coordinate_y] == '~' and
            field[coordinate_x][coordinate_y+1] == '~' and
            field[coordinate_x-1][coordinate_y] == '~' and
            field[coordinate_x-1][coordinate_y+1] == '~' and
            field[coordinate_x+1][coordinate_y] == '~' and
            field[coordinate_x+1][coordinate_y+1] == '~'):
                return True
        elif (coordinate_x >= 1 and coordinate_x <=8 and coordinate_y >= 1 and
            coordinate_y <=8):
            if (field[coordinate_x][coordinate_y] == '~' and
            field[coordinate_x-1][coordinate_y-1] == '~' and
            field[coordinate_x-1][coordinate_y] == '~' and
            field[coordinate_x-1][coordinate_y+1] == '~' and
            field[coordinate_x][coordinate_y-1] == '~' and
            field[coordinate_x][coordinate_y+1] == '~' and
            field[coordinate_x+1][coordinate_y-1] == '~' and
            field[coordinate_x+1][coordinate_y] == '~' and
            field[coordinate_x+1][coordinate_y+1] == '~'):
                return True
        else:
            return False

    def field_initializetion(self, field):
        ship_counter = 0
        coordinates = []
        while (ship_counter < 8):
            coordinate_x = random.randint(0, 9)
            coordinate_y = random.randint(0, 9)
            if self.field_availability(field, coordinate_x, coordinate_y):
                field[coordinate_x][coordinate_y] = 'o'
                coordinates.append((coordinate_x, coordinate_y))
                ship_counter += 1
            else:
                continue
        self.ship_counter_player_1 = 8
        self.ship_counter_player_2 = 8

    def shoot(self, shot_field, main_field):
        shot_x = input('Enter coordinate(vertical)(0-9)')
        shot_y = input('Enter 2-nd coordinate(horizontal)(0-9)')
        if shot_x and shot_y:
            shot_x = int(shot_x)
            shot_y = int(shot_y)
        else:
            print('ERROR')
            return 0
        if shot_x > 10 or shot_x < -1:
            print('Error, incorrect value')
        elif shot_y < -1 or shot_y > 10:
            print('Error, incorrect value')
        else:
            if main_field[shot_x][shot_y] == 'o':
                main_field[shot_x][shot_y] = 'X'
                shot_field[shot_x][shot_y] = 'X'
                return True
            elif main_field[shot_x][shot_y] == '~':
                shot_field[shot_x][shot_y] = '*'
                print('you miss')
                return False

    def winer_print(self, player):
        if player == 1:
            print('╔═══╦╗─╔══╦╗╔╦═══╦═══╗─╔╗─╔╗╔╗╔╦══╦╗─╔╗')
            sleep(0.3)
            print('║╔═╗║║─║╔╗║║║║╔══╣╔═╗║╔╝║─║║║║║╠╗╔╣╚═╝║')
            sleep(0.3)
            print('║╚═╝║║─║╚╝║╚╝║╚══╣╚═╝║╚╗║─║║║║║║║║║╔╗─║')
            sleep(0.3)
            print('║╔══╣║─║╔╗╠═╗║╔══╣╔╗╔╝─║║─║║║║║║║║║║╚╗║')
            sleep(0.3)
            print('║║──║╚═╣║║║╔╝║╚══╣║║║──║║─║╚╝╚╝╠╝╚╣║─║║')
            sleep(0.3)
            print('╚╝──╚══╩╝╚╝╚═╩═══╩╝╚╝──╚╝─╚═╝╚═╩══╩╝─╚╝')
            print('YOU')
            self.interface(self.player_1_main_field)
            print('OPONENT')
            self.interface(self.player_2_main_field)
        elif player == 2:
            print('╔═══╦╗─╔══╦╗╔╦═══╦═══╗─╔══╗─╔╗╔╗╔╦══╦╗─╔╗')
            sleep(0.3)
            print('║╔═╗║║─║╔╗║║║║╔══╣╔═╗║─╚═╗║─║║║║║╠╗╔╣╚═╝║')
            sleep(0.3)
            print('║╚═╝║║─║╚╝║╚╝║╚══╣╚═╝║─╔═╝║─║║║║║║║║║╔╗─║')
            sleep(0.3)
            print('║╔══╣║─║╔╗╠═╗║╔══╣╔╗╔╝─║╔═╝─║║║║║║║║║║╚╗║')
            sleep(0.3)
            print('║║──║╚═╣║║║╔╝║╚══╣║║║──║╚═╗─║╚╝╚╝╠╝╚╣║─║║')
            sleep(0.3)
            print('╚╝──╚══╩╝╚╝╚═╩═══╩╝╚╝──╚══╝─╚═╝╚═╩══╩╝─╚╝')
            print('YOU')
            self.interface(self.player_2_main_field)
            print('OPONENT')
            self.interface(self.player_1_main_field)

    def printer(self):
        print('='*61)
        for i in range(10):
            print('|', end='')
            for j1 in range(10):
                print(self.player_1_shot_field[i][j1], end=' ')
            print('\t'*3, end='')
            for j2 in range(10):
                print(self.player_2_shot_field[i][j2], end=' ')
            print('|')
        print('='*61)

    def worker(self):
        self.tittle_battleship()
        os.system('cls')
        self.printer()
        self.field_initializetion(self.player_1_main_field)
        self.field_initializetion(self.player_2_main_field)
        print('First player ships')
        self.interface(self.player_1_main_field)
        sleep(4)
        os.system('cls')
        self.printer()
        print('Second player ships')
        self.interface(self.player_2_main_field)
        sleep(4)
        os.system('cls')
        self.printer()
        x1, x2 = (0, 0)
        while True:
            player_hit = True
            while player_hit:
                player_hit = False
                self.interface(self.player_1_shot_field)
                print('First player shot.')
                player_hit = self.shoot(self.player_1_shot_field, self.player_2_main_field)
                if player_hit:
                    self.ship_counter_player_2 -= 1
                os.system('cls')
                self.printer()
                if self.ship_counter_player_2 == 0:
                    self.winer_print(1)
                    x1 = 1
                    break
            if x1 == 1:
                break
            os.system('cls')
            self.printer()
            player_hit = True
            while player_hit:
                player_hit = False
                self.interface(self.player_2_shot_field)
                player_hit = False
                print('Second player shot.')
                player_hit = self.shoot(self.player_2_shot_field, self.player_1_main_field)
                if player_hit:
                    self.ship_counter_player_1 -= 1
                os.system('cls')
                self.printer()
                if self.ship_counter_player_1 == 0:
                    self.winer_print(2)
                    x2 = 1
                    break
            if x2 == 1:
                break

            os.system('cls')
            self.printer()



a = Battleship()
a.worker()
