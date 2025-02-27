from vehicles import Vehicle

class ParkingSpot:
    def __init__(self, spot_id):
        self.spot_id = spot_id
        self.vehicle_id = None
    
    def can_vehicle_use_spot(self, vehicle):
        if vehicle.type in self.allowed_vehicles:
            return True
        
        return False
    
    def get_spot_id(self):
        return self.spot_id

    def get_vehicle_id(self):
        return self.vehicle_id
    
    def set_vehicle_id(self, vehicle:Vehicle):
        self.vehicle_id = vehicle.get_vehicle_id()
    
    def release_spot(self):
        self.vehicle_id = None

class CarParkingSpot(ParkingSpot):
    def __init__(self, spot_id):
        super().__init__(spot_id)
        self.allowed_vehicles = ["car", "motorcycle"]
    
class MotorcycleParkingSpot(ParkingSpot):
    def __init__(self, spot_id):
        super().__init__(spot_id)
        self.allowed_vehicles = ["motorcycle"]

class TruckParkingSpot(ParkingSpot):
    def __init__(self, spot_id):
        super().__init__(spot_id)
        self.allowed_vehicles = ["car", "motorcycle", "truck"]
