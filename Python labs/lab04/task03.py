# 3. Does the agent ever stop? If no, can you make it stop? Is your program rational?
# No, the agent in the provided program does not have a mechanism to stop automatically. It will continue executing steps indefinitely until the program is terminated or an external condition is met.
# To make the agent stop after a certain condition is met, we can modify the executeStep() method to include a termination condition. For example, we can add a maximum step limit or check if all rooms are clean. Once the termination condition is met, the agent can stop executing further steps.
# Here's how we can modify the executeStep() method to include a termination condition based on the maximum number of steps:                                      class NRoomVaccumCleanerEnvironment(Environment):
    # Previous code...
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

    while any(room != 0 for room in environment):  # Continue until all rooms are clean
        current_room_status = agent.sense(environment)
        if current_room_status == 1:
            print("Vacuum is cleaning room", agent.location)
            agent.clean(environment)
        else:
            print("Room", agent.location, "is already clean")
        
        agent.move()

if __name__ == "__main__":
    main()