#!/usr/bin/env python
# coding: utf-8

# In[1]:


import mysql.connector

dataBase = mysql.connector.connect(
    host ="localhost",
    user ="root"
)

#preparing a cursor object
cursorObject = dataBase.cursor()

#creating database 
cursorObject.execute("CREATE DATABASE db_V3922028")


# In[2]:


import mysql.connector 

dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    database="db_V3922028"
)

#preparing a cursor object
cursorObject = dataBase.cursor()

#membuat tabel stok_barang
courseRecord = """CREATE TABLE Stok_barang(
            Id_Barang VARCHAR(20) PRIMARY KEY,
            Nama_Barang VARCHAR(255),
            Harga_Barang INT,
            Stok_Awal INT,
            Barang_Masuk INT,
            Barang_Keluar INT,
            Stok_Akhir INT
            )"""
cursorObject.execute(courseRecord)

#disconnecting from server
dataBase.close()


# In[22]:


import mysql.connector

#Koneksi ke database
dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    database = 'db_V3922028'
)

cursorObject = dataBase.cursor()

#Fungsi untuk menambahkan data ke tabel
def insert_data( Id_Barang, Nama_Barang, Harga_Barang, Stok_Awal, Barang_Masuk, Barang_Keluar, Stok_Akhir ):
    sql = "INSERT INTO Stok_barang (Id_Barang, Nama_Barang, Harga_Barang, Stok_Awal, Barang_Masuk, Barang_Keluar, Stok_Akhir)    VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (Id_Barang, Nama_Barang, Harga_Barang, Stok_Awal, Barang_Masuk, Barang_Keluar, Stok_Akhir)
    
    cursorObject.execute(sql, val)
    dataBase.commit()

    print(" ")
    print("Data berhasil ditambahkan")

#Fungsi untuk menampilkan data dari tabel
def show_data():
    query = "SELECT * FROM Stok_barang"
    
    cursorObject.execute(query)

    myresult = cursorObject.fetchall()

    for x in myresult:
        print(x)
        
    print(" ")
    print("Data berhasil ditampilkan")

#Fungsi untuk mengupdate data di tabel
def update_data(Id_Barang, Nama_Barang, Harga_Barang, Stok_Awal, Barang_Masuk, Barang_Keluar, Stok_Akhir):
    sql = "UPDATE Stok_barang SET Nama_Barang = %s, Harga_Barang = %s, Stok_Awal = %s, Barang_Masuk = %s, Barang_Keluar = %s, Stok_Akhir = %s WHERE Id_Barang = %s"
    val = (Nama_Barang, Harga_Barang, Stok_Awal, Barang_Masuk, Barang_Keluar, Stok_Akhir, Id_Barang)
    
    cursorObject.execute(sql, val)
    dataBase.commit()
    
    print(" ")
    print("Data berhasil diupdate")

#Fungsi untuk menghapus data dari tabel
def delete_data(Id_Barang):
    sql = "DELETE FROM Stok_barang WHERE Id_Barang = %s"
    val = (Id_Barang,)
    
    cursorObject.execute(sql, val)
    dataBase.commit()
    
    print(" ")
    print("Data berhasil dihapus")

#Fungsi untuk mencari data berdasarkan Id_Barang
def search_data(id_barang):
    sql = "SELECT * FROM Stok_barang WHERE Id_Barang = %s"
    val = (id_barang,)

    cursorObject.execute(sql, val)

    myresult = cursorObject.fetchall()

    if myresult:
        print("+------------+----------------------+--------------+-----------+--------------+---------------+------------+")
        print("| Id Barang  | Nama Barang          | Harga Barang | Stok Awal | Barang Masuk | Barang Keluar | Stok Akhir |")
        print("+------------+----------------------+--------------+-----------+--------------+---------------+------------+")
        for row in myresult:
            print("| {:<10} | {:<20} | {:>12,.2f} | {:>9} | {:>12} | {:>13} | {:>10} |".format(
                row[0], row[1], row[2], row[3], row[4], row[5], row[6]
            ))
        print("+------------+----------------------+--------------+-----------+--------------+---------------+------------+")
        print("Data berhasil dicari")
    else:
        print("Id Barang tidak ditemukan.")




