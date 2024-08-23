from abc import ABC


class  SternmanEngine():
    def __init__(self, warning_light_indicator):
        super().__init__(warning_light_indicator)
        self.warning_light_indicator = warning_light_indicator


    def needs_service(self):
        if self.warning_light_indicator == 'on':
            return True
            
        else:
            return False
        
