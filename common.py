import json
from fuzzywuzzy import fuzz

class MapLocations:
    def __init__(self):
        self.maps = {}
        try:
            with open('maps.json') as json_file:
                self.maps = json.load(json_file)
        except FileNotFoundError:
            print("Error: JSON file not found")
        except:
            print("Error: Failed to load map data")
    
    def get_location(self, map_name):
        for key in self.maps.keys():
            if fuzz.partial_ratio(key, map_name) >= 90:
                return self.maps[key]
        return 'Location not found'
