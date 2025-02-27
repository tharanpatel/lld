class Vehicle:
    def __init__(self, number_plate):
        self.vehicle_id = number_plate
        self.vehicle_type = None
    
    def get_vehicle_id(self):
        return self.vehicle_id

class Car(Vehicle):
    def __init__(self, number_plate):
        super().__init__(number_plate)
        self.type = "car"

class Motorcycle(Vehicle):
    def __init__(self, number_plate):
        super().__init__(number_plate)
        self.type = "motorcycle"

class Truck(Vehicle):
    def __init__(self, number_plate):
        super().__init__(number_plate)
        self.type = "truck"