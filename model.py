class Transport:
    def __init__(self,nomi,tezligi):
        self.nomi = nomi
        self.tezligi = tezligi

    def get_nomi(self):
        return self.nomi

    def get_tezligi(self):
        return self.tezligi

    def set_nomi(self,nomi):
        self.nomi = nomi

    def set_yoshi(self,tezligi):
        self.tezligi = tezligi

class Velosiped(Transport):
    def __init__(self,nomi,tezligi,):
        super().__init__(nomi,tezligi)


car = Transport('BMW', 120)
print(f"Avtomobil yo‘lda yuryapti. Tezligi: {car.tezligi} km/soat")
velosiped = Velosiped('BBB',25)
print(f"Velosiped pedal bosmoqda. Tezligi: {velosiped.tezligi} km/soat")
