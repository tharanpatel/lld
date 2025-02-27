from vehicles import Vehicle
from parking_level import ParkingLevel

class ParkingLot:
    _instance = None
    def __init__(self):
        if ParkingLot._instance is not None:
            raise Exception("This class is a singleton!")
        else:
            ParkingLot._instance = self
            self.levels:list[ParkingLevel] = []

    @staticmethod
    def get_instance():
        if ParkingLot._instance is None:
            ParkingLot()
        return ParkingLot._instance
    
    def add_level(self, level):
        self.levels.append(level)
    
    def get_free_spaces(self):
        counter = 0
        for level in self.levels:
            print(f"-----Level {level.get_level_id()}-----")
            counter += level.check_free_spaces()
        
        print(f"This parking lot has {counter} free spaces.")
        return counter
    
    def park_vehicle(self, vehicle:Vehicle):
        for level in self.levels:
            if level.park_vehicle(vehicle):
                return True

        print(f"There are no valid spots for vehicle {vehicle.get_vehicle_id()}.")
        return False

    def unpark_vehicle(self, vehicle:Vehicle):
        for level in self.levels:
            if level.unpark_vehicle(vehicle):
                return True
        
        print(f"Could not unpark vehicle {vehicle.get_vehicle_id()}.")
        return False
    
    