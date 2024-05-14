def jampesan():
    nama_file = input("Enter a file name: ")

    try:
        with open(nama_file, 'r') as file:
            distribusi_jam = {}

            for baris in file:
                if baris.startswith('From '):
                    kata_kata = baris.split()
                    waktu = kata_kata[5]
                    jam = waktu.split(':')[0]
                    distribusi_jam[jam] = distribusi_jam.get(jam, 0) + 1

            for jam in sorted(distribusi_jam.keys()):
                print(f"{jam} {distribusi_jam[jam]}")

    except FileNotFoundError:
        print(f"File {nama_file} tidak ditemukan.")

jampesan()
