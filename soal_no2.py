import pandas as pd

mahasiswa = [
    ["Mahasiswa 1", 90, 80],
    ["Mahasiswa 2", 50, 60],
    ["Mahasiswa 3", 65, 70],
]

df = pd.DataFrame(mahasiswa, columns=["Nama", "Algoritma dan Struktur Data", "Matematika Numerik"])

rata_rata_mk = df.mean()
print("Rata-rata Nilai per Mata Kuliah:")
print(rata_rata_mk)

rata_rata_mhs = df.mean(axis=1)
print("\nRata-rata Nilai per Mahasiswa:")
print(rata_rata_mhs)
