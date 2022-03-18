from mesa.agent import Agent
from getDataFromExcel import get_XLSX_Data as data
import numpy as np


Weather_Data = data('solardata','Sheet1',{'Temp' : float, 'Radiation':float})

dataset  ={'CAR-1A': float, 'Acceleration-1A': float,'1A-available': float,'CAR-1B': float, 'Acceleration-1B': float,'1B-available': float}
EV_Data = data('EVsample','EVsample',dataset)

#_________________________________________________________________________________   Solar Panel Agent  _______________________________

class SolarPanelAgent(Agent):
    def __init__(self,unique_id, model):
        super().__init__(unique_id, model)

        self.neeta = 0.153
        self.Tow = 0.9
        self.A = 1.636
        
        self.Gc = 1000
        self.Tc = 298.15
        self.alpha = 0.0043
        
    def calculateSolarEnergy(self):

        cellmates = self.model.grid.get_cell_list_contents ([self.pos])
        weatherAgent = cellmates[1]

        G = weatherAgent.getOutdoorLight()
        T = weatherAgent.getOutdoorTemp()
        
        return 220*(G*self.Tow*self.neeta*self.A*(1 - self.alpha*(T-self.Tc )))

    def step(self):
        self.energy_E = self.calculateSolarEnergy()
  
#_________________________________________________________________________________  WEATHER _______________________________


class WeatherAgent(Agent): # weather condition, outdoor temperature,solar irradiance 
    def __init__(self,unique_id, model):
        super().__init__(unique_id, model)
        
        self.outdoorTempList = Weather_Data['Temp']
        self.outLightList = Weather_Data['Radiation']
     
    def getOutdoorTemp(self):
        return  self.outdoorTempList[self.model.schedule.steps]
    
    def getOutdoorLight(self): 
        return self.outLightList[self.model.schedule.steps]    
            
    def step(self):
        
        self.outLight = self.getOutdoorLight()
        self.outdoorTemp = self.getOutdoorTemp()

