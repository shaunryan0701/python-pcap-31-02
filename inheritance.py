class Vehicle:
    pass

class LandVehicle(Vehicle):
    pass

class Car(LandVehicle):
    pass


print(issubclass(Car, LandVehicle))