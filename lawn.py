import random

class Environment():

    def __init__(self, growth_rate) -> None:
        self.growth_rate = growth_rate

class Lawn():
    
    Lawn_Grid = 0
    new_Mower = 0
    cut_Percent = 0
    current_direction = "x"

    def __init__(self, lawn_x, lawn_y) -> None:
        self.lawn_x = lawn_x + 2
        self.lawn_y = lawn_y + 2
        self.lawn_Size = 0
        self.Lawn_Grid = []
        
    
    def make_Lawn(self):
        lawn = []
        row = []

        for i in range(self.lawn_x):
            xlist = []
            row.append(xlist)

        for i in range(self.lawn_y):
            new_list = row.copy()
            lawn.append(new_list)

        self.lawn_Size = self.lawn_y * self.lawn_x
        self.Lawn_Grid = lawn        

    def grow_Grass(self):
        for i in range(len(self.Lawn_Grid)):
            for u in range(len(self.Lawn_Grid[i])):
                self.Lawn_Grid[i][u] = Grass(5)

    def spawn_Mower(self):
        self.new_Mower = Mower(3,15,15)
        
        for i in range(len(self.Lawn_Grid)):
            if i == self.new_Mower.position_x - 1:
                for u in range(len(self.Lawn_Grid[i])):
                    if u == self.new_Mower.position_y - 1:
                        self.Lawn_Grid[i][u].grass_height = self.new_Mower.cut_height

    def move_Mower(self):
        
        directions = ["x","y","xy1","xy2","xy3","xy4","xn","yn"]
        random_event_change = random.randint(0,5)
        move_x_positive = self.new_Mower.position_x + 1
        move_y_positive = self.new_Mower.position_y + 1
        move_x_negative = self.new_Mower.position_x - 1
        move_y_negative = self.new_Mower.position_y - 1

        if random_event_change == 5:
            random_change = random.randint(0,7)
            self.current_direction = directions[random_change]
        

        if self.current_direction == "x" and (0 < move_x_positive <= self.lawn_x):
            self.new_Mower.position_x = move_x_positive
        elif self.current_direction == "xn" and (0 < move_x_negative <= self.lawn_x):
            self.new_Mower.position_x = move_x_negative
        elif self.current_direction == "y" and (0 < move_y_positive <= self.lawn_y):
            self.new_Mower.position_y = move_y_positive
        elif self.current_direction == "yn" and (0 < move_y_negative <= self.lawn_y):
            self.new_Mower.position_y = move_y_negative
        elif self.current_direction == "xy1" and (0 < move_y_positive <= self.lawn_y) and (0 < move_x_positive <= self.lawn_x):
            self.new_Mower.position_y = move_y_positive
            self.new_Mower.position_x = move_x_positive
        elif self.current_direction == "xy2" and (0 < move_y_negative <= self.lawn_y) and (0 < move_x_positive <= self.lawn_x):
            self.new_Mower.position_y = move_y_negative
            self.new_Mower.position_x = move_x_positive
        elif self.current_direction == "xy3" and (0 < move_y_negative <= self.lawn_y) and (0 < move_x_negative <= self.lawn_x):
            self.new_Mower.position_y = move_y_negative
            self.new_Mower.position_x = move_x_negative
        elif self.current_direction == "xy4" and (0 < move_y_positive <= self.lawn_y) and (0 < move_x_negative <= self.lawn_x):
            self.new_Mower.position_y = move_y_positive
            self.new_Mower.position_x = move_x_negative
        else:
           
            random_direction = random.randint(0,7)
            
            self.current_direction = directions[random_direction]
        
        for i in range(len(self.Lawn_Grid)):
            if i == self.new_Mower.position_x - 1:
                for u in range(len(self.Lawn_Grid[i])):
                    if u == self.new_Mower.position_y - 1:
                        self.Lawn_Grid[i][u].grass_height = self.new_Mower.cut_height
                        

        self.cut_Percent = self.cut_Percent_calc()

    def cut_Percent_calc(self):
        tot = 0
        cut = 0
        for i in range(len(self.Lawn_Grid)):
            for u in range(len(self.Lawn_Grid[i])):
                if self.Lawn_Grid[i][u].grass_height == self.new_Mower.cut_height:
                    cut += 1
                    tot += 1
                else:
                    tot += 1
        
        return (cut / tot) * 100

    def print_lawn(self):
        
        print_lawn = []
        row = []

        for i in range(self.lawn_x):
            xlist = []
            row.append(xlist)

        for i in range(self.lawn_y):
            new_list = row.copy()
            print_lawn.append(new_list)

        for i in range(len(self.Lawn_Grid)):
            for u in range(len(self.Lawn_Grid[i])):
                
                print_lawn[i][u] = self.Lawn_Grid[i][u].grass_height

        for i in range(len(print_lawn)):
            print(print_lawn[i])


class Grass():
    
    def __init__(self, grass_height) -> None:
        self.grass_height = grass_height


class Mower():

    def __init__(self, cut_height, position_x, position_y) -> None:
        self.cut_height = cut_height
        self.position_x = position_x
        self.position_y = position_y
    

    
Environment = Environment(1)
Lawn = Lawn(30, 30)
Lawn.make_Lawn()
Lawn.grow_Grass()

Lawn.spawn_Mower()
c = 0

while c < 1024:
    
    print(f"Mower X: {Lawn.new_Mower.position_x}, Y: {Lawn.new_Mower.position_y} Direction {Lawn.current_direction}")
    Lawn.move_Mower()
     
    c += 1
print(f"{Lawn.cut_Percent}")
Lawn.print_lawn()

