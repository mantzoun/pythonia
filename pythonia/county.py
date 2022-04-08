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

    prosp_diff = 0
    pop_diff   = 0
    manp_diff  = 0

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
        print("population : " + str(self.population) + " (" + str(self.pop_diff)+ ")")
        print("prosperity : " + str(self.prosperity) + " (" + str(self.prosp_diff)+ ")")
        print("manpower   : " + str(self.manpower) + " (" + str(self.manp_diff)+ ")")
        
    def advance_turn(self):
        self.update_population()
        self.update_industry()
        self.update_manpower()
   
    def update_manpower(self):
        target_manpower = self.population * MANPOWER_PERCENTAGE
        diff = int(target_manpower - self.manpower)
        incr = int(self.population * MANPOWER_INCR_PCT)
        
        if abs(diff) < incr:
            self.manpower += diff
            self.manp_diff = diff
        else:
            if diff > 0:
                self.manpower += incr
                self.manp_diff = incr
            elif diff < 0:
                self.manpower -= incr
                self.manp_diff = incr * (-1)
    
    def update_population(self):
        target_level = int(self.total_goods / self.population)
        print(str(target_level))
        if ( target_level > PROSPERITY_MAX_LEVEL):
            target_level = PROSPERITY_MAX_LEVEL
        
        diff = target_level - self.prosperity
        print(str(diff) + " " + str(target_level))

        self.prosp_diff = target_level - self.prosperity
        self.prosperity = target_level
    
        pct = diff * 0.2 + random.randrange(-2, 3)/100
        print(str(pct))
        
        self.population += int(pct * self.population / 100)
        self.pop_diff = int(pct * self.population / 100)
        
    def update_industry(self):
        pass 

    def get_manpower(self):
        return self.manpower
