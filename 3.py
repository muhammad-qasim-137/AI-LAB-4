class SecuritySystem:
    def respond(self):
        print("General security response")


class Firewall(SecuritySystem):
    def respond(self):
        print("Block suspicious network traffic")


class Antivirus(SecuritySystem):
    def respond(self):
        print("Isolate malicious files")


class IntrusionDetectionSystem(SecuritySystem):
    def respond(self):
        print("Generate security alert")


tools = [Firewall(), Antivirus(), IntrusionDetectionSystem()]

for tool in tools:
    tool.respond()
