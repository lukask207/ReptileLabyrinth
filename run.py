import random


class Reptile:
    """
    Reptile class which sets the start position
    and moves the reptile depending on N(orth),
    S(outh), E(ast) and W()west input from the user
    """
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.steps = 0

    def walk_direction(self, direction):
        """North and South are in y direction,
           East and West are in X direction"""
        if direction == 'N':
            self.y -= 1
        elif direction == 'S':
            self.y += 1
        elif direction == 'E':
            self.x += 1
        elif direction == 'W':
            self.x -= 1
        """" Only increase steps if direction is input
             as N/S/E/W character """
        if (direction == 'N' or direction == 'S' or
           direction == 'E' or direction == 'W'):
            self.steps += 1

    def display_labyrinth(self):
        """ Print reptile name initial and H for home of
            the reptile """
        Reptile_initial = self.name[0]
        for grid_y in range(7):
            for grid_x in range(7):
                if grid_x == reptile.x and grid_y == reptile.y:
                    print(Reptile_initial, end='  ')
                elif grid_x == home.x and grid_y == home.y:
                    print("H", end='  ')
                else:
                    print(".", end='  ')
            print()


class Home:
    """
    Reptile home position
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y


"""
Initialize Reptile, start position, and locations of the Trap
Re-define name of reptile to start with capital
"""

reptile_name = input("Name your reptile: \n").capitalize()
reptile = Reptile(reptile_name, 0, 0)

""" Position home at the right bottom area of the labyrinth """
home = Home((random.randint(4, 6)), (random.randint(4, 6)))
""" Generate random positions for three traps
    and make sure (0,0) and Home are not part of the trap positions
"""
traps = [(random.randint(0, 6), random.randint(0, 6)) for i in range(3)]
while ((0, 0) or (home.x, home.y)) in traps:
    traps = [(random.randint(0, 6), random.randint(0, 6)) for i in range(3)]


"""
    Start of Reptile Labyrinth Game

    Traps are not re-positioned until a new game is started
    It is not allowed to move outside the labyrinth
"""
while reptile.x != home.x or reptile.y != home.y:
    print(f"{reptile.name} is at ({reptile.x}, {reptile.y})")

    """ Check if the reptile is outside the labyrinth """
    if reptile.x < 0 or reptile.x > 6 or reptile.y < 0 or reptile.y > 6:
        print("You're outside the labyrinth! Start Over!")
        reptile.x = 0
        reptile.y = 0

    """ Check for traps """
    for ind in traps:
        if reptile.x == ind[0] and reptile.y == ind[1]:
            print("OOPS, you were trapped! Start over!")
            reptile.x = 0
            reptile.y = 0

    """ Move the lizard """
    reptile.display_labyrinth()
    direction = input('Which direction do '
                      'you want to walk? (N/S/E/W): \n').upper()
    reptile.walk_direction(direction)

""" Print message at the end of the game """
print(f'Well done {reptile.name}!')
print(f'You came safely home in {reptile.steps} steps!')