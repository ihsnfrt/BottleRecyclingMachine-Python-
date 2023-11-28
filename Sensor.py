import random

class Sensor:

    def __init__(self):
        print("Sensor calibration is done!")

    def get_bottle_type(self):
        bottle_types = [0, 1, 2, 3] #0 tanimsiz
                                    # 1 kucuk boy
                                    # 2 orta boy
                                    # 3 buyuk boy
        read_bottle_type = random.choice(bottle_types)
        return read_bottle_type

    def get_bottle_sensor(self):

        bottle_on_off = [0, 1]
        choice = random.choice(bottle_on_off)

        return choice
