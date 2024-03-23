import time

class VacuumAgent:
    def __init__(self, num_rooms):
        self.num_rooms = num_rooms
        self.location = 1  # Starting room is 1
        self.score = 0
    
    def sense(self, environment):
        return environment[self.location]
    
    def move(self):
        self.score -= 1  # Deduct 1 point for moving
        self.location = (self.location % self.num_rooms) + 1
    
    def clean(self, environment):
        environment[self.location] = 0  # Mark the room as cleaned
        self.score += 25  # Add 25 points for cleaning


def main():
    num_rooms = int(input("Enter the number of rooms: "))
    environment = [1] * num_rooms  # 1 represents dirty, 0 represents clean
    agent = VacuumAgent(num_rooms)

    while any(room != 0 for room in environment):  # Continue until all rooms are clean
        current_room_status = agent.sense(environment)
        if current_room_status == 1:
            print("Vacuum is cleaning room", agent.location)
            agent.clean(environment)
        else:
            print("Room", agent.location, "is already clean")
        
        agent.move()
        time.sleep(1)  # Wait for 1 second
        print("Score:", agent.score)

if __name__ == "__main__":
    main()