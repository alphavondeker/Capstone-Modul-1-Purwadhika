#CAPSTONE
#DAGANG BESI

import os
import sys
import numbers

from tabulate import tabulate

#data Pipa Galvanis
data={'050186bsa':
        {"Diameter":0.5,"Tebal":1.8,"Panjang":6,"Berat":5.19,"Harga":136000,"Tipe":"BSA","Stock":20},
          '050206lgh':
          {"Diameter":0.5,"Tebal":2.0,"Panjang":6,"Berat":5.68,"Harga":147000,"Tipe":"LGH","Stock":25},
          "075186med":
          {"Diameter":0.75,"Tebal":1.8,"Panjang":6,"Berat":6.63,"Harga":167000,"Tipe":"MEDIUM","Stock":18},
          "075236lgh":
          {"Diameter":0.75,"Tebal":2.3,"Panjang":6,"Berat":8.28,"Harga":209000,"Tipe":"LGH","Stock":18}
          }
judul = ["Kode", "Diameter (inch)", "Tebal (mm)", "Panjang (m)", "Berat (kg)", "Harga","Tipe","Stock"]

def itemlist(): # katalog lengkap
    print()
    print("Katalog Lengkap Pipa Galvanis")
    listflattened=[]
    for key,val in data.items():
        listflattened.append([key,val["Diameter"],val["Tebal"],val["Panjang"],val["Berat"],val["Harga"],val["Tipe"],val["Stock"]])

    print(tabulate(listflattened, headers=judul, tablefmt="pipe"))
    print()
      
def deleteitem(): # Menghapus pipa
    print()
    while True:
        kodehapus=input("Masukkan kode pipa yang akan dihapus : ").lower()
        listflattened=[]
        for key,val in data.items():
            if kodehapus == key:
                listflattened.append([key,val["Diameter"],val["Tebal"],val["Panjang"],val["Berat"],val["Harga"],val["Tipe"],val["Stock"]])
                break
            else:
                continue
        print()
        print(f"Spesifikasi pipa {kodehapus}")
        print(tabulate(listflattened, headers=judul ,tablefmt="pipe"))
        
        if kodehapus in data:
            print()
            yornomenu3=input("Apakah kode pipa yang akan dihapus sudah benar? y/n : ")
            if yornomenu3 == "y":
                del data[kodehapus]
                print()
                itemlist()
                print()
                print("Berhasil Diperbaharui!")
                print()
                break
            elif yornomenu3 == "n":
                print()
            else:
                print("Input yang dimasukkan tidak valid! Coba lagi!")
            
        else:
            print("Kode pipa tidak ditemukan! Coba Lagi!")