#Script untuk pilihan menu
while True:
    print(" ")
    print("=== SISTEM PENCATATAN DATA BARANG ===")
    print("1. Input Data Barang")
    print("2. Tampilkan Data Barang")
    print("3. Update Data Barang")
    print("4. Hapus Data Barang")
    print("5. Cari Data Barang")
    print("6. Keluar Sistem")
    print("-------------------")
    menu = input("Pilih Nomor 1-6 ") #input untuk pilihan menu yang akan dicari
    print(" ")

    #pilihan 1 "insert data"
    if menu == "1":
        Id_Barang = input("Masukkan Id Barang : ")
        Nama_Barang = input("Masukkan Nama Barang : ")
        Harga_Barang = int(input("Masukkan Harga Barang : "))
        Stok_Awal = int(input("Masukkan Stok Awal : "))
        Barang_Masuk = int(input("Masukkan Barang Masuk : "))
        Barang_Keluar = int(input("Masukkan Barang Keluar : "))
        
        #Rumus untuk mencari stok_akhir
        Stok_Akhir = Stok_Awal + Barang_Masuk - Barang_Keluar
        
        #mencetak Stok_Akhir dari rumus sebelumnya
        print("Stok Akhir : ", Stok_Akhir)
        
        insert_data(Id_Barang, Nama_Barang, Harga_Barang, Stok_Awal, Barang_Masuk, Barang_Keluar, Stok_Akhir)
    
    #pilihan 2 "show data"
    elif menu == "2":
        cursorObject.execute("SELECT * FROM Stok_barang")
        data = cursorObject.fetchall()
        if len(data) == 0:
            print("Tidak ada data yang tersimpan")
        else:
            # printing table headers
            print("+------------+----------------------+-----------------+------------+-----------------+------------------+------------+")
            print(f"| {'ID Barang'.ljust(10)} | {'Nama Barang'.ljust(20)} | {'Harga Barang'.ljust(15)} | {'Stok Awal'.ljust(10)} | {'Barang Masuk'.ljust(15)} | {'Barang Keluar'.ljust(15)} | {'Stok Akhir'.ljust(10)} |")
            print("+------------+----------------------+-----------------+------------+-----------------+------------------+------------+")
            # printing table rows
            for row in data:
                print(f"| {str(row[0]).ljust(10)} | {row[1].ljust(20)} | {str(row[2]).ljust(15)} | {str(row[3]).ljust(10)} | {str(row[4]).ljust(15)} | {str(row[5]).ljust(15)} | {str(row[6]).ljust(10)} |")
            print("+------------+----------------------+-----------------+------------+-----------------+------------------+------------+")


    #pilihan 3 "update data"
    elif menu == "3":
        Id_Barang = input("Masukkan Id Barang yang akan diupdate : ")
        Nama_Barang = input("Masukkan Nama Barang baru : ")
        Harga_Barang = int(input("Masukkan Harga Barang baru : "))
        Stok_Awal = int(input("Masukkan Stok Awal baru : "))
        Barang_Masuk = int(input("Masukkan Barang Masuk baru : "))
        Barang_Keluar = int(input("Masukkan Barang Keluar baru : "))
        
        Stok_Akhir = Stok_Awal + Barang_Masuk - Barang_Keluar
        print("Stok Akhir setelah diupdate : ", Stok_Akhir)
        
        update_data(Id_Barang, Nama_Barang, Harga_Barang, Stok_Awal, Barang_Masuk, Barang_Keluar, Stok_Akhir)

    #pilihan 4 "hapus data"
    elif menu == "4":
        Id_Barang = input("Masukkan Id Barang yang ingin dihapus : ")
        
        delete_data(Id_Barang)

    #pilihan 5 "cari data"
    elif menu == "5":
        Id_Barang = input("Masukkan Id Barang yang ingin dicari: ")
        result = search_data(Id_Barang)

    #pilihan 6 "keluar dari program"
    elif menu == "6":
        print("Terima kasih sudah menggunakan Aplikasi kami :D")
        break

    #ketika menginputkan tidak sesuai dengan pilihan yang tertera
    else:
        print("Pilihan anda tidak valid, Mohon coba lagi dan pilihlah dengan benar")


# In[ ]:




