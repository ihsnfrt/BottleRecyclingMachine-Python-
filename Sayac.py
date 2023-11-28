class Counter:

    def __init__(self):
        print("Counter is reseted")
        self.total = 0
        self.small_bottle = 0
        self.medium_bottle = 0
        self.large_bottle = 0

    def bottle_counter(self, value):

        if value == 0:
            print("Bottle is not recognized, please check the bottle")


        elif value == 1:
            self.small_bottle += 1


        elif value == 2:
            self.medium_bottle += 1


        elif value == 3:
            self.large_bottle += 1

    def total_bottle(self):
        print(f"Total Small bottle {self.small_bottle}")
        print(f"Total Medium bottle {self.medium_bottle}")
        print(f"Total Large bottle {self.large_bottle}")
