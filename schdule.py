# from collections import defaultdict
# from typing import Dict
from mesa.time import BaseScheduler

from controlagent import *

class CustomBaseSheduler(BaseScheduler):
    def __init__(self,model):
        super().__init__(model)

        self.agents_dict ={}
        self.steps = 0
        self.time = 0
        
    def add(self,agent):

        agent_class = type(agent).__name__
        agent_id = agent.unique_id

        if agent_class in  self.agents_dict.keys():
            if agent_id in self.agents_dict[agent_class].keys():
                raise Exception(
                    "Agent with unique id {0} already added to scheduler".format(repr(agent.unique_id))
                )
            else:
                self.agents_dict[agent_class][agent_id] = agent
        else :
            self.agents_dict[agent_class] = {agent_id : agent}

        self.add_reporter_params(agent, agent_id)

    def remove(self, agent):
        agent_class = type(agent).__name__
        agent_id = agent.unique_id
        del self.agents_dict[agent_class][agent_id]
            
    def getAllAgentsList(self,agent):
        agent_class = type(agent).__name__
        return self.agents_dict[agent_class].values()

    def getAllAgentsListByClass(self,agent_class):
        return self.agents_dict[agent_class.__name__].values()

    def getAllAgentsinGrid(self):
        return self.agents_dict

    def collectData(self, agent, param):
        agent_class = type(agent).__name__
        agent_id = agent.unique_id
        thisAgent = self.agents_dict[agent_class][agent_id]
        return getattr(thisAgent,param)

    def add_reporter_params(self,agent, unique_id):
        agent_class = type(agent)

        if agent_class == EV_Agent: 
            self.model.reporter_params[f'{unique_id} : Actual Speed (km/h)'] = lambda m: m.schedule.collectData(agent,'speed')
            self.model.reporter_params[f'{unique_id} : Availability'] = lambda m: m.schedule.collectData(agent,'availability')

        elif agent_class == WeatherAgent: 
            self.model.reporter_params[f'{unique_id} : Temperature (K)'] = lambda m: m.schedule.collectData(agent,'outdoorTemp')
            self.model.reporter_params[f'{unique_id} : Irradiance (W/m^2)'] = lambda m: m.schedule.collectData(agent,'outLight')

        elif agent_class == SolarPanelAgent : 
            self.model.reporter_params[f'{unique_id} : Solar Power (W)'] = lambda m: m.schedule.collectData(agent,'energy_E')

        elif agent_class == Charging_Control_Agent : 
            self.model.reporter_params[f'{unique_id} : SOC'] = lambda m: m.schedule.collectData(agent,'stateofcharge')
            # controlchargingAgent  :    stateofcharge, Control_value, powervalue,batterysoc 
            #  add these type and params

    def getCount(self, agent_class):
        return len(self.agents_dict[agent_class.__name__])

    def step(self):

        self.steps += 1
        self.time += 1

        for agent_class in self.agents_dict:
            for agent in self.agents_dict[agent_class].values():
                agent.step()

