from parking_lot import ParkingLot
from parking_level import ParkingLevel
from parking_spot import CarParkingSpot, MotorcycleParkingSpot, TruckParkingSpot
from vehicles import Car, Motorcycle, Truck

class ParkingLotDemo:
    def run():
        parking_lot = ParkingLot.get_instance()

        level1 = ParkingLevel(1)
        parking_lot.add_level(level1)

        spot1 = CarParkingSpot(1)

        level1.add_parking_spot(spot1)

        car1 = Car("bmw")
        car2 = Car("bmw2")

        parking_lot.park_vehicle(car1)
        parking_lot.get_free_spaces()
        parking_lot.park_vehicle(car2)



if __name__ == "__main__":
    ParkingLotDemo.run()
