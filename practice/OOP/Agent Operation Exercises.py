class Agent:
    def __init__(self, code_name: str, clearance_level: int):
        self.code_name = code_name
        self._clearance_level = clearance_level
    
    def report(self):
        print("Agent {} reporting. Clearance Level: {}".format(self.code_name, self._clearance_level))
        
class Mission():
    def __init__(self, mission_name: str, target_location: str, assigned_agent: Agent):
        self.mission_name = mission_name
        self.target_location = target_location
        self.assigned_agent = assigned_agent
        
    def brief(self):
        print("Mission: {}, Target: {}, Agent: {}".format(self.mission_name, self.target_location, self.assigned_agent.code_name))