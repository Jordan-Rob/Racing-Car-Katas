import unittest

from tire_pressure_monitoring import Alarm

"""
Create child class to inherit Alarm for Testing purposes
in specific test cases, this provides a workaround for the random 
psi_pressure_value in parent Alarm class' check() method.
When can set psi_pressure_value as a property in child class
"""
class TestingAlarm(Alarm):

    def __init__(self, psi_pressure_value):
        super().__init__()
        self.psi_pressure_value = psi_pressure_value
    
    def check(self):
        psi_pressure_value = self.psi_pressure_value
        if psi_pressure_value < self._low_pressure_threshold \
                or self._high_pressure_threshold < psi_pressure_value:
            self._is_alarm_on = True

class AlarmTest(unittest.TestCase):

    # modify alarm varaibles to use TestingAlarm class above
     
    def test_alarm_is_off_by_default(self):
        alarm = TestingAlarm(0)
        assert not alarm.is_alarm_on

    def test_property_validation(self):
        alarm = TestingAlarm(11)

        assert alarm._high_pressure_threshold == 21
        assert alarm._low_pressure_threshold == 17
        assert alarm._is_alarm_on ==False
        assert not alarm._sensor == None


# Possible Test cases
    
# validate properties that we need:
# loW_pressure_threshold
# high_pressure_threshold
# sensor
# is_alarm_on = False
    
# check() tests
# is_alarm_on  psi_pressure_value < low_pressure_threshold
# high_pressure_threshold < psi_pressure_value
        
"""
Note: randomness of psi_pressure_value creates 
difficulty testing Alarm's check() for both 
low and high pressure thresholds
"""
