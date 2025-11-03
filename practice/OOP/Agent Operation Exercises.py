class Agent:
    total_agents = 0
    def __init__(self, code_name: str, clearance_level: int):
        self.code_name = code_name
        self._clearance_level = clearance_level
        Agent.total_agents += 1

    def report(self):
        return """Agent {} reporting. Clearance Level: {}""".format(self.code_name, self._clearance_level)

    def get_clearance_level(self):
        print(self._clearance_level)

    def set_clearance_level(self, level: int):
        if level < 1 or level > 10:
            return "You cannot change the level below 1 or above 10."
        self._clearance_level = level

    @staticmethod
    def get_total_agents():
        print("Total agents created: {}".format(Agent.total_agents))

class Mission():
    def __init__(self, mission_name: str, target_location: str, assigned_agent: Agent):
        self.mission_name = mission_name
        self.target_location = target_location
        self.assigned_agent = assigned_agent

    def brief(self):
        print("Mission: {}, Target: {}, Agent: {}".format(self.mission_name, self.target_location, self.assigned_agent.code_name))

class FieldAgent(Agent):
    def __init__(self, code_name: str, clearance_level: int, region: str):
        super().__init__(code_name, clearance_level)
        self.region = region

    def report(self):
        return super().report() + self.region

class CyberAgent(Agent):
    def __init__(self, code_name, clearance_level, specialty):
        super().__init__(code_name, clearance_level)
        self.specialty = specialty

    def report(self):
        return super().report() + self.specialty
    
def print_agent(list_agent: list):
    for i in list_agent:
        print(i.report())