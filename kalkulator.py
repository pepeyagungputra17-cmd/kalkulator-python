# Kalkulator Sederhana

def tambah(a, b):
    """Fungsi untuk menambah dua angka"""
    return a + b

def kurang(a, b):
    """Fungsi untuk mengurangi dua angka"""
    return a - b

def kali(a, b):
    """Fungsi untuk mengalikan dua angka"""
    return a * b

def bagi(a, b):
    """Fungsi untuk membagi dua angka"""
    if b == 0:
        return "Error: Tidak boleh membagi dengan nol!"
    return a / b

def kalkulator():
    """Fungsi utama kalkulator interaktif"""
    print("=" * 40)
    print("       KALKULATOR SEDERHANA")
    print("=" * 40)
    
    while True:
        print("\nPilihan operasi:")
        print("1. Tambah (+)")
        print("2. Kurang (-)")
        print("3. Kali (*)")
        print("4. Bagi (/)")
        print("5. Keluar")
        
        pilihan = input("\nMasukkan pilihan (1/2/3/4/5): ")
        
        if pilihan == '5':
            print("Terima kasih telah menggunakan kalkulator. Sampai jumpa!")
            break
        
        if pilihan in ['1', '2', '3', '4']:
            try:
                angka1 = float(input("Masukkan angka pertama: "))
                angka2 = float(input("Masukkan angka kedua: "))
                
                if pilihan == '1':
                    hasil = tambah(angka1, angka2)
                    print(f"\n{angka1} + {angka2} = {hasil}")
                elif pilihan == '2':
                    hasil = kurang(angka1, angka2)
                    print(f"\n{angka1} - {angka2} = {hasil}")
                elif pilihan == '3':
                    hasil = kali(angka1, angka2)
                    print(f"\n{angka1} * {angka2} = {hasil}")
                elif pilihan == '4':
                    hasil = bagi(angka1, angka2)
                    print(f"\n{angka1} / {angka2} = {hasil}")
            
            except ValueError:
                print("Error: Masukkan angka yang valid!")
        else:
            print("Pilihan tidak valid! Silakan pilih 1, 2, 3, 4, atau 5.")

# Jalankan program
if __name__ == "__main__":
    kalkulator()
