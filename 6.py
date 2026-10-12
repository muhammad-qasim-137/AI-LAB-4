class Computer:
    def __init__(self, cpu_usage, ram_usage, battery_level):
        self.cpu_usage = cpu_usage
        self.ram_usage = ram_usage
        self.battery_level = battery_level

    def system_status(self):
        warning_found = False

        if self.cpu_usage > 80:
            print("Heavy CPU Load")
            warning_found = True

        if self.ram_usage > 85:
            print("High Memory Usage")
            warning_found = True

        if self.battery_level < 20:
            print("Low Battery")
            warning_found = True

        if not warning_found:
            print("System operating normally")


computer = Computer(90, 88, 15)
computer.system_status()
