# 1. Run the two room vaccum cleaner agent program and understand it. Convert the 
# program to a Three room environment.
from abc import abstractmethod

class Environment(object):
    ''' Abstract class representing an environment '''

    @abstractmethod
    def __init__(self, n):
        self.n = n

    @abstractmethod
    def executeStep(self, n=1):
        raise NotImplementedError('executeStep must be defined!')

    @abstractmethod
    def executeAll(self):
        raise NotImplementedError('executeAll must be defined!')

    def delay(self, n=100):
        self.delay = n

class ThreeRoomVaccumCleanerEnvironment(Environment):
    ''' Represents a three-room vaccum cleaner environment '''

    def __init__(self, agent):
        ''' Constructor '''
        self.r1 = Room('A', 'dirty')
        self.r2 = Room('B', 'dirty')
        self.r3 = Room('C', 'dirty')
        self.agent = agent
        self.currentRoom = self.r1
        self.delay = 1000
        self.step = 1
        self.action = ""

    def executeStep(self, n=1):
        ''' Execute n steps in the environment '''
        for _ in range(0, n):
            self.displayPerception()
            self.agent.sense(self)
            res = self.agent.act()
            self.action = res
            if res == 'clean':
                self.currentRoom.status = 'clean'
            elif res == 'right':
                if self.currentRoom == self.r1:
                    self.currentRoom = self.r2
                elif self.currentRoom == self.r2:
                    self.currentRoom = self.r3
            elif res == 'left':
                if self.currentRoom == self.r2:
                    self.currentRoom = self.r1
                elif self.currentRoom == self.r3:
                    self.currentRoom = self.r2
            self.displayAction()
            self.step += 1

    def executeAll(self):
        ''' Execute all steps in the environment '''
        raise NotImplementedError('executeAll must be defined!')

    def displayPerception(self):
        ''' Display perception of the environment '''
        print("Perception at step %d is [%s, %s]" % (self.step, self.currentRoom.status, self.currentRoom.location))

    def displayAction(self):
        ''' Display action taken by the agent '''
        print("------- Action taken at step %d is [%s]" % (self.step, self.action))

class Room:
    ''' Represents a room in the environment '''

    def __init__(self, location, status="dirty"):
        ''' Constructor '''
        self.location = location
        self.status = status

class Agent(object):
    ''' Abstract class representing an agent '''

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def sense(self, environment):
        pass

    @abstractmethod
    def act(self):
        pass

class VaccumAgent(Agent):
    ''' Represents a vaccum cleaner agent '''

    def __init__(self):
        ''' Constructor '''
        pass

    def sense(self, env):
        ''' Sense the environment '''
        self.environment = env

    def act(self):
        ''' Take action based on the environment '''
        if self.environment.currentRoom.status == 'dirty':
            return 'clean'
        if self.environment.currentRoom.location == 'A':
            return 'right'
        if self.environment.currentRoom.location == 'B':
            return 'left'

# Test program
if __name__ == '__main__':
    # Create a VaccumAgent object
    vcagent = VaccumAgent()

    # Create a ThreeRoomVaccumCleanerEnvironment object
    env = ThreeRoomVaccumCleanerEnvironment(vcagent)

    # Execute 50 steps in the environment
    env.executeStep(50)



