class Buah():

    def __init__(self, nama, warna, rasa):
        self.nama = nama
        self.warna = warna
        self.rasa = rasa

    def set_nama(self, nama_baru):
        self.nama = nama_baru

    def set_warna(self, warna_baru):
        self.warna = warna_baru

    def informasi(self):
        print(f"Nama buah: {self.nama}")
        print(f"Warna: {self.warna}")
        print(f"Rasa: {self.rasa}")


class Mangga(Buah):

    def __init__(self, nama, warna, rasa, vitamin):
        super().__init__(nama, warna, rasa) 
        self.vitamin = vitamin

    def set_vitamin(self, vitamin_baru):
        self.vitamin = vitamin_baru

    def informasi(self):
        super().informasi() 
        print(f"Vitamin: {self.vitamin}")


mangga1 = ("Mangga Gadung", "Kuning", "Manis", "Vitamin A, C, dan E")
mangga2 = ("Mangga Golek", "Hijau Kekuningan", "Manis Legit", "Vitamin B6 dan K")

mangga1.informasi()
print("\n")
mangga2.informasi()