def menu1(): # ANGKA MENU 1 List Pipa Galvanis
    while True:
        print()
        print("Menu Katalog Pipa Galvanis")
        print("0. Kembali ke Menu Utama")
        print("1. Menampilkan Seluruh Katalog")
        print("2. Menampilkan Pipa berdasarkan Diameter")
        print("3. Menampilkan Pipa berdasarkan Tebal")
        print("4. Menampilkan Pipa berdasarkan Panjang")
        print("5. Menampilkan Pipa berdasarkan Tipe")
        print("6. Menampilkan Pipa berdasarkan Kode")
        print()
        inputmenu1=input("Masukkan Angka Menu yang ingin dijalankan : ")

        if inputmenu1=="0":
            os.system('cls')
            break

        elif inputmenu1=="1":
            os.system('cls')
            itemlist()
        
        elif inputmenu1=="2": # Berdasarkan Diameter
            while True:    
                try:
                    inputdiameter=float(input("Masukkan Diameter (inch): "))
                    listflattened=[]
                    for key,val in data.items():
                        if inputdiameter == val["Diameter"]:
                            listflattened.append([key,val["Diameter"],val["Tebal"],val["Panjang"],val["Berat"],val["Harga"],val["Tipe"],val["Stock"]])
                            print()
                        else:
                            continue
                    os.system('cls')
                    print(f"Katalog pipa dengan diameter {inputdiameter} m")
                    print(tabulate(listflattened, headers=judul, tablefmt="pipe"))
                    print()
                    break
                except ValueError:
                            print("Input tidak Valid! Coba lagi!")
                            print()

        elif inputmenu1=="3": # Berdasarkan Tebal
            while True:    
                try:
                    inputtebal=float(input("Masukkan Tebal Pipa (mm) : "))
                    listflattened=[]
                    for key,val in data.items():
                        if inputtebal == val["Tebal"]:
                            listflattened.append([key,val["Diameter"],val["Tebal"],val["Panjang"],val["Berat"],val["Harga"],val["Tipe"],val["Stock"]])
                            print()
                        else:
                            continue
                    os.system('cls')
                    print(f"Katalog pipa dengan tebal {inputtebal} m")
                    print(tabulate(listflattened, headers=judul, tablefmt="pipe"))
                    print()
                    break
                except ValueError:
                            print("Input tidak Valid! Coba lagi!")
                            print()        

        elif inputmenu1=="4": # Berdasarkan Panjang
            while True:    
                try:
                    inputpanjang=float(input("Masukkan Panjang Pipa (m) : "))
                    listflattened=[]
                    for key,val in data.items():
                        if inputpanjang == val["Panjang"]:
                            listflattened.append([key,val["Diameter"],val["Tebal"],val["Panjang"],val["Berat"],val["Harga"],val["Tipe"],val["Stock"]])
                            print()
                        else:
                            continue
                    os.system('cls')
                    print(f"Katalog pipa dengan panjang {inputpanjang} m")
                    print(tabulate(listflattened, headers=judul, tablefmt="pipe"))
                    print()
                    break
                except ValueError:
                            print("Input tidak Valid! Coba lagi!")
                            print() 

        elif inputmenu1=="5": # Berdasarkan Tipe
            tipebaru=(input("Masukkan tipe pipa : ")).upper()
            if tipebaru.isalpha()==False:
                print("Input tidak Valid! Coba lagi!")
            else:
                listflattened=[]
                for key,val in data.items():
                    if tipebaru == val["Tipe"]:
                        listflattened.append([key,val["Diameter"],val["Tebal"],val["Panjang"],val["Berat"],val["Harga"],val["Tipe"],val["Stock"]])
                        print()
                    else:
                        continue
                os.system('cls')
                print(f"Katalog pipa dengan Tipe {tipebaru} m")
                print(tabulate(listflattened, headers=judul, tablefmt="pipe"))
                print()
        elif inputmenu1=="6": # Berdasarkan Kode
            kodecari=(input("Masukkan kode pipa : ")).lower()
            if kodecari not in data:
                print("Kode tidak ada dalam katalog!")
            else:
                listflattened=[]
                for key,val in data.items():
                    if kodecari == key:
                        listflattened.append([key,val["Diameter"],val["Tebal"],val["Panjang"],val["Berat"],val["Harga"],val["Tipe"],val["Stock"]])
                        print()
                    else:
                        continue
                os.system('cls')
                print(f"Katalog pipa dengan kode {kodecari} ")
                print(tabulate(listflattened, headers=judul, tablefmt="pipe"))
                print()
                
def additem(): # ANGKA MENU 2 update Pipa
    print()   
    while True:
        print()
        print("Menu Update Pipa")
        print("1. Menambahkan Pipa baru")
        print("2. Menambah Stock Pipa")
        print("3. Mengurangi Stock Pipa")
        print("4. Mengubah Harga Pipa")
        print("5. Menghapus Pipa")
        print("0. Kembali ke Menu Utama")
        print()
        inputmenu2=input("Masukkan Angka Menu yang ingin dijalankan : ")
    
        if inputmenu2=="1": #1. Menambahkan Pipa baru
            while True:
                while True:
                    print()
                    kodebaru=input("Masukkan Kode pipa baru : ").lower() 
                    if kodebaru in data:
                        print("Kode sudah terdaftar di katalog!")
                    
                    elif len(kodebaru)!=9 or kodebaru.isalnum()==False:
                        print("Kode yang dimasukkan tidak valid!")
                    else:
                        break
                
                while True:
                    try:
                        diameterbaru=float(input("Masukkan Diameter pipa : "))
                        break
                    except ValueError:
                        print("Input tidak Valid! Coba lagi!")

                while True:
                    try:
                        tebalbaru=float(input("Masukkan tebal pipa : "))
                        break
                    except ValueError:
                        print("Input tidak Valid! Coba lagi!")

                while True:
                    try:
                        panjangbaru=float(input("Masukkan panjang pipa : "))
                        break
                    except ValueError:
                        print("Input tidak Valid! Coba lagi!")

                while True:
                    try:
                        beratbaru=float(input("Masukkan berat pipa : "))
                        break
                    except ValueError:
                        print("Input tidak Valid! Coba lagi!")
                
                while True:
                    try:
                        hargabaru=float(input("Masukkan Harga pipa : "))
                        break
                    except ValueError:
                        print("Input tidak Valid! Coba lagi!")
                
                while True:
                    tipebaru=(input("Masukkan tipe pipa : ")).upper()
                    if tipebaru.isalpha()==False:
                        print("Input tidak Valid! Coba lagi!")
                    else:
                        break
                while True:
                    try:
                        stockbaru=float(input("Masukkan stock pipa : "))
                        break
                    except ValueError:
                        print("Input tidak Valid! Coba lagi!")
                
                yornomenu2=input("Apakah data yang dimasukkan sudah benar? y/n : ")
                if yornomenu2 == "y":
                    print()
                    data[kodebaru]={"Diameter":diameterbaru, "Tebal":tebalbaru, "Panjang":panjangbaru, "Berat":beratbaru, "Harga":hargabaru,"Tipe":tipebaru,"Stock":stockbaru}
                    print("Berhasil Diperbaharui!")
                    itemlist()
                    print()
                    break
                elif yornomenu2 == "n":
                    print()
                else:
                    print("Input yang dimasukkan tidak valid! Coba lagi!")
        
        elif inputmenu2=="2": #2. Menambah Stock Pipa"
            while True:    
                try:
                    kodeupdate=(input("Masukkan Kode Pipa yang akan diperbarui Stock: "))
                    if kodeupdate not in data:
                        print("Kode yang dimasukkan tidak terdapat pada katalog. Silahkan masukkan kembali kode")
                    else:
                        print()
                        print(f"Stock pipa {kodeupdate} : {data[kodeupdate]["Stock"]}")
                        print()
                        plusstock=int(input("Masukkan Jumlah Stock yang akan ditambah : "))
                        yornoupdate=input(f"Apakah input sudah benar? ({plusstock}) y/n : ")
                        if yornoupdate == "y":
                            data[kodeupdate]["Stock"]=(data[kodeupdate]["Stock"])+plusstock
                            os.system('cls')
                            print(f"Stock Berhasil diperbaharui! (Kode pipa : {kodeupdate}, Stock : {data[kodeupdate]["Stock"]})")
                            break
                        elif yornoupdate == "n":
                            print()
                        else:
                            print("Input yang dimasukkan tidak valid! Coba lagi!")
                except ValueError:
                            print("Input tidak Valid! Coba lagi!")
                            print()

        elif inputmenu2=='3': #3. Mengurangi Stock Pipa
            while True:
                try:
                    kodeminus=(input("Masukkan Kode Pipa yang akan diperbarui Stock: "))
                    if kodeminus not in data:
                            print("Kode yang dimasukkan tidak terdapat pada katalog. Silahkan masukkan kembali kode")
                    else:
                        print()
                        print(f"Stock pipa {kodeminus} : {data[kodeminus]["Stock"]}")
                        print()
                        minusstock=int(input("Masukkan Jumlah Stock yang akan dikurangi : "))
                        yornominus=input(f"Apakah input sudah benar? ({minusstock}) y/n : ")
                        if yornominus == "y":
                            if (data[kodeminus]["Stock"])-minusstock < 0:
                                print()
                                print("Jumlah yang dimasukkan melebihi stock yang ada!")
                                print()
                            else:
                                data[kodeminus]["Stock"]=(data[kodeminus]["Stock"])-minusstock
                                os.system('cls')
                                print(f"Stock Berhasil diperbaharui! (Kode pipa : {kodeminus}, Stock : {data[kodeminus]["Stock"]})")
                                break
                        elif yornominus == "n":
                            print()
                        else:
                            print("Input yang dimasukkan tidak valid! Coba lagi!")
                except ValueError:
                    print("Input tidak Valid! Coba lagi!")
                    print()

        elif inputmenu2=='4': #4. Mengubah Harga Pipa
            while True:
                kodeharga=input("Masukkan kode pipa yang akan dihapus : ").lower()
                
                if kodeharga in data:
                    try:
                        inputharga=float(input(f"Masukkan Harga baru pipa kode {kodeharga} : "))
                        print(f"Kode : {kodeharga}  Harga Sekarang : {data[kodeharga]["Harga"]}  Harga Baru : {inputharga}")
                        print()
                    except ValueError:
                        print()
                        print("Input Tidak Valid! Coba Lagi!")

                    yornomenu3=input("Apakah kode pipa yang akan dihapus sudah benar? y/n : ")
                    if yornomenu3 == "y":
                        data[kodeharga]["Harga"]=inputharga
                        print()
                        itemlist()
                        print()
                        print("Berhasil Diperbaharui!")
                        print()
                        break
                    elif yornomenu3 == "n":
                        print()
                    else:
                        print("Input yang dimasukkan tidak valid! Coba lagi!")
                    
                else:
                    print("Kode pipa tidak ditemukan! Coba Lagi!")

        elif inputmenu2=='5': #5. Menghapus Pipa
            os.system('cls')
            itemlist()
            deleteitem()

        elif inputmenu2=="0":
            os.system('cls')
            break
        
        else:
            print()
            print("Input tidak valid! Coba lagi!") 
        
