class Elevator:
    def __init__(self, current_floor=1):
        self.current_floor = current_floor

    def move(self, target_floor):
        if target_floor == self.current_floor:
            print(f"Elevator is already on floor {target_floor}")
        elif target_floor > self.current_floor:
            self.move_up(target_floor)
        else:
            self.move_down(target_floor)

    def move_up(self, target_floor):
        print(f"Moving up from floor {self.current_floor} to floor {target_floor}")
        self.current_floor = target_floor

    def move_down(self, target_floor):
        print(f"Moving down from floor {self.current_floor} to floor {target_floor}")
        self.current_floor = target_floor

def main():
    elevator = Elevator()

    while True:
        try:
            print(f"Elevator is currently on floor {elevator.current_floor}")
            target_floor = int(input("Enter the target floor (or 0 to exit): "))

            if target_floor == 0:
                print("Exiting the elevator program. Goodbye!")
                break

            elevator.move(target_floor)

        except ValueError:
            print("Invalid input. Please enter a valid floor number.")

if __name__ == "__main__":
    main()
