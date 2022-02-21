import pythonia.world as w
import pythonia.county as c
if __name__ == '__main__':
   
    world = w.World("Arda");
    
    county = c.County("Messinia", 3000)
    world.add_county(county)
    
    county = c.County("Laconia", 4000)
    world.add_county(county)
    
    county = c.County("Arcadia", 5000)
    world.add_county(county)

    world.info()
    
    for i in range(30):
        world.advance()
        world.info()