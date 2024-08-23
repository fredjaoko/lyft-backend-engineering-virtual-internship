from datetime import datetime
from battery.battery import Battery



class SpindlerBattery(Battery):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date



    def needs_service(self):
        date_last = self.lastservicedate
        year_last = date_last.year


        date_today = datetime.today()
        year_today = date_today.year
        
        
        if year_today - year_last >= 3:
            return True
        else:
            return False
        