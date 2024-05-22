import unittest

from tire_pressure_monitoring import Alarm

class AlarmTest(unittest.TestCase):

    def test_alarm_is_off_by_default(self):
        alarm = Alarm()
        assert not alarm.is_alarm_on

    def test_property_validation(self):
        alarm = Alarm()

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
