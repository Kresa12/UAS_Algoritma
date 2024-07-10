class AntrianRestoran:

    antrian = []


    def enqueue(self,pesanan):
       
        AntrianRestoran.antrian.append(pesanan)
        print(f"Pesanan {pesanan} ditambahkan ke antrian.")

    def dequeue(self):
        
        if not AntrianRestoran.antrian:
            print("Antrian kosong!")
            return None

        pesanan_depan = AntrianRestoran.antrian[0]
        AntrianRestoran.antrian.pop(0)
        print(f"Pesanan {pesanan_depan} diproses.")
        return pesanan_depan