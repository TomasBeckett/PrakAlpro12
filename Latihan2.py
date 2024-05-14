def proses_data(data_diri):
    nama, nim, alamat = data_diri
    
    print(f"NIM : {nim}")
    print(f"NAMA : {nama}")
    print(f"ALAMAT : {alamat}")
    
    nim_tuple = tuple(nim)
    print(f"NIM: {nim_tuple}")
    
    nama_depan = tuple(nama.split()[0])
    print(f"NAMA DEPAN: {nama_depan}")
    
    nama_terbalik = tuple(nama.split()[::-1])
    print(f"NAMA TERBALIK: {nama_terbalik}")

data = ('Tomas Becket', '71230985', 'Jakarta')

proses_data(data)

