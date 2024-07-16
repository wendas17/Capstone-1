from tabulate import tabulate


database = [
        {'Kode':1,'Nama': 'Lestari Jaya Makmur', 'Alamat': 'Jl. Merdeka No.1', 'Kota': 'Jakarta', 'Telepon': '021-1234567', 'Tipe Bisnis':'Elektronik'},
        {'Kode':2,'Nama': 'Apotek Sehat Selalu', 'Alamat': 'Jl. Diponegoro No.15', 'Kota': 'Yogyakarta', 'Telepon': '0274-5432109', 'Tipe Bisnis':'Apotek'},
        {'Kode':3,'Nama': 'Klinik Kesehatan Medika', 'Alamat': 'Jl. Ahmad Yani No.25', 'Kota': 'Bandung', 'Telepon': '022-5432109', 'Tipe Bisnis':'Klinik Kesehatan'},
        {'Kode':4,'Nama': 'Rumah Makan Sederhana', 'Alamat': 'Jl. Pahlawan No.5', 'Kota': 'Bandung', 'Telepon': '022-7654321', 'Tipe Bisnis':'Rumah Makan'},
        {'Kode':5,'Nama': 'Bengkel Mobil Andalan', 'Alamat':'Jl. Soekarno Hatta No.10', 'Kota': 'Surabaya', 'Telepon': '031-8765432', 'Tipe Bisnis':'Bengkel Mobil'},
        {'Kode':6,'Nama': 'Salon Kecantikan Anggun', 'Alamat': 'Jl. Kartini No.20', 'Kota': 'Semarang', 'Telepon': '024-6543210', 'Tipe Bisnis':'Salon Kecantikan'},
        {'Kode':7,'Nama': 'Hotel Merdeka', 'Alamat': 'Jl. Malioboro No.50', 'Kota': 'Yogyakarta', 'Telepon': '0274-8765432', 'Tipe Bisnis':'Hotel'},
        {'Kode':8,'Nama': 'Toko Buku Maju', 'Alamat': 'l. Pemuda No.40', 'Kota': 'Surabaya', 'Telepon': '031-7654321', 'Tipe Bisnis':'Toko Buku'},
        {'Kode':9,'Nama': 'Restoran Padang Bundo', 'Alamat': 'Jl. Sudirman No.30', 'Kota': 'Jakarta', 'Telepon': '021-6543210', 'Tipe Bisnis':'Rumah Makan'}
]

#validasi inputan angka
def input_num(prompt):

    inputan = input(prompt)
    if inputan.isdigit():
        return int(inputan)
    else:
        print('Format Salah, Inputan Anda Bukan Angka')
        input_num(prompt)
    
#validasi inputan alfabet
def input_alpha(prompt):
        inputan = input(prompt)
        if inputan.isalpha():
            return inputan
        else:
            print('Format Salah, Inputan Anda Bukan Alfabet')
            input_alpha(prompt)
#Read Data
def read_data(data):
    print(tabulate(data, headers = 'keys', tablefmt = 'pretty'))

#Validasi kode unik
def kode_unik(id):
    for entry in database:
        if entry['Kode'] == id:
            return False
    return True

#Input Kode baru
def input_kode(prompt):
   while True:
    
          inputan = input_num(prompt)
          if kode_unik(inputan):
              return inputan
          else:
            print('Kode sudah ada')

#Create Data
def create_data():
    while True:
          Kode = input_kode('Masukkan Kode: ')
           
          Nama = input('Masukkan Nama: ').title()

          Alamat = input('Masukkan Alamat: ').title()

          Kota = input('Masukkan Kota: ').title()
          while not Kota.isalpha():
              print('Format Salah, Inputan Anda Bukan Alfabet')
              Kota = input('Masukkan Kota: ').title()
          
          while True :
                Telepon = input('Masukkan 10 digit no Telepon beserta kode wilayah: ')
                if  len(Telepon) >= 10: 
                      Telepon = Telepon[:-7] + '-' + Telepon[-7:]
                      break
                else:
                      print('Format Telepon salah')

          Tipe_Bisnis = input('Masukkan Tipe Bisnis: ').title()
          while not Tipe_Bisnis == str(Tipe_Bisnis):
              print('Format Salah, Inputan Anda Bukan Alfabet')
              Tipe_Bisnis = input('Masukkan Tipe Bisnis: ').title()

          database.append({'Kode': Kode, 'Nama': Nama, 'Alamat': Alamat, 'Kota': Kota, 'Telepon': Telepon, 'Tipe Bisnis': Tipe_Bisnis})
          print('Data Berhasil Ditambahkan')
          read_data(database)
          break
         



#Update Data
def update_data():
    row = input_num('Masukkan Kode Data yang akan diupdate: ')-1

    kolom = input('Masukkan Nama Kolom yang akan diupdate: ').title()
    if kolom in database[row].keys():
        if kolom == 'Kode':
            database[row][kolom] = input_num('Masukkan Kode Baru: ')
        elif kolom == 'Nama':
            database[row][kolom] = input('Masukkan Nama Baru: ').title ()
        elif kolom == 'Alamat':
            database[row][kolom] = input('Masukkan Alamat Baru: ').title ()
        elif kolom == 'Kota':
            database[row][kolom] = input_alpha('Masukkan Kota Baru: ').title ()
        elif kolom == 'Telepon':
            database[row][kolom] = input('Masukkan Telepon Baru: ')
        elif kolom == 'Tipe Bisnis':
            database[row][kolom] = input_alpha('Masukkan Tipe Bisnis Baru: ').title ()

    else:
        print('Kolom tidak ada')

#Filter

def filter_kota(database, kota):
    hasil = [data for data in database if data['Kota'] == kota]
    if not hasil:
        print('Kota tidak ada')
    return hasil

def filter_tipe_bisnis(database, tipe_bisnis):
    hasil = [data for data in database if data['Tipe Bisnis'] == tipe_bisnis]
    if not hasil:
        print('Tipe Bisnis tidak ada')
    return hasil


def filter_data():
    while True:
        print('''
        -- Filter By --

        1. Kota
        2. Tipe Bisnis
        3. Exit
        ''')
        inputan = input('Pilih Angka pada Menu: ')
        if inputan == '1':
            kota = input('Masukkan Kota: ').title()
            hasil = filter_kota(database, kota)
            print(hasil)
        elif inputan == '2':
            tipe_bisnis = input('Masukkan Tipe Bisnis: ').title()
            hasil = filter_tipe_bisnis(database, tipe_bisnis)
            print(hasil)
        elif inputan == '3':
            break
        else:
            print('Menu tidak ada')

#Delete Data
def delete_data():
  for row,input in enumerate(database):
    row = input_num('Masukkan Kode Data yang akan dihapus: ')
    if input ['Kode'] == row:
        del database[(row-1)]
        return True
  return False


def main():
    while True:
        print('''
        -- DAFTAR KONTAK TELEPON --

        1. Read Data
        2. Create Data
        3. Update Data
        4. Filter Data
        5. Delete Data
        6. Exit
        ''')

        inputan = input('Pilih Angka pada Menu: ')
        if inputan == '1':
            read_data(database)
        elif inputan == '2':
            create_data()
        elif inputan == '3':
            update_data()
        elif inputan == '4':
            filter_data()
        elif inputan == '5':
            delete_data()
        elif inputan == '6':
            print('Exit')
            break # keluar

        else:
            print('menu tidak ada')


main()

