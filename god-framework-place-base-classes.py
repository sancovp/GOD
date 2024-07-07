from unifai import unifai
from typing import Dict, Any, List

class Handler:
    def __init__(self):
        self.functions = {}

    def add_function(self, name: str, func):
        self.functions[name] = func

class Building:
    def __init__(self, name: str):
        self.name = name

class Repository(Building):
    def __init__(self):
        super().__init__("Repository")

class Factory(Building):
    def __init__(self):
        super().__init__("Factory")

class Service(Building):
    def __init__(self):
        super().__init__("Service")

class Center(Building):
    def __init__(self):
        super().__init__("Center")

class Road:
    def __init__(self, name: str):
        self.name = name

class Railroad(Road):
    def __init__(self, name: str):
        super().__init__(name)

class Agent:
    def __init__(self, name: str, role: str):
        self.name = name
        self.role = role
        self.instructions = ""
        self.domain = ""
        self.workflow = ""
        self.world_name = ""
        self.building_name = ""
        self.place_name = ""
        self.species = ""
        self.type = ""
        self.state = {}
        self.memories = []
        self.brain = None
        self.agent_anatomy = {}
        self.sdna_chains = []

    def process(self, context: Dict[str, Any]) -> Dict[str, Any]:
        return unifai.client.assistant_run(
            system_msg=f"You are {self.name}, a {self.role} in the GOD framework.",
            user_msg_template="Process the following: {0}",
            user_msg_input=str(context)
        ).content

    def use_tool(self, tool_name: str, **kwargs) -> Any:
        return unifai.client.tool_call(tool_name, **kwargs)

class Place:
    def __init__(self, name: str):
        self.name = name
        self.agent = None
        self.handler = Handler()
        self.buildings = {}
        self.roads = {}
        self.railroads = {}
        self.center = None

    def set_agent(self, agent: Agent):
        self.agent = agent

    def add_building(self, building: Building):
        self.buildings[building.name] = building

    def add_road(self, road: Road):
        self.roads[road.name] = road

    def add_railroad(self, railroad: Railroad):
        self.railroads[railroad.name] = railroad

    def set_center(self, center: Center):
        self.center = center
