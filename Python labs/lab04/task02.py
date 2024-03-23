class VacuumAgent:
    def __init__(self, num_rooms):
        self.num_rooms = num_rooms
        self.location = 1  # Starting room is 1
    
    def sense(self, environment):
        return environment[self.location]
    
    def move(self):
        self.location = (self.location % self.num_rooms) + 1
    
    def clean(self, environment):
        environment[self.location] = 0  # Mark the room as cleaned


def main():
    num_rooms = int(input("Enter the number of rooms: "))
    environment = [1] * num_rooms  # 1 represents dirty, 0 represents clean
    agent = VacuumAgent(num_rooms)

    for _ in range(num_rooms * 2):  # Run for 2 times the number of rooms steps
        current_room_status = agent.sense(environment)
        if current_room_status == 1:
            print("Vacuum is cleaning room", agent.location)
            agent.clean(environment)
        else:
            print("Room", agent.location, "is already clean")
        
        agent.move()

if __name__ == "__main__":
    main()