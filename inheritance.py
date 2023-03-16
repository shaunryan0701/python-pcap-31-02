class Vehicle:
    class_message = 'This is a message from the Vehicle class!'
    def __init__(self, speed):
        self.speed = speed

class LandVehicle(Vehicle):
    def __init__(self, speed, wheeel_count):
        super().__init__(speed)
        self.wheel_count = wheeel_count
        print(Vehicle.class_message)

class Car(LandVehicle):
    pass


my_vehicle = Vehicle(50)
my_land_vehicle = LandVehicle(60, 3)
my_car = Car(50, 4)

# print(issubclass(Car, LandVehicle))
print(isinstance(my_vehicle, LandVehicle))
print(isinstance(my_land_vehicle, LandVehicle))
print(isinstance(my_car, LandVehicle))
print(my_vehicle.__dict__)
print(my_land_vehicle.__dict__)
print(my_car.__dict__)