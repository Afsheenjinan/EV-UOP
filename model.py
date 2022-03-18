from mesa.model import Model
from schdule import CustomBaseSheduler
# from agents import *      #  control agent already import other agents
from controlagent import *

from mesa.datacollection import DataCollector  #Data collector
from mesa.space import MultiGrid, SingleGrid

class ConceptModel(Model):
   
    def __init__(self ,height , width, grid_positions = "uncontrolled"  ):

        self.steps = 0
        self.minute = 0
        self.hour = 0
        self.day = 0
        self.week = 0
        self.month = 0

        self.reporter_params = {}

        self.schedule = CustomBaseSheduler(self)

        self.grid = MultiGrid(width, height, torus=True)
        self.grid_positions = grid_positions
        
        for id,cord in {'CA':(1,1)}.items():           # weather agent ''' Add two weather agents'''
            agent = Charging_Control_Agent(id,self)
            self.schedule.add(agent)
            self.grid.place_agent(agent, (cord[0], cord[1]))    # x : cord[0] , y: cord[1]
        
        for id,cord in {'ws1':(2,9) , 'ws2': (3,10)}.items():           # weather agent ''' Add two weather agents'''
            weatherAgent = WeatherAgent(id,self)
            self.schedule.add(weatherAgent)
            self.grid.place_agent(weatherAgent, (cord[0], cord[1]))    # x : cord[0] , y: cord[1]

        for id,cord in {'1A':(5,10) , '1B': (5,9)}.items():             # EV agent     ''' Add two ev agents'''
            ev_agent = EV_Agent(id,self)
            self.schedule.add(ev_agent)
            self.grid.place_agent(ev_agent, (cord[0], cord[1]))        # solar agent    ''' Add one solar agent''' 

        for id,cord in {'1':(1,18)}.items():               
            solarPanelAgent = SolarPanelAgent(f'Solar{id}',self)
            weatherAgent = WeatherAgent(f'Weather{id}',self)
            self.schedule.add(solarPanelAgent)
            self.schedule.add(weatherAgent)
            self.grid.place_agent(solarPanelAgent, (cord[0], cord[1]))   
            self.grid.place_agent(weatherAgent, (cord[0], cord[1])) 

         

         
        """
        weatherAgent = WeatherAgent('ws1',self)
        self.schedule.add(weatherAgent)
        self.grid.position_agent(weatherAgent,(2,9))    # weather agent


        solarPanelAgent = SolarPanelAgent('Solar',self)
        self.schedule.add(solarPanelAgent)
        self.grid.position_agent(solarPanelAgent,1,18)  # solar agent
        
        car1 = EV_Agent('1A', self)
        self.schedule.add(car1)
        self.grid.position_agent(car1,5,10)             # EV agent
        """

        """
        ChargeAgent1 = Charge_pole('charge1',self)
        self.schedule.add(ChargeAgent1)
        self.grid.position_agent(ChargeAgent1,6,10)     #create chargepole

        ChargeAgent2 = Charge_pole('charge2',self)
        self.schedule.add(ChargeAgent2)
        self.grid.position_agent(ChargeAgent2,6,9)      #create chargepole

        ControlAgent = Charging_Control_Agent('control_value',self)
        self.schedule.add(ControlAgent)
        self.grid.position_agent(ControlAgent,6,11)      #create controlAgent
        """

        """
        reporter_params = {
                "Temperature (K)"       : lambda m: m.schedule.collectData(weatherAgent,'outdoorTemp'),
                "Irradiance (W/m^2)"    : lambda m: m.schedule.collectData(weatherAgent,'outLight'),
                
                f'Actual Speed {car1.unique_id} (km/h)': lambda m: m.schedule.collectData(car1,'actual_speed'),
                f'Actual Speed {car2.unique_id} (km/h)': lambda m: m.schedule.collectData(car2,'actual_speed')}
        """

        # print(self.reporter_params)
        self.datacollector = DataCollector(self.reporter_params)
        
        """  
            # model_reporters = {
            #     "Temperature (K)"       : lambda m: m.schedule.collectData(weatherAgent,'outdoorTemp'),
            #     "Irradiance (W/m^2)"    : lambda m: m.schedule.collectData(weatherAgent,'outLight'),
                
            #     f'Actual Speed {car1.unique_id} (km/h)': lambda m: m.schedule.collectData(car1,'actual_speed'),
            #     f'Actual Speed {car2.unique_id} (km/h)': lambda m: m.schedule.collectData(car2,'actual_speed'),
            #     # "Solar Power (W)": lambda m: m.schedule.getCurrentPower(SolarPanelAgent), 
            #     # "Temperature (K)": lambda m: m.schedule.getCurrentWeather(weatherAgent),
            #     # "Irradiance (W/m^2)": lambda m: m.schedule.getCurrentIrr(weatherAgent),
            #     # f'Actual Speed {car1.unique_id} (km/h)': lambda m: m.schedule.getactualspeed(car1),
            #     # f'Actual Speed {car2.unique_id} (km/h)': lambda m: m.schedule.getactualspeed(car2),
            #     # "Availability": lambda m: m.schedule.getavailability(EV_Agent),

            #     # "SOC_CAR": lambda m: m.schedule.getSoC(Charging_Control_Agent)[0][self.B][0],
            #     # "Car Battery Power(W)": lambda m: m.schedule.getcarbattery(Charging_Control_Agent)[0][self.B][0],
            #     # "Grid_Power (W)": lambda m: m.schedule.getactualgridpower(Charging_Control_Agent)[0][0][self.B],
            #     # "Battery_SOC": lambda m: m.schedule.getbattsoc(Charging_Control_Agent)[0][self.B]

            # })"""
  
        self.running = True
        
    def step(self):
        self.schedule.step()
        self.datacollector.collect(self)
        self.steps += 1

        self.minute += 5
        if self.minute > 59:
            self.hour += 1
            self.minute = 0

        if self.hour > 23:
            self.day += 1
            self.hour = 0

        if self.day > 6:
            self.week += 1
            self.day = 1
                
        if self.week > 4:
            self.month +=1
            self.week = 1
               
        # print(  "Week : {} Day : {} Hour : {} minute: {}\n".format(self.week, self.day, self.hour,self.minute))     
        # 
        '''This is getting RESET AlWAYS - see the console - values might be different, because the agents load values from shedule.steps'''   
