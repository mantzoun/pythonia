import random

import pythonia.industry as ind


MANPOWER_PERCENTAGE = 0.3
MANPOWER_INCR_PCT = 0.011

PROSPERITY_MAX_LEVEL = 100
    
class County:
    name = "empty"
    industry_list = []
    total_goods = 200000
    prosperity = 50
    unemployment = 10
    population = 3000
    manpower = 0
    modifiers = []

    def __init__(self, name, population):
        self.name = name
        self.population = population
        
        random.seed()
        
    def get_name(self):
        return self.name;
    
    def get_population(self):
        return self.population
    
    def info(self):
        print(self.name)
        print("population : " + str(self.population))
        print("prosperity : " + str(self.prosperity))
        print("manpower   : " + str(self.manpower))
        
    def advance_turn(self):
        self.update_population()
        self.update_industry()
        self.update_manpower()
   
    def update_manpower(self):
        target_manpower = self.population * MANPOWER_PERCENTAGE
        diff = target_manpower - self.manpower
        incr = self.population * MANPOWER_INCR_PCT
        
        if abs(diff) < incr:
            self.manpower += diff
        else:
            if diff > 0:
                self.manpower += incr
            elif diff < 0:
                self.manpower -= incr
    
    def update_population(self):
        target_level = self.total_goods / self.population
        print(str(target_level))
        if ( target_level > PROSPERITY_MAX_LEVEL):
            target_level = PROSPERITY_MAX_LEVEL
        
        diff = target_level - self.prosperity
        print(str(diff) + " " + str(target_level))
        self.proesperity = target_level
    
        pct = diff * 0.2 + random.randrange(-2, 3)/100
        print(str(pct))
        
        self.population += pct * self.population / 100
        
    def update_industry(self):
        pass 

    def get_manpower(self):
        return self.manpower