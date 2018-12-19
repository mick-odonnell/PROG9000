from datetime import datetime as dt
import os
import collections



class Shop_Manager:
    def __init__(self, vehicle_list):
        self.fleet = {}

    def load_cars(self, vehicles):
        # intakes a list of vehicles and creates objects based on their attributes
        # each item in the vehicle list is a dictionary, with the parameters as shown in the
        # vehicle classes
        op_dict = {}

        for asset in vehicles:
            if 'doors' in asset:
                self.fleet[asset['regnum']] = Car(asset['regnum'],
                                               asset['make'],
                                               asset['model'],
                                               asset['efficiency'],
                                               asset['seats'],
                                               asset['daily_cost'],
                                               asset['weekly_cost'],
                                               asset['weekend_cost'],
                                               asset['doors']
                                               )
            else:
                self.fleet[asset['regnum']] = Van(asset['regnum'],
                                               asset['make'],
                                               asset['model'],
                                               asset['efficiency'],
                                               asset['seats'],
                                               asset['daily_cost'],
                                               asset['weekly_cost'],
                                               asset['weekend_cost']
                                               )
        return(op_dict)

class Vehicle:
    def __init__(self, regnum, make, model, efficiency, seats, daily_cost, weekly_cost, weekend_cost):
        self.id = regnum
        self.make = make
        self.model = model
        self.efficiency = efficiency
        self.seats = seats
        self.daily = daily_cost
        self.weekly = weekly_cost
        self.weekend = weekend_cost

class Car(Vehicle):
    def __init__(self, regnum, make, model, efficiency, seats, daily_cost, weekly_cost, weekend_cost,
                 doors):
        super().__init__(self, regnum,  make, model, efficiency, seats, daily_cost, weekly_cost, weekend_cost)
        self.doors = doors

class Van(Vehicle):
    def __init__(self, regnum, make, model, efficiency, seats, daily_cost, weekly_cost, weekend_cost):
        super().__init__(self, regnum, make, model, efficiency, seats, daily_cost, weekly_cost, weekend_cost)


