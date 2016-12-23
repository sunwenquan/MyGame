'''
Created on Dec 21, 2016

@author: Hunter Malm
'''

class Player:
    health = 100
    location = 'lab'
    inventory = []
    weight = 0
    
    def __init__(self, name):
        self.name = name
        
        
    def display_health(self):
        print('Health: ' + str(self.health) + '%')
        
        
    def display_location(self):
        print('Location: ' + str(self.location))
        
        
    def set_location(self, location):
        if self.location == location:
            print('>>> ' + str(self.name) + ' is already at the ' + str(location))
        else:
            self.location = location
            print('>>> ' + str(self.name) + ' moved to the ' + str(location))
    
    
    def display_weight(self):
        print('Weight: ' + str(self.weight))
        
        
    def set_name(self, name):
        self.name = name
    
    
    def display_name(self):
        print('Name: ' + str(self.name))
        
        
    def display_inventory(self):
        print('Inventory: ' + str(self.inventory))
        
        
    def add_inventory(self, item):
        self.inventory.append(item)
        
        
    def display_stats(self):
        self.display_name()
        self.display_health()
        self.display_location()
        self.display_inventory()
        self.display_weight()
        
        
class Environment:
    inventory = []
    
    
    def add_item(self, item):
        self.inventory.append(item)
        
        
    def remove_item(self, item):
        self.inventory.remove(item)
    
class Lab(Environment):
    inventory = ['phone']
    
    
    
    