def beli():
    os.system('cls')    
    dictbeli={}

    while True:
        itemlist()
        kodebeli=input("Masukkan kode pipa yang akan dibeli : ")
        if kodebeli=="":
            break
        elif kodebeli not in data:
            print("Kode yang dimasukkan tidak terdapat pada katalog. Silahkan masukkan kembali kode")
        else:
            while True:
                print(f"Spesifikasi pipa {kodebeli} adalah")
                for key,val in data[kodebeli].items():
                    print(f"{key} : {val}")
                jumlahbeli=int(input("Masukkan jumlah pipa yang akan dibeli : "))
                if jumlahbeli > data[kodebeli]["Stock"]:
                    print()
                    print("Mohon Maaf pesanan melebihi stock")
                    print()
                else:
                    dictbeli[kodebeli]=jumlahbeli
                    break
            
        yornobelilagi=input("Apakah anda ingin membeli jenis pipa lain? y/n : ")
        if yornobelilagi == "n":
            break
        elif yornobelilagi == "y":
            os.system('cls')
            print()
            listflatcart=[]
            headercart=["Kode","Jumlah"]
            for key,val in dictbeli.items():
                listflatcart.append([key,val])
            print("Keranjang Belanja")
            print(tabulate(listflatcart,headers=headercart,tablefmt="pipe"))
            print()
        else:
            print("Input yang dimasukkan tidak valid! Coba lagi!")
        

    #Pengurangan Stock
    for key,val in dictbeli.items():
        data[key]["Stock"]=data[key]["Stock"]-val

    print()
    print("Detail Belanja")

    totalharga=0
    for key,val in dictbeli.items():
        print(f"{key} : {val} x Rp.{data[key]["Harga"]} = Rp.{val*data[key]["Harga"]}")
        totalharga=totalharga+(val*data[key]["Harga"])

    totalberat=0
    for key,val in dictbeli.items():
        totalberat=totalberat+(val*data[key]["Berat"])
        
    print()
    print(f"Total harga pesanan anda adalah Rp. {totalharga} ")
    print(f"Total berat pesanan anda adalah {round(totalberat,2)} kg")

# MAIN PROGRAM
while True:
    print()
    print("Selamat Datang di Toko Pipa Besi Galvanis")
    print("List Menu\n 1. Menampilkan Daftar Besi\n 2. Update Katalog Pipa\n 3. Menu Pembelian\n 4. Exit Program")
    print()
    angkamenu=input("Masukkan angka Menu yang ingin dijalankan : ")
    
    if angkamenu == "4": # Exit Program
        print()
        print("Terima Kasih!")
        break

    elif angkamenu=="1": # Menampilkan katalog daftar besi
        os.system('cls')
        print()
        menu1()
    
    elif angkamenu=="2": # Menambah pipa baru
        os.system('cls')
        itemlist()
        additem()
    
    elif angkamenu=="3": # Menu pembelian
        beli()