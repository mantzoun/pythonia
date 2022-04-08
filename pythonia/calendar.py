import logging

class Calendar:
    day_counter = 0

    dow = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    month = ["January", "February", "March", "April", "May", "June",\
             "July", "August", "September", "October", "November", "December"]

    dom = 1
    moy = 1
    year = 0

    logger = None

    def __init__(self):
        day_counter = 0
        dom = 1
        moy = 1
        self.logger = logging.getLogger(__name__)

    def get_date(self):
        return self.dow[self.day_counter % 7] + ", " + \
               self.month[self.moy - 1] + " " + \
               str(self.dom) + self.get_date_ending() + ", " + \
               "year " + str(self.year)

    def get_date_ending(self):
        switcher = {
        1: "st",
        2: "nd",
        3: "rd"
        }

        return switcher.get( self.dom % 10, "th")

    def advance(self):
        self.day_counter += 1
        self.dom = self.dom + 1
        if self.dom == 31: self.dom = 1

        if self.dom == 1:
            self.moy += 1
            if self.moy == 13: self.moy = 1

        if self.moy == 1 and self.dom == 1:
            self.year += 1

        self.logger.debug("New day : " + self.get_date())
