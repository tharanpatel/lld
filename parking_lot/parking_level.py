from parking_spot import ParkingSpot
from vehicles import Vehicle

class ParkingLevel:
    def __init__(self, level_id:int):
        self.parking_spots:dict[int:ParkingSpot] = {} # SpotId : Spot
        self.occupied_spots:dict[Vehicle:ParkingSpot] = {} # Vehicle : Spot
        self.level_id = level_id
    
    def get_level_id(self):
        return self.level_id
    
    def add_parking_spot(self, parking_spot:ParkingSpot):
        self.parking_spots[parking_spot.get_spot_id()] = parking_spot
    
    def remove_parking_spot(self, parking_spot:ParkingSpot):
        del self.parking_spots[parking_spot.get_spot_id()]
    
    def check_free_spaces(self):
        counter = 0
        for key in self.parking_spots:
            spot = self.parking_spots[key]
            if not spot.get_vehicle_id():
                print(f"Spot {spot.get_spot_id()} is free on level {self.level_id}.")
                counter += 1
        
        print(f"There are {counter} free spaces on level {self.level_id}.")
        return counter
    
    def park_vehicle(self, vehicle:Vehicle):
        for key in self.parking_spots:
            spot = self.parking_spots[key]
            valid_spot_for_vehicle = spot.can_vehicle_use_spot(vehicle)
            is_spot_occupied = spot.get_vehicle_id()

            if valid_spot_for_vehicle and not is_spot_occupied:
                spot.set_vehicle_id(vehicle)
                return True
        
        return False
    
    def unpark_vehicle(self, vehicle):
        for key in self.parking_spots:
            spot = self.parking_spots[key]
            spot_vehicle_id = spot.get_vehicle_id()

            if spot_vehicle_id == vehicle.get_vehicle_id():
                spot.release_spot()
                return True
        
        return False
    

        
    

