class Vehicle:
    color = "white"

    def __init__(self, _name: str, _capacity: int, _max_speed: int, _mileage: int):
        self._name = _name
        self._capacity = _capacity
        self._max_speed = _max_speed
        self._mileage = _mileage
    
    def travel(self, distance: int):
        self._mileage += distance
    
    def leastTimeToTravel(self, distance: int):
        travel_time: float = (distance * 60) / self._max_speed 
        return travel_time

    def __str__(self):
        return f"{self._name} (Color: {self.color}, Mileage: {self._mileage}, Capacity: {self._capacity})"

    def __lt__(self, other):
        return self._mileage < other._mileage


class Bus(Vehicle):
    color = "white"

    def __init__(self, _name: str, _max_speed: int, _mileage: int, _rows: int, _columns: int):
        default_capacity = _rows * _columns
        super().__init__(_name, default_capacity, _max_speed, _mileage)
        self._rows = _rows
        self._columns = _columns
        self.seat_occupation = [[False] * _columns for _ in range(_rows)]

    def isSeatOccupied(self, row: int, column: int):
        return self.seat_occupation[row - 1][column - 1]

    def total_occupation(self):
        occupied_seats = sum(row.count(True) for row in self.seat_occupation)
        total_seats = self._rows * self._columns
        return occupied_seats, total_seats

    def leastTimeToTravel(self, distance: int):
        base_time = super().leastTimeToTravel(distance)
        occupation_percentage = self.total_occupation()[0] / self.total_occupation()[1]

        # If the bus is occupied, adjust the least time
        if occupation_percentage > 0:
            time_increase: float = 0.1 * int(occupation_percentage / 0.2)
            return base_time * (1 + time_increase)
        else:
            return base_time

    def __str__(self):
        return f"{self._name} (Color: {self.color}, Mileage: {self._mileage}, Capacity: {self._capacity}, Rows: {self._rows}, Columns: {self._columns})"

    def __lt__(self, other):
        if self._mileage < other._mileage:
            return True
        elif self._mileage == other._mileage:
            return self._capacity < other._capacity
        else:
            return False

# Example usage
vehicle = Vehicle("Car", 4, 120, 100)
print(vehicle)

bus = Bus("City Bus", 80, 0, 4, 15)
print(bus)
