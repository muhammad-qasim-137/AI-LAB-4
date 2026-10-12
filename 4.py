class Robot:
    def __init__(self, name, battery):
        self.name = name
        self.battery = battery

    def move(self):
        print("Robot is moving")

    def charge(self, amount):
        self.battery = min(100, self.battery + amount)
        print("Battery level:", self.battery)


class DeliveryRobot(Robot):
    def move(self):
        if self.battery < 20:
            print("Battery too low to move")
        else:
            print("Moving to a delivery location")


class SecurityRobot(Robot):
    def move(self):
        if self.battery < 20:
            print("Battery too low to move")
        else:
            print("Patrolling a specific area")


class RescueRobot(Robot):
    def move(self):
        if self.battery < 20:
            print("Battery too low to move")
        else:
            print("Moving toward a disaster location")


robots = [
    DeliveryRobot("DeliveryBot", 80),
    SecurityRobot("SecurityBot", 15),
    RescueRobot("RescueBot", 60)
]

for robot in robots:
    robot.move()

robots[1].charge(30)
robots[1].move()
