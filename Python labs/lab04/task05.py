class ReflexVacuumAgent:
    def __init__(self, num_rooms):
        self.num_rooms = num_rooms
        self.location = 1  # Starting room is 1
        self.model = [1] * num_rooms  # Initialize all rooms as dirty
    
    def decide(self):
        if self.model[self.location - 1] == 1:  # Check if the current room is dirty
            return 'clean'
        else:
            return 'move'
    
    def move(self):
        self.location = (self.location % self.num_rooms) + 1
    
    def clean(self):
        self.model[self.location - 1] = 0  # Mark the room as cleaned


def main():
    num_rooms = int(input("Enter the number of rooms: "))
    agent = ReflexVacuumAgent(num_rooms)

    while any(room != 0 for room in agent.model):  # Continue until all rooms are clean
        action = agent.decide()
        if action == 'clean':
            print("Vacuum is cleaning room", agent.location)
            agent.clean()
        elif action == 'move':
            print("Vacuum is moving to room", agent.location)
            agent.move()

if __name__ == "__main__":
    main()