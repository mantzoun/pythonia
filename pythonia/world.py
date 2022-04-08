import pythonia.county as c

class World:
    name = "empty"
    county_list = []

    def __init__(self, name):
        self.name = name
        
    def get_name(self):
        return self.name;
    
    def add_county(self, county):
        self.county_list.append(county)
        
    def info(self):
        print(self.name)
        print("=====")
        
        for cnty in self.county_list:
            cnty.info()
            print("---")
            
    def advance(self):
        for cnty in self.county_list:
            cnty.advance_turn()