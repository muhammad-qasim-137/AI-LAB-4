class Agent:
    def __init__(self, name, status):
        self.name = name
        self.status = status

    def perform_task(self):
        print("Agent is performing a task")


class SecurityAgent(Agent):
    def perform_task(self):
        print("Detecting cyber threat")


class MonitoringAgent(Agent):
    def perform_task(self):
        print("Monitoring system activity")


class RecoveryAgent(Agent):
    def perform_task(self):
        print("Recovering system services")


agents = [
    SecurityAgent("Security Agent", "Active"),
    MonitoringAgent("Monitoring Agent", "Active"),
    RecoveryAgent("Recovery Agent", "Active")
]

for agent in agents:
    print(agent.name, "-", agent.status)
    agent.perform_task()
