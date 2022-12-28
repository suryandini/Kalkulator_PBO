print("Nama  : SURYANDINI")
print("Nim   : D0221360")
print("Kelas : G TEKNIK INFORMATIKA")


print ("=======================FINAL PBO======================")
class LuasBangunDatar:
    def luas(self):
        pass

class Persegi(LuasBangunDatar):
    def __init__(self, sisi):
        self.sisi = sisi
    def luas(self):
        return self.sisi * self.sisi

class Segitiga(LuasBangunDatar):
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi
        
    def luas(self):
        return self.alas * self.tinggi / 2
    
class Lingkaran(LuasBangunDatar):
    def __init__(self, jari_jari):
        self.jari_jari = jari_jari
        
    def luas(self):
        return 22/7 * self.jari_jari * self.jari_jari

# class bangun ruang    
class VolumeBangunRuang:
    def volume(self):
        pass
    
class Kubus(VolumeBangunRuang):
    def __init__(self, sisi):
        self.sisi = sisi
        
    def volume(self):
        return self.sisi * self.sisi * self.sisi
    
class Limas(VolumeBangunRuang):
    def __init__(self, alas, tinggi_alas, tinggi_limas):
        self.alas = alas
        self.tinggi_alas = tinggi_alas
        self.tinggi_limas = tinggi_limas
        
    def volume(self):
        return 1/3 * ((1/2 * self.alas * self.tinggi_alas) * self.tinggi_limas)

class Tabung(VolumeBangunRuang):
    def __init__(self, jari_jari, tinggi):
        self.jari_jari = jari_jari
        self.tinggi = tinggi
        
    def volume(self):
        return 22/7 * self.jari_jari * self.jari_jari * self.tinggi


# menu utama

def menu_utama():
    while True:
        print(" ")
        print("=" * 50)
        print(" PROGRAM MENGHITUNG LUAS DAN VOLUME ")
        print("=" * 50)
        print("\n1. Luas \n2. Volume \n3. Keluar")
        pilihan = int(input("\nMasukkan Pilihan : "))
        if pilihan == 1:
            menu_luas()
            
        elif pilihan == 2:
            menu_volume()
        
        elif pilihan == 3:
            print(" ")
            print("-" * 50)
            print(" EXIT PROGRAM ".center(50,"="))
            print("-" * 50)
            exit()
        
        else:
            print(" ")
            print("Perintah Tidak Ditemukan !")
            print("Silahkan Pilih Menu Yang Tersedia")
            
# menu luas bangun datar : persegi, segitiga, dan lingkaran.
def menu_luas():
    while True:
        print(" ")
        print("=" * 50)
        print(" PROGRAM MENGHITUNG LUAS ")
        print("=" * 50)
        print("\n1. Persegi \n2. Segitiga \n3. Lingkaran \n4. Kembali")
        subpilihan = int(input("\nMasukkan Pilihan : "))
        if subpilihan == 1:
            print(" ")
            print("-" * 50)
            print(" PROGRAM MENGHITUNG LUAS PERSEGI ")
            print("-" * 50)
            sisi = float(input("Masukkan Sisi Persegi : "))
            persegi = Persegi(sisi)
            print("Luas Persegi : ", persegi.luas())
            print("-" * 50)
            print(" ")

        elif subpilihan == 2:
            print(" ")
            print("-" * 50)
            print(" PROGRAM MENGHITUNG LUAS SEGITGA ")
            print("-" * 50)
            alas = float(input("Masukkan Alas Segitiga : "))
            tinggi = float(input("Masukkan Tinggi Segitiga : "))
            segitiga = Segitiga(alas, tinggi)
            print("Luas Segitiga : ", segitiga.luas())
            print("-" * 50)
            print(" ")

        elif subpilihan == 3:
            print(" ")
            print("-" * 50)
            print(" PROGRAM MENGHITUNG LUAS LINGKARAN ")
            print("-" * 50)
            jari_jari = float(input("Masukkan Jari-Jari Lingkaran : "))
            lingkaran = Lingkaran(jari_jari)
            print("Luas Lingkaran : ", lingkaran.luas())
            #print("Luas Lingkaran : ", round(lingkaran.luas())) ---> jika ingin menggunakan pembulatan
            print("-" * 50)
            print(" ")

        elif subpilihan == 4:
            menu_utama()
        else:
            print(" ")
            print("Perintah Tidak Ditemukan")
            print("Masukkan Perintah Dengan Benar!")

# menu volume bangun ruang : kubus, limas, dan tabung.
def menu_volume():
    while True:
        print(" ")
        print("=" * 50)
        print(" PROGRAM MENGHITUNG VOLUME ".center(50, "="))
        print("=" * 50)
        print("\n1. Kubus \n2. Limas Segitiga \n3. Tabung \n4. Kembali")
        subpilihan = int(input("\nMasukkan Pilihan : "))
        if subpilihan == 1:
            print(" ")
            print("-" * 50)
            print(" PROGRAM MENGHITUNG VOLUME KUBUS ")
            print("-" * 50)
            sisi = float(input("Masukkan panjang sisi : "))
            kubus = Kubus(sisi)
            print("Volume Kubus : ", kubus.volume())
            print("-" * 50)
            print(" ")
            
        elif subpilihan == 2:
            print(" ")
            print("-" * 50)
            print(" PROGRAM MENGHITUNG VOLUME LIMAS SEGITIGA ")
            print("-" * 50)
            alas = float(input("Masukkan nilai alas : "))
            tinggi_alas = float(input("Masukkan  nilai tinggi : "))
            tinggi_limas = float(input("Masukkan tinggi limas : "))
            limas = Limas(alas, tinggi_alas, tinggi_limas)
            print("Volume Limas : ", limas.volume())
            print("-" * 50)
            print(" ")

        elif subpilihan == 3:
            print(" ")
            print("-" * 50)
            print(" PROGRAM MENGHITUNG VOLUME TABUNG ")
            print("-" * 50)
            jari_jari = float(input("Masukkan Jari-Jari Lingkaran Tabung : "))
            tinggi = float(input("Masukkan Tinggi Tabung : "))
            tabung = Tabung(jari_jari, tinggi)
            print("Volume Tabung : ", tabung.volume())
            #print("Volume Tabung : ", round(tabung.volume())) ---> jika ingin menggunakan pembulatan
            print("-" * 50)
            print(" ")
            
        elif subpilihan == 4:
                menu_utama()
        else:
            print(" ")
            print("Perintah Tidak Ditemukan")
            print("Masukkan Perintah Dengan Benar!") 
            
menu_utama()