#_________________________________________________________________________________  EV  _______________________________
class EV_Agent(Agent):

    def __init__(self,unique_id, model):
        super().__init__(unique_id, model)

        self.daylist = [0]
        self.s = 0

        self.actual_speed_list= EV_Data[f'CAR-{unique_id}']
        self.accleration_list = EV_Data[f'Acceleration-{unique_id}']
        self.availability_list = EV_Data[f'{unique_id}-available']
        self.availability = 0

    def getAccleration(self):
        return  self.accleration_list[self.model.schedule.steps]
        
    def getAvailability(self):
        return self.availability_list[self.model.schedule.steps]
        
    def getSpeed(self):
        return self.actual_speed_list[self.model.schedule.steps]     


    # def Resistance_Force(self):
    #     self.Rolling_Resistance = []
    #     self.Aero_Dynamic = []
    #     self.Gradiant = []
    #     self.Inertia_Resistance = []
    #     self.R_Force = []
        
    #     self.co_effecient_RR = []
    #     self.Mass_Vehicle = [1800,1800]
    #     self.Ground_Accleration = 9.8
    #     self.inclanation_angle = 0
    #     self.Frontal_Area = 2.27
    #     self.Drag_Coeff = 0.29
    #     self.AirDensity = 1.184
    #     self.Wind_speed = 4.5
    #     self.Rotery_inertia_coeff = 1.04
        
    #     for V in self.V_act:
    #         co_effecient_rr = 0.01*(1+0.01*0.277*V)
    #         self.co_effecient_RR.append(co_effecient_rr)
            
    #         aero_Dynamic = 0.5*self.AirDensity*self.Frontal_Area*self.Drag_Coeff*(0.277*(V - self.Wind_speed))**2
    #         self.Aero_Dynamic.append(aero_Dynamic)
            
    #     for (co_effecient_rr,m) in  zip(self.co_effecient_RR,self.Mass_Vehicle):
    #         rolling_Resistance =  co_effecient_rr*m*self.Ground_Accleration*np.cos(self.inclanation_angle)
    #         self.Rolling_Resistance.append(rolling_Resistance)
            
    #     for (a,m) in zip(self.accleration,self.Mass_Vehicle):
    #         inertia_Resistance = self.Rotery_inertia_coeff*m*a
    #         self.Inertia_Resistance.append(inertia_Resistance)
        
    #     for m in self.Mass_Vehicle:
    #         gradiant_force = m*self.Ground_Accleration*np.sin(self.inclanation_angle)
    #         self.Gradiant.append(gradiant_force)

    #     for (rr,ir,ad,gf) in zip(self.Rolling_Resistance,self.Inertia_Resistance,self.Aero_Dynamic,self.Gradiant):
    #         self.r_Force = rr + gf + ad + ir
    #         self.R_Force.append(self.r_Force)
    #     #print( "r_force:{} ".format(self.R_Force))  
    #     return self.R_Force
        
    # def Power(self):
        
    #     self.Battery_Powerlist = []
       
    #     self.AuxiliaryPower = 300
    #     self.Powerusage = []
    #     self.Power_Traction = [] 
    #     self.Power_Braking = []
        
    #     self.alpha_regeneration = 0.3
    #     self.power_train_eff = 0.92
        
    #     for (V,r) in zip(self.V_act,self.R_Force):
    #         powerusage = 0.277*r*V  
    #         self.Powerusage.append(powerusage)
          
    #     for P in self.Powerusage:
    #         tp = P/self.power_train_eff
    #         bp = self.alpha_regeneration*P
            
    #         self.Power_Traction.append(tp)
    #         self.Power_Braking.append(bp)
                   
        
    #     for (a,tp,bp )in zip(self.accleration,self.Power_Traction,self.Power_Braking):
        
    #         if a > 0:
                
    #             self.Battery_Power = tp + self.AuxiliaryPower
                
    #         elif a <0:
                
    #             self.Battery_Power =  bp + self.AuxiliaryPower
    #         else:
    #             self.Battery_Power = tp
                
    #         self.Battery_Powerlist.append(self.Battery_Power)
    #     #print("Battery_Powerlist: {}".format(self.Battery_Powerlist))
    #     return self.Battery_Powerlist
            
    # def carSOC(self):
    #     self.initial_current_capacity = 112.6
    #     self.Opencircuit_Voltage = 312.96
    #     self.Battery_Resistance = 0.096
        
    #     Current = []
    #     Value = []
    #     self.SOC_value = [1,1]
    #     self.daylist.append(self.day)
        
    #     for self.Battery_Power in self.Battery_Powerlist:
    #         current = (self.Opencircuit_Voltage - ((self.Opencircuit_Voltage)**2 - 4*self.Battery_Resistance*self.Battery_Power )**0.5)*0.5/self.Battery_Resistance
    #         Current.append(current)
            
    #     for i in Current:
        
    #         value = 5*i/(self.initial_current_capacity*60)
    #         Value.append(value)
        
    #     #Update SOC value of EV as 1 in every start of the day otherthan that,calculate SOC w.r.t value
    #     if self.daylist[self.s-1] != self.day:

    #         self.SOC_value = [1,1]
         
    #     else:
    #         for i in range(len(self.SOC_value)):
    #             self.SOC_value[i] = self.SOC_value[i] + -1*Value[i]
            
        
        
    #     #print("SOC: {}".format(self.SOC_value))
    #     return self.SOC_value
           
    def step(self):
     
        self.speed = self.getSpeed()
        self.accleration = self.getAccleration()
        self.availability  = self.getAvailability()
        # self.ResistanceForce = self.Resistance_Force()
        # self.Powerconsumed = self.Power()
        # self.stateofcharge = self.carSOC()


#_________________________________________________________________________________  Utility_Grid  _______________________________

class Utility_Grid(Agent):

    def __init__(self,unique_id, model):
        super().__init__(unique_id, model)


    def step(self):
        pass

#_________________________________________________________________________________  Battery_Storage  _______________________________
      
class Battery_Storage(Agent):

    def __init__(self,unique_id, model):
        super().__init__(unique_id, model)

        #battery_storage_cap in Wh & max_power in W
        self.max_power  = 25000
        self.battery_storage_cap = 19730
        self.soc_max = 0.8
        self.soc_min = 0.2

        
    def step(self):
        pass

#_________________________________________________________________________________  Charge_pole  _______________________________

class Charge_pole(Agent):
 
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
    

    def fastcharging(self):
        charging_amount = 30000
        return charging_amount
        
    def L2charging(self):
        charging_amount = 6600
        return charging_amount

    def step(self):
        
        self.F = self.fastcharging()
        self.S = self.L2charging()

            
                