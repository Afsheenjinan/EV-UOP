from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import CanvasGrid, ChartModule, TextElement
from mesa.visualization.UserParam import UserSettableParameter

from model import ConceptModel
from controlagent import *


import asyncio
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


model_params = {    "height": 20, "width": 20   }
grid_positions = [  'uncontrolled', 'V2G', 'G2V'    ]

def visual_portrayal(agent):
   
    portrayal = {
        'scale'         : 1.0,
        'Layer'         : 0,
        'Text'          : type(agent).__name__ +" : "+  agent.unique_id,
        'text_color'    : 'white'
    }

    if type(agent) is SolarPanelAgent:
        # portrayal["Shape"] = "resources/solar.jpg"
        portrayal["Shape"] = "resources/solar.jpg"
        portrayal["Layer"] = 1
        
    elif type(agent) is WeatherAgent:

        portrayal["Shape"] = "resources/temp.png"
                 
    elif type(agent) is EV_Agent:
        if agent.getAvailability() :
            portrayal["Shape"] = "resources/car.png"
        else :
            # portrayal.update({"Shape": "circle", "Color":"white", "Filled": "true", "r": 0.5})
            portrayal = {"Shape": "circle", "Color":"white", "Layer" : 0, "Filled": "true", "r": 0.5}

    elif type(agent) is Charge_pole:
        portrayal["Shape"] = "resources/pole.jpg"
        
    elif type(agent) is Charging_Control_Agent:
        portrayal["Shape"] = "resources/control.png"

    return portrayal

canvas_element = CanvasGrid(visual_portrayal, model_params['width'], model_params['height'], 500, 500)

chart_element = ChartModule(
    [{"Label": "Solar1 : Solar Power (W)", "Color": "#AA0000"}])

chart_element2 = ChartModule(
    [{"Label": "ws1 : Temperature (K)", "Color": "#666666"},{"Label": "ws1 : Irradiance (W/m^2)", "Color": "#14aa00"}])

chart_element3 = ChartModule(
    [{"Label": "1A : Actual Speed (km/h)", "Color": "#14aa00"},{"Label": "1B : Actual Speed (km/h)", "Color": "#154895"}])

# chart_element4 = ChartModule(
#     [{"Label": "SOC_CAR_1", "Color": "#14aa00"},{"Label": "SOC_CAR_2", "Color": "#AA0000"},{"Label": "Battery_SOC", "Color": "#DDA0DD"}]    )\

# chart_element5 = ChartModule(
#     [{"Label": "Car Battery Power(W)", "Color": "#14aa00"}, {"Label": "Car Battery Power_2(W)", "Color": "#AA0000"}]    )

# chart_element6 = ChartModule(
#     [{"Label": "Grid_Power (W)", "Color": "#AA0000"} ,{"Label": "CP_Battery_Power (W)", "Color": "#46FF33"}] )

chart_element7 = ChartModule(
    [{"Label": "1A : Availability", "Color": "#AA0000"} ,{"Label": "1B : Availability", "Color": "#46FF33"}])


choice_option = UserSettableParameter('choice', 'Charge_option', value='uncontrolled', choices = grid_positions)
server = ModularServer(
   ConceptModel, 
   [canvas_element, chart_element, chart_element2, chart_element3, chart_element7],#,chart_element,chart_element4,chart_element5,chart_element6 ],
   "Energy Model",  
   {"width":model_params['width'], "height":model_params['height'], "grid_positions": choice_option}
)


