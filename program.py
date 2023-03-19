import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
from pandas import DataFrame
import os

# Class data processing
class dataProcessing:
    def __init__(self, file):
        self.file = pd.read_csv(file)
    # Mengembalikan nilai data asli
    def dataAsli(self):
        return self.file
    # Mengembalikan daftar nama kolom dalam bentuk list
    def tampilKolom(self):
        print("~~ Nama Kolom ~~")
        daftarKolom = []
        index = 0
        for namaKolom in self.file:
            daftarKolom.append(namaKolom)
            print(f"{index}. {namaKolom}")
            index+=1
        return daftarKolom
    # Membersihkan variabel missing
    def cleansingData(self):
        self.file.loc[2] = ["B456", "kaos", 8, "sandang"]
        self.file.loc[3] = ["B457", "sabuk", 9, "sandang"]
        self.file.loc[4] = ["B455", "anduk", 17, "sandang"]
        self.file.loc[7] = ["B126", "sate", 16, "pangan"]
        self.file.loc[8] = ["B447", "celana", 20, "sandang"]
        return self.file
    # mengubah data ke dalam bentuk numerik
    def toNumerik(self):
        dataset = dataProcessing.cleansingData(self)
        le = LabelEncoder()
        for kolom in dataset.columns.values:
            if dataset[kolom].dtypes == 'object':
                data = dataset[kolom].append(dataset[kolom])
                le.fit(data.values)
                dataset[kolom]= le.transform(dataset[kolom])
        return dataset
    # menscaling data
    def scaling(self):
        dataset = dataProcessing.toNumerik(self)
        scale = MinMaxScaler()
        label = dataProcessing.tampilKolom(self)
        dataLoc = dataset.loc[0:, label]
        dataLoc = scale.fit_transform(dataLoc)

        dataset.loc[0:, label] = dataLoc
        return dataset
        


# nama file
namaFile = "soal.csv"

# Perulangan untuk menampilkan menu
while True:
    print("\n=====================\n Menu Pemrosesan data\n=====================")
    print("1. Print Data Asli")
    print("2. Print Data Bersih")
    print("3. Hitung Missing Value")
    print("4. Ubah data ke numerik")
    print("5. Prosess feature scalling")
    print("0. Keluar")
    print("=====================")
    # input pilihan menu
    pilih = input("Pilih(0~5) : ")
    print("=====================")
    if pilih == "1":
        # menjalankan perintah cls pada terminal windows
        os.system('cls')
        print("~~~~~~Data Asli~~~~~~")
        # mencetak data yang dipanggil dari class
        print(dataProcessing(namaFile).dataAsli())
    elif pilih == "2":
        os.system('cls')
        print("~~~~~~Data Bersih~~~~~~")
        dataupdate = dataProcessing(namaFile).cleansingData()
        # mencetak data yang dipanggil dari class
        print(dataupdate)
    elif pilih == "3":
        os.system('cls')
        while True:
            daftarKolom = dataProcessing(namaFile).tampilKolom()
            dataAsli = dataProcessing(namaFile).dataAsli()
            print("\n=====================")
            try:
                # input pilihan kolom
                indexKolom = int(input("Pilih Kolom : "))
                namaKolom = daftarKolom[indexKolom]
                # menjumlahkan data missing yang ada di kolom yang diinputkan
                hitungNull = dataAsli[namaKolom].isnull().sum()
                break
            except:
                print("\n=====================")
                print("Pilih index yang ada!")
                print("=====================\n")
                continue
        print("=====================")
        print(f"Data missing pada kolom {namaKolom} adalah {hitungNull}")

    elif pilih == "4":
        
        dataNumerik = dataProcessing(namaFile).toNumerik()
        os.system('cls')
        print("~~~~~~~~~~ Data Numerik ~~~~~~~~~~")
        print(dataNumerik)


    elif pilih == "5":
        dataScaling = dataProcessing(namaFile).scaling()
        os.system('cls')
        print("~~~~~~~~~~ Data yang sudah di-Scaling ~~~~~~~~~~")
        print(dataScaling)



    elif pilih == "0":
        # Menghentikan perulangan/keluar dari looping menu
        break
    # kondisi saat input pilihan menu tidak valid
    else:
        print("Pilihan Tidak Ada")


        
