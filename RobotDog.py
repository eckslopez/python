class Robot:
    def __init_(self, name, position):
        self.name = name
        self.position = [0,0]
        print('My name is', self.name)

    def walk(self, x):
        self.position[0] = self.position[0] + x
        print('New position:', self.position)

class RobotDog(Robot):
    def make_noise(self):
        print('Woof woof!')

my_robot_dog = RobotDog()
my_robot_dog.walk(10)
my_robot_dog.make_noise()