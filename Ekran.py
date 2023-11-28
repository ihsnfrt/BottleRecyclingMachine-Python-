class Display:

    def __init__(self):
        print("Display is calibrated")

    def display_power_on(self):
        print("Display is opened")

    def display_power_of(self):
        print("Display is closed")

    def display_write_to_screen(self, numb):
        print("***********************")
        print(f"Passed Bottle is {numb}")
        print("************************")
