class Vehicle:
    def __init__(self, speed):
        self.speed = speed

class LandVehicle(Vehicle):
    def __init__(self, speed, wheeel_count):
        Vehicle.__init__(self, speed)
        self.wheel_count = wheeel_count

class Car(LandVehicle):
    pass


my_car = Car(50, 4)
print(issubclass(Car, LandVehicle))
print(my_car.__dict__)