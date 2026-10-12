class ThreatDetector:
    def __init__(self, device_name, ip_address, threat_level):
        self.device_name = device_name
        self.ip_address = ip_address
        self.threat_level = threat_level

    def scan(self):
        if self.threat_level.lower() == "low":
            print("System Safe")
        elif self.threat_level.lower() == "medium":
            print("Suspicious Activity")
        elif self.threat_level.lower() == "high":
            print("Critical Threat Detected")
        else:
            print("Invalid threat level")


device = ThreatDetector("Computer1", "192.168.1.10", "High")
device.scan()
