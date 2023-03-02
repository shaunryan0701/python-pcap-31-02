class Car:
    def __init__(self, model, color, initial_speed = 0):
        self.model = model
        self.color = color
        self.speed = initial_speed


    def speed_up(self):
        self.speed += 5

    
    def slow_down(self):
        self.speed -= 5


    def show_speed(self):
        print('Current speed: ', self.speed)
        

my_car = Car('C4', 'black')    
my_car.speed_up()
my_car.speed_up()
my_car.speed_up()

my_car.show_speed()