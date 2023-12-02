from requests import *
from json import *
from pprint import pprint

class Swapi_Object():
    def __init__(self, url):
        self.url = url
        
    def get_info(self):
        info_request = get(self.url)
        return loads(info_request.text)
    
class Ship():
    def __init__(self, info):
        self.ship_name = info['name']
        self.max_atmosphering_speed = info['max_atmosphering_speed']
        self.starship_class = info['starship_class']
        self.pilots = info['pilots']
        
    def resample_pilots_data(self):
        for i in range(len(self.pilots)):
            curr_pilot_swapi_obj = Swapi_Object(self.pilots[i])
            curr_pilot = Pilot(curr_pilot_swapi_obj.get_info())
            self.pilots[i] = curr_pilot.get_data()
        
    def get_data(self):
        self.resample_pilots_data()
        return {"ship_name": self.ship_name, "starship_class": self.starship_class, "max_atmosphering_speed": self.max_atmosphering_speed, "pilots": self.pilots}
    
class Pilot():
    def __init__(self, info):
        self.name = info['name']
        self.height = info['height']
        self.mass = info['mass']
        self.homeworld_url = info['homeworld']
        planet_swapi_obj = Swapi_Object(self.homeworld_url)
        self.homeworld = planet_swapi_obj.get_info()['name']
        
    def get_data(self):
        return {'name': self.name, 'height': self.height, "mass": self.mass, "homeworld": self.homeworld, "homeworld_url": self.homeworld_url}

starship_swapi_object = Swapi_Object("https://swapi.dev/api/starships/10")
ship = Ship(starship_swapi_object.get_info())
ship_data = ship.get_data()

with open("test.json", "w") as file:
    dump(ship_data, file, indent = 4)
pprint(ship_data)