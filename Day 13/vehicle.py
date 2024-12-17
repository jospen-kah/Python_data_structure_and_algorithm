# Base class
class Vehicle:
    def __init__(self, brand, year, model):
        self.brand = brand
        self.model = model
        self.year = year
        
    def display_info(self):
        return f"{self.brand} {self.model} {self.year}"
    
class LandVehicle(Vehicle):
    def __init__(self, brand, year, model,wheels):
        super().__init__(model, year, brand)
        self.wheels = wheels
    def display_info(self):
        return f"{super().display_info()} with {self.wheels}"
    
class Bike(LandVehicle): 
    def __init__(self, brand, year, model, wheels, bike_type):
        super().__init__(model, year, brand, wheels)
        self.bike_type = bike_type
    def display_info(self):
        return f"{super().display_info()} bike_type {self.bike_type} "
    
    
    
class Car(LandVehicle):
    def __init__(self,brand, year, model, wheels, fuel_type):
        super().__init__(model, year, brand, wheels)
        self.fuel_type  = fuel_type
    def display_info(self):
        return f"{super().display_info()}, fuel type:{self.fuel_type}"
    
    
class AirVehicle(Vehicle):
    def __init__(self, brand, year, model, engine_type):
        super().__init__(model, year, brand)
        self.engine_type = engine_type
    def display_info(self):
        return f"{super().display_info()} with engine type: {self.engine_type}"
        
car = Car("Toyota",  2021,"Camry", 4, "Gasoline")
bike = Bike("Yamaha",  2022,"YZF-R1", 2, "Sport")
plane = AirVehicle("Yamaha",  2020,"242X", "Jet Propulsion")
bus = LandVehicle("Mercedes",  2012, "Actros", 4)

print(car.display_info())        
print(bike.display_info())      
print(plane.display_info())       
print(bus.display_info()) 