class Printer:

    def __init__(self):
        print("printer calibration is done")

    def print(self, total):

        if total ==0:
            print(f"{total} TL tutarindaki yemek fisiniz yazdirilmistir")

        if total ==1:
            print(f"{total} TL Tutarindaki market fisiniz yazdirilmistir")
