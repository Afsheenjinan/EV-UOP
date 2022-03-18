from agents import *

class Charging_Control_Agent(Agent):
    def __init__(self,unique_id, model):
        super().__init__(unique_id, model)
        
        self.stateofcharge = 0
        # self.daylist = [0]
        # self.s = 0

        # print(self.model.grid_positions)
        # self.SOC_value1 = [1,1]
        # self.SOC_value2 =[1,1]
        # self.SOC_value3 = [1,1]
        
        # self.batterySOC1 = 0.6
        # self.batterySOC2 = 0.6
        # self.batterySOC3 = 0.6
        
        # self.solarpanelagent = SolarPanelAgent('Solar_data',self)
        # self.EVagent = EV_Agent('SoC_Data',self)
        # self.chargepole = Charge_pole('Charging_power',self)
        # self.batterypole = Battery_Storage('Battery_capacity',self)
          
        # self.Batterypower = 0
        # self.Gridpower = 0

    def myFunction(self):
        
        all_EV_agents_in_grid = self.model.schedule.getAllAgentsListByClass(EV_Agent)
        print(all_EV_agents_in_grid)
        """do whatever with the EV agents List"""

        all_agents_in_grid = self.model.schedule.getAllAgentsinGrid()
        print(all_agents_in_grid)

        for a in all_EV_agents_in_grid:
            acceleration = a.getAccleration()
            print(acceleration)

        """do whatever with all agents Dict"""
           
    # def SoC(self):

    #     self.initial_current_capacity = [112.6,112.6]
    #     self.Opencircuit_Voltage = [312.96,312.96]
    #     self.Battery_Resistance = [0.096,0.096]
        
    #     Battery_Current = []
    #     current1 =[]
    #     current2= []
    #     current3 = []
        
    #     Value = []
    #     Value1 =[]
    #     Value2 =[]
    #     Value3 =[]
        
    #     self.daylist.append(self.day)
        
    #     #Calculate battery current [[i1,i2],[],[]]and soc values
        
    #     for (power,v,r) in zip(self.PP[0],self.Opencircuit_Voltage,self.Battery_Resistance):
    #         c = (v - ((v)**2 - 4*r*power )**0.5)*0.5/r
    #         current1.append(c)
                 
    #     for (i,cc) in zip(current1,self.initial_current_capacity):
    #         value = 5*i/(cc*60)
    #         Value1.append(round(value,2))
                
    #     for (power,v,r) in zip(self.PP[1],self.Opencircuit_Voltage,self.Battery_Resistance):
    #         c = (v - ((v)**2 - 4*r*power )**0.5)*0.5/r
    #         current2.append(c)
                 
    #     for (i,cc) in zip(current2,self.initial_current_capacity):
    #         value = 5*i/(cc*60)
    #         Value2.append(round(value,2))        
                
    #     for (power,v,r) in zip(self.PP[2],self.Opencircuit_Voltage,self.Battery_Resistance):
    #         c = (v - ((v)**2 - 4*r*power )**0.5)*0.5/r
    #         current3.append(c)
                 
    #     for (i,cc) in zip(current3,self.initial_current_capacity):
    #         value = 5*i/(cc*60)
    #         Value3.append(round(value,2)) 
            
    #     Battery_Current = [current1,current2,current3]
    #     Value = [Value1,Value2,Value3]
    #     #print(Value)
        
    #     #Update SOC value of EV as 1 in every start of the day otherthan that,calculate SOC w.r.t value
    #     if self.daylist[self.s-1] != self.day:

    #         self.SOC_value1 = [1,1]
    #         self.SOC_value2 = [1,1]
    #         self.SOC_value3 = [1,1]
            
    #     else:
     
    #        self.SOC_value1[0] += -1*Value[0][0]
    #        self.SOC_value2[0] += -1*Value[1][0]
    #        self.SOC_value3[0] += -1*Value[2][0]
            
    #        self.SOC_value1[1] += -1*Value[0][1]
    #        self.SOC_value2[1] += -1*Value[1][1]
    #        self.SOC_value3[1] += -1*Value[2][1]
    #     #self.SOC_value= [[0,1],[0,1],[0,1]]
    #     self.SOC_value = [ self.SOC_value1,self.SOC_value2,self.SOC_value3]  
    #     #print("self.SOC_value:{}".format(self.SOC_value) )
    #     return self.SOC_value
        
    # def chargingcontrol(self):
        
    #     self.E1 = self.chargepole.L2charging()
    #     self.E2 = self.chargepole.fastcharging()
    #     self.P = self.EVagent.Power()
    #     self.D = self.EVagent.a
        
    #     self.Power1 = []
    #     self.Power2 = []
    #     self.Power3 = []
    #     self.SOC_value = [ self.SOC_value1,self.SOC_value2,self.SOC_value3]
        
    #     #If car start to charge in UNCONTROLLED CHARGING PATTERN - whenever car stops in the faculty it charge the car until SOC reach to 1 or disconnection/return to home
    #     for  (p,v,uSOC) in  zip(self.P,self.D,self.SOC_value[0]):  
    #         if 8 <= self.hour <= 17:
    #             print("Charge Pole is Available - U Can Charge..!!!")
                    
    #             if v == 1:
    #                 if uSOC < 1:
    #                     PP1 = -1*self.E1 + p
                              
    #                 else:
    #                     PP1 = p
                            
    #             else:
    #                 PP1 = p
                    
    #         else:
    #             print("Charge Pole is not available....SORRY.....!!!")
    #             PP1 = p
    #         self.Power1.append(PP1)        
        
    #     #if car choose V2G controlled charging - when SOC less than 0.5, it immediately charge in fast charging mode to reach to 0.5,then it charge until SOC = 0.8 afterwards  it is in V2G mode '''
    #     for  (p,v,v2g_SOC) in  zip(self.P,self.D,self.SOC_value[1]):   
    #         if 8 <= self.hour <= 17:
    #             print("Charge Pole is Available - U Can Charge..!!!")
                    
    #             if v == 1:
    #                 if v2g_SOC <= 0.5:
    #                     PP2 = -1*self.E2 + p
    #                     print("SoC less than 50% recharge to 0.5")
                              
    #                 elif  0.5< round(v2g_SOC,2) < 0.80:
    #                     PP2 = -1*self.E1 + p
    #                     print("It's controlled charging - G2V")
                     
                     
    #                 elif  0.8 <= round(v2g_SOC,2) < 0.82:
    #                     PP2 =  p
    #                 else:
    #                     PP2 = self.E1 + p
    #                     print("It's controlled charging - V2G")
    #             else:
    #                 PP2 = p
    #         else:
    #             print("Charge Pole is not available....SORRY.....!!!")
    #             PP2 = p
                
    #        # print(round(v2g_SOC,1))    
    #         self.Power2.append(PP2)
    #     #if car choose G2V controlled charging - when SOC is in 0.5 it immediately charge in fast charging mode to reach to 0.5, then it charge in slow charges the car
    #     for  (p,v,G2V_SOC) in  zip(self.P,self.D,self.SOC_value[2]):    
    #         if 8 <= self.hour <= 17:
    #             print("Charge Pole is Available - U Can Charge..!!!")
                    
    #             if v == 1:
                    
    #                 if G2V_SOC <= 0.5:
    #                     PP3 = -1*self.E2 + p
    #                     print("SoC less than 50% recharge to 0.5")
                              
    #                 elif  0.5< G2V_SOC <= 1.0:
    #                     PP3 = -1*self.E1 + p
    #                     print("It's controlled charging - G2V")
                            
    #                 else:
    #                     PP3 = p 
                            
    #             else:
    #                 PP3 = p
                    
    #         else:
    #             print("Charge Pole is not available....SORRY.....!!!")
    #             PP3 = p
    #         self.Power3.append(PP3)
            
    #     #self.pp1=[s1,s2]
    #     self.PP = [self.Power1,self.Power2,self.Power3]
    #     #print("PP_amount: {}".format(self.PP))
    #     return self.PP    
            
    # def battery_SOC(self):
    #     #CP battery SOC calculate here. It starts with 0.5 and it can calculate w.r.t the battery power value
        
    #     soc_Value = []
    #     battery_storage_cappacity = self.batterypole.battery_storage_cap
    
    #     if self.daylist[self.s-1] == 0:
            
    #         self.batterySOC1 = 0.6
    #         self.batterySOC2 = 0.6
    #         self.batterySOC3 = 0.6
            
    #     else:
    #         for m in self.battpowerlist:
    #             soc = -1*m*5 /(battery_storage_cappacity*60)
    #             soc_Value.append(round(soc,2))
                
    #         #print(soc_Value)
    #         self.batterySOC1 += soc_Value[0]
    #         self.batterySOC2 += soc_Value[1]
    #         self.batterySOC3 += soc_Value[2]
        
        
    #     self.SOC_Value_battery = [ self.batterySOC1, self.batterySOC2, self.batterySOC3]  
        
    #     #print("SOC: {}".format(self.SOC_Value_battery))
    #     return self.SOC_Value_battery
            
    # def power_management(self):
    #     self.solar = self.solarpanelagent.calculateSolarEnergy()
    #     SOC_max_value = 0.8
    #     SOC_min_value = 0.2
    #     battery_max_power_limit = self.batterypole.max_power
        
    #     #Delta = [0,1,2]
    #     Delta = []
        
    #     self.EV_Battery =[]
    #     EV_Battery1 = []
    #     EV_Battery2 = []
    #     EV_Battery3 = []
        
    #     #print("Solar: {}".format(self.solar)  )     
    #     self.gridpowerlist = []
    #     self.battpowerlist = []
  
        
    #     for (tp,cp) in zip(self.PP[0],self.P):
    #         evp = -1*( tp - cp)
    #         EV_Battery1.append(evp)
            
    #     for (tp,cp) in zip(self.PP[1],self.P):
    #         evp = -1*( tp - cp)
    #         EV_Battery2.append(evp)

    #     for (tp,cp) in zip(self.PP[2],self.P):
    #         evp = -1*( tp - cp)
    #         EV_Battery3.append(evp)

    #     self.EV_Battery = [EV_Battery1,EV_Battery2,EV_Battery3]
            
    #     #print("self.EV_Battery:{}".format(self.EV_Battery))
        
    #     for evp in self.EV_Battery:
    #         EVP = evp[0] +evp[1]
    #         delta = self.solar - EVP
    #         Delta.append(delta)
           
    #     #print("delta: {}".format(Delta))
    #     #power management: initially solar can supply the power to EV, which is not enough CP battery can give it, then EV can get the energy from grid
        
    #     for (self.delta_P,self.SOCValue) in zip(Delta,self.SOC_Value_battery):
           
        
    #         if self.delta_P <= 0:
    #             if self.SOCValue <= SOC_min_value:
                
    #                 self.Batterypower = 0
                    
    #             else:
                
    #                 if self.delta_P < -1*battery_max_power_limit:
    #                     self.Batterypower = battery_max_power_limit
                      
                        
    #                 else:
    #                     self.Batterypower = -1*self.delta_P
                       
                        
    #         else:
    #             if self.SOCValue >= SOC_max_value:
    #                 self.Batterypower = 0
                    
    #             else:
    #                 if self.delta_P > battery_max_power_limit:
    #                     self.Batterypower = -1*battery_max_power_limit
                       
    #                 else:
    #                     self.Batterypower = -1*self.delta_P
                        
    #         self.Gridpower = -1*(self.delta_P + self.Batterypower)
            
            
    #         self.gridpowerlist.append(self.Gridpower) 
    #         self.battpowerlist.append(self.Batterypower)
    #     #print(self.battpowerlist)
    #     return (   self.gridpowerlist,     self.battpowerlist)
    
        
    def step(self):
    
        # self.EVagent.step()
        # self.solarpanelagent.step()
        
        # self.batterysoc = self.battery_SOC()
        # self.Control_value = self.chargingcontrol()
        # self.stateofcharge = self.SoC()
        # self.powervalue = self.power_management()
        
        # self.s += 1
        self.myFunction()

            