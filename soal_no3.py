from modul import AntrianRestoran

antrian = AntrianRestoran()

antrian.enqueue("Nasi Goreng")
antrian.enqueue("Mie Goreng")
antrian.enqueue("Capcay")

antrian.dequeue()
antrian.dequeue()

antrian.enqueue("Es Teh")
antrian.dequeue()