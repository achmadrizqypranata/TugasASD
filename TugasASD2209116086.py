import datetime
import getpass
from prettytable import PrettyTable

class Akun:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Admin(Akun):
    def __init__(self, username, password):
        super().__init__(username, password)

class Pembeli(Akun):
    def __init__(self, username, password, e_money):
        super().__init__(username, password)
        self.e_money = e_money
        self.cart = []
        self.transaction_count = 0
        self.last_transaction_date = datetime.date.today()

class Barang:
    def __init__(self, nama, jumlah, harga, kategori):
        self.nama = nama
        self.jumlah = jumlah
        self.harga = harga
        self.kategori = kategori

def jam_kerja():
    sekarang = datetime.datetime.now()
    return sekarang.hour >= 8 and sekarang.hour < 16

def total_harga(items):
    total_harga = sum(item.harga * item.jumlah for item in items)
    return total_harga

def diskon(total_harga):
    if total_harga >= 100000:
        return total_harga * 0.9
    return total_harga

def menu_admin(items):
    while True:
        print("\n--- Menu Admin ---")
        print("1. Tambah Barang")
        print("2. Lihat Barang")
        print("3. Update Barang")
        print("4. Hapus Barang")
        print("5. Keluar")

        pilihan = input("Pilih opsi: ")

        if pilihan == '1':
            nama = input("Nama Barang: ")
            jumlah = int(input("Jumlah: "))
            harga = int(input("Harga: "))
            print("Kategori:")
            print("1. Kostum Fullset")
            print("2. Wig")
            print("3. Aksesoris")
            kategori_pilihan = input("Pilih kategori (1/2/3): ")
            kategori = ""
            if kategori_pilihan == '1':
                kategori = "Kostum Fullset"
            elif kategori_pilihan == '2':
                kategori = "Wig"
            elif kategori_pilihan == '3':
                kategori = "Aksesoris"
            else:
                print("Kategori tidak valid.")
                continue

            items.append(Barang(nama, jumlah, harga, kategori))
            print("Barang berhasil ditambahkan.")

        elif pilihan == '2':
            print("\nDaftar Barang:")
            for index, item in enumerate(items):
                print(f"{index + 1}. {item.nama} - {item.jumlah} pcs - Rp{item.harga} - {item.kategori}")
        elif pilihan == '3':
            print("\nDaftar Barang:")
            for index, item in enumerate(items):
                print(f"{index + 1}. {item.nama} - {item.jumlah} pcs - Rp{item.harga} - {item.kategori}")
            id_barang = int(input("Pilih ID Barang yang ingin diupdate: ")) - 1
            if 0 <= id_barang < len(items):
                print("\n--- Update Barang ---")
                print("1. Update Jumlah")
                print("2. Update Harga")
                print("3. Update Kategori")
                opsi_update = input("Pilih opsi: ")

                if opsi_update == '1':
                    jumlah_baru = int(input("Jumlah baru: "))
                    items[id_barang].jumlah = jumlah_baru
                    print("Jumlah barang berhasil diupdate.")
                elif opsi_update == '2':
                    harga_baru = int(input("Harga baru: "))
                    items[id_barang].harga = harga_baru
                    print("Harga barang berhasil diupdate.")
                elif opsi_update == '3':
                    kategori_baru = input("Kategori baru: ")
                    items[id_barang].kategori = kategori_baru
                    print("Kategori barang berhasil diupdate.")
                else:
                    print("Opsi tidak valid.")
            else:
                print("ID Barang tidak valid.")
        elif pilihan == '4':
            print("\nDaftar Barang:")
            for index, item in enumerate(items):
                print(f"{index + 1}. {item.nama} - {item.jumlah} pcs - Rp{item.harga} - {item.kategori}")
            id_barang = int(input("Pilih ID Barang yang ingin dihapus: ")) - 1
            if 0 <= id_barang < len(items):
                items.pop(id_barang)
                print("Barang berhasil dihapus.")
            else:
                print("ID Barang tidak valid.")
        elif pilihan == '5':
            break
        else:
            print("Opsi tidak valid, silakan coba lagi.")

def menu_pembeli(pembeli, items):
    hari_ini = datetime.date.today()
    if pembeli.last_transaction_date != hari_ini:
        pembeli.transaction_count = 0
        pembeli.last_transaction_date = hari_ini
    
    while True:
        print(f"\nSelamat datang {pembeli.username} di Miko Cosplay Shop >w<!")
        print(f"Saldo e-money Anda: Rp{pembeli.e_money}")
        print(f"Transaksi hari ini: {pembeli.transaction_count}/3")
        print("\n--- Menu Pembeli ---")
        print("1. Top Up e-Money")
        print("2. Beli Barang")
        print("3. Cek Isi Keranjang")
        print("4. Checkout")
        print("5. Logout")

        pilihan = input("Pilih opsi: ")

        if pilihan == '1':
            jumlah = int(input("Masukkan jumlah top up: "))
            pembeli.e_money += jumlah
            print(f"Top up berhasil. Saldo e-money sekarang: Rp{pembeli.e_money}")
        elif pilihan == '2':
            print("\nDaftar Barang yang Tersedia:")
            for index, item in enumerate(items):
                print(f"{index + 1}. {item.nama} - {item.jumlah} pcs - Rp{item.harga} - {item.kategori}")
            
            nomor_barang = int(input("Pilih nomor barang yang ingin dibeli: ")) - 1
            if 0 <= nomor_barang < len(items):
                jumlah = int(input("Masukkan jumlah yang ingin dibeli: "))
                if items[nomor_barang].jumlah >= jumlah:
                    barang_terpilih = Barang(items[nomor_barang].nama, jumlah, items[nomor_barang].harga, items[nomor_barang].kategori)
                    pembeli.cart.append(barang_terpilih)
                    items[nomor_barang].jumlah -= jumlah
                    print("\nBarang berhasil ditambahkan ke keranjang.")
                else:
                    print("Jumlah barang tidak mencukupi.")
            else:
                print("Nomor barang tidak valid.")
        elif pilihan == '3':
            print("\nIsi Keranjang:")
            if not pembeli.cart:
                print("Keranjang kamu kosong.")
            else:
                for item in pembeli.cart:
                    print(f"{item.nama} - {item.jumlah} pcs - Rp{item.harga} - {item.kategori}")
        elif pilihan == '4':
            if not pembeli.cart:
                print("Keranjang kosong, tidak bisa checkout.")
            else:
                if pembeli.transaction_count >= 3:
                    print("Anda telah mencapai batas transaksi harian. Silahkan coba lagi besok :3")
                    continue

                total_harga_barang = total_harga(pembeli.cart)
                print(f"Total harga: Rp{total_harga_barang}")
                
                total_harga_barang = diskon(total_harga_barang)
                print(f"Setelah diskon: Rp{total_harga_barang}")

                if total_harga_barang >= 100000:
                    print("Selamat kamu mendapatkan Diskon 10% >w<")
                    total_harga_barang = total_harga_barang * 0.9
                else:
                    print("Anda masih belum memenuhi syarat untuk mendapatkan diskon. Ayo belanja lebih banyak lagi :3")
                    print(f"Setelah diskon: Rp{total_harga_barang}")

                if pembeli.e_money >= total_harga_barang:
                    pembeli.e_money -= total_harga_barang

                    nota_pembelian = PrettyTable()
                    nota_pembelian.field_names = ["Nama Pembeli", "Nama Barang", "Jumlah", "Harga per Item", "Total Harga"]
                    for item in pembeli.cart:
                        nota_pembelian.add_row([pembeli.username, item.nama, item.jumlah, f"Rp{item.harga}", f"Rp{item.harga * item.jumlah}"])
                    nota_pembelian.add_row(["", "", "", "Total Bayar", f"Rp{total_harga_barang}"])

                    print("\n--- Nota Pembelian ---")
                    print(nota_pembelian)

                    pembeli.cart.clear()
                    pembeli.transaction_count += 1
                    print(f"Pembelian berhasil. Sisa e-money: Rp{pembeli.e_money}")
                else:
                    print("Maaf, saldo e-money tidak mencukupi.")
        elif pilihan == '5':
            break
        else:
            print("Opsi tidak valid, silakan coba lagi.")

def daftar(buyers):
    username = input("Masukkan username: ")
    password = getpass.getpass("Masukkan password: ")
    e_money = int(input("Masukkan saldo e-money awal: "))
    buyers.append(Pembeli(username, password, e_money))
    print("Registrasi berhasil, silakan login.")

def main():
    admin = Admin("rizqy", "rizqy86")
    pembeli = [
        Pembeli("sakura", "sakura18", 2000000),
        Pembeli("sarah", "sarah25", 1000000),
        Pembeli("chelly", "chelly40", 1500000)
    ]

    items = [
        Barang("Arima Kana Oshi no Ko", 5, 500000, "Kostum Fullset"),
        Barang("Boa Hancock One Piece", 5, 400000, "Kostum Fullset"),
        Barang("Takina Inoue Lycoris Recoil", 5, 450000, "Kostum Fullset"),
        Barang("Yuji Itadori Jujutsu Kaisen", 5, 300000, "Kostum Fullset"),
        Barang("Hutao Genshin Impact Wig", 5, 200000, "Wig"),
        Barang("Kaedehara Kazuha Genshin Impact Wig", 5, 150000, "Wig"),
        Barang("Marin Kitagawa My Dress-Up Darling Wig", 5, 200000, "Wig"),
        Barang("Wigcap", 20, 10000, "Aksesoris"),
        Barang("Stocking", 10, 20000, "Aksesoris"),
        Barang("Sisir Wig", 15, 15000, "Aksesoris")
    ]

    if jam_kerja():
        print("--- Menu Dashboard Miko Cosplay Shop ---")
        
        while True:
            print("\n1. Login sebagai Admin")
            print("2. Login sebagai Pembeli")
            print("3. Keluar")
            pilihan = input("Pilih opsi: ")

            if pilihan == '1':
                username = input("Username: ")
                password = getpass.getpass("Password: ")

                if username == admin.username and password == admin.password:
                    print("Login berhasil sebagai admin.")
                    menu_admin(items)
                else:
                    print("Username atau password salah.")
            elif pilihan == '2':
                print("\n1. Login")
                print("2. Registrasi")
                pilihan = input("Pilih opsi: ")

                if pilihan == '1':
                    username = input("Username: ")
                    password = getpass.getpass("Password: ")

                    pembeli_ini = next((b for b in pembeli if b.username == username and b.password == password), None)
                    if pembeli_ini:
                        print("Login berhasil sebagai pembeli.")
                        menu_pembeli(pembeli_ini, items)
                    else:
                        print("Username atau password salah.")
                elif pilihan == '2':
                    daftar(pembeli)
                else:
                    print("Opsi tidak valid.")
            elif pilihan == '3':
                print("Terima kasih telah mengunjungi shop kami ^^")
                break
            else:
                print("Opsi tidak valid, silakan coba lagi.")
    else:
        print("Maaf, toko kami hanya buka pada jam kerja (08.00 - 16.00).")

if __name__ == "__main__":
    main()
