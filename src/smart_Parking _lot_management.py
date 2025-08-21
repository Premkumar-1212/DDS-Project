import time

class CarNode:
    def __init__(self, vehicle_number, entry_time):
        self.vehicle_number = vehicle_number
        self.entry_time = entry_time
        self.next = None

class ParkingLot:
    def __init__(self, total_slots):
        self.total_slots = total_slots
        self.head = None
        self.count = 0

    def park_car(self, vehicle_number):
        if self.count >= self.total_slots:
            print("Parking Lot Full! Cannot park more cars.")
            return

        entry_time = time.strftime("%Y-%m-%d %H:%M:%S")
        new_car = CarNode(vehicle_number, entry_time)
        # Insert at head (for efficiency)
        new_car.next = self.head
        self.head = new_car
        self.count += 1
        print(f"Vehicle {vehicle_number} parked at {entry_time}.")

    def exit_car(self, vehicle_number):
        prev = None
        current = self.head
        while current:
            if current.vehicle_number == vehicle_number:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                self.count -= 1
                exit_time = time.strftime("%Y-%m-%d %H:%M:%S")
                print(f"Vehicle {vehicle_number} exited at {exit_time}. Parked since {current.entry_time}")
                return
            prev = current
            current = current.next
        print("Vehicle not found in the lot!")

    def display_parked_cars(self):
        if not self.head:
            print("No cars parked.")
            return
        print("Active parked cars:")
        i = 1
        current = self.head
        while current:
            print(f"{i}. {current.vehicle_number} - Parked at {current.entry_time}")
            current = current.next
            i += 1
        print(f"Total parked cars: {self.count} / {self.total_slots}")

def main():
    total_slots = int(input("Enter total parking slots: "))
    lot = ParkingLot(total_slots)

    while True:
        print("\n--- Parking Lot Menu ---")
        print("1. Park car")
        print("2. Car exit")
        print("3. Show parked cars")
        print("4. Quit")
        choice = input("Your choice: ")

        if choice == "1":
            vehicle_number = input("Enter vehicle number: ")
            lot.park_car(vehicle_number)
        elif choice == "2":
            vehicle_number = input("Enter vehicle number to exit: ")
            lot.exit_car(vehicle_number)
        elif choice == "3":
            lot.display_parked_cars()
        elif choice == "4":
            print("Exiting Parking Lot System.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()


#Output:-
Enter total parking slots: 2

--- Parking Lot Menu ---
1. Park car
2. Car exit
3. Show parked cars
4. Quit
Your choice: 1
Enter vehicle number: KA05AB1234
Vehicle KA05AB1234 parked at 2025-08-21 08:17:10.

--- Parking Lot Menu ---
1. Park car
2. Car exit
3. Show parked cars
4. Quit
Your choice: 1
Enter vehicle number: MH12CD5678
Vehicle MH12CD5678 parked at 2025-08-21 08:17:14.

--- Parking Lot Menu ---
1. Park car
2. Car exit
3. Show parked cars
4. Quit
Your choice: 1
Enter vehicle number: TN09EF0009
Parking Lot Full! Cannot park more cars.

--- Parking Lot Menu ---
1. Park car
2. Car exit
3. Show parked cars
4. Quit
Your choice: 3
Active parked cars:
1. MH12CD5678 - Parked at 2025-08-21 08:17:14
2. KA05AB1234 - Parked at 2025-08-21 08:17:10
Total parked cars: 2 / 2

--- Parking Lot Menu ---
1. Park car
2. Car exit
3. Show parked cars
4. Quit
Your choice: 2
Enter vehicle number to exit: KA05AB1234
Vehicle KA05AB1234 exited at 2025-08-21 08:17:22. Parked since 2025-08-21 08:17:10

--- Parking Lot Menu ---
1. Park car
2. Car exit
3. Show parked cars
4. Quit
Your choice: 4
Exiting Parking Lot System.

