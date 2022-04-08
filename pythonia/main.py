import time
import logging

import pythonia.world as w
import pythonia.county as c
import pythonia.calendar as cal


if __name__ == '__main__':

    logging.basicConfig(filename='pythonia.log', filemode='w', level=logging.DEBUG)

    logger = logging.getLogger(__name__)
    logger.debug("START")

    world = w.World("Arda");

    calendar = cal.Calendar()

    county = c.County("Messinia", 3000)
    world.add_county(county)

    county = c.County("Laconia", 4000)
    world.add_county(county)

    county = c.County("Arcadia", 5000)
    world.add_county(county)

    world.info()

    day = 0
    while ( True ):
        with open('date.html', 'w') as f:
            f.write(calendar.get_date())

        #world.advance()

        calendar.advance()
        time.sleep(3600)


