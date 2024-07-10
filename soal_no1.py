data_mahasiswa = []

while True:
    nim = input("Masukan NIM: ")
    nama = input("Masukan Nama: ")

    data_mahasiswa.append({"nim": nim,"nama": nama})

    tambah_lagi = input("Tambah data mahasiswa lagi? (y/n): ")
    if tambah_lagi.lower() != "y":
      break

    print("\nData Mahasiswa:")

for mahasiswa in data_mahasiswa:
    print(f"NIM: {mahasiswa['nim']}")
    print(f"Nama: {mahasiswa['nama']}")
    print()