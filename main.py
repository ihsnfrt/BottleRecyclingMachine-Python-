from Sayac import Counter
from Ekran import Display
from Motor import Motor
from Sensor import Sensor
from Barkod import Printer
import random

o_display = Display()
o_motor = Motor()
o_sensor = Sensor()
o_barkod = Printer()
rnd = random
power = 1  # kullanici baslata bastiginda

while power:

    o_counter = Counter()
    print("Hos geldiniz")
    decision = input("Ucreti yemek fisi olarak almak istiyorsaniz 1'e "
                     "market fisi olarak almak istiyorsaniz 2'ye basiniz")
    trigger = 1

    while trigger == 1:

        is_sensor_active = o_sensor.get_bottle_sensor()
        if is_sensor_active == 0:

            o_motor.motor_forward()

        elif is_sensor_active == 1:

            read_value = o_sensor.get_bottle_type()
            o_counter.bottle_counter(read_value)

            if read_value == 0:

                o_motor.motor_backward()

            else:

                o_counter.bottle_counter(read_value)
                o_motor.motor_forward()

        list_0_1 = [0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        user_finish_pressed = random.choice(list_0_1)
        if user_finish_pressed == 1:
            total = o_counter.total_bottle()
            o_barkod.print(total)
            trigger = 0
