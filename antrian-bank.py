from gtts import gTTS
import os
import heapq

class AntrianBank:
    def __init__(self):
        self.antrian_bisnis = []
        self.antrian_personal = []
        self.loket1 = []
        self.loket2 = []
        self.antrian_counter_bisnis = 1
        self.antrian_counter_personal = 1

    def tambah_antrian_bisnis(self):
        nomor_antrian = "B{:02d}".format(self.antrian_counter_bisnis)
        self.antrian_bisnis.append(nomor_antrian)
        self.antrian_counter_bisnis += 1
        self.suara(f"Antrian bisnis {nomor_antrian} ditambahkan.")

    def tambah_antrian_personal(self):
        nomor_antrian = "P{:02d}".format(self.antrian_counter_personal)
        self.antrian_personal.append(nomor_antrian)
        self.antrian_counter_personal += 1
        self.suara(f"Antrian personal {nomor_antrian} ditambahkan.")

    def panggil_meja1(self):
        if self.antrian_bisnis:
            nomor_antrian = self.antrian_bisnis.pop(0)
            self.loket1.append(nomor_antrian)
            self.suara(f"Nomor antrian {nomor_antrian} ke loket 1")
        elif self.antrian_personal:
            nomor_antrian = self.antrian_personal.pop(0)
            self.loket1.append(nomor_antrian)
            self.suara(f"Nomor antrian {nomor_antrian} ke loket 1")
        else:
            self.suara("Tidak ada antrian yang dipanggil di Meja 1.")

    def panggil_meja2(self):
        if self.antrian_bisnis:
            nomor_antrian = self.antrian_bisnis.pop(0)
            self.loket2.append(nomor_antrian)
            self.suara(f"Nomor antrian {nomor_antrian} ke loket 2")
        elif self.antrian_personal:
            nomor_antrian = self.antrian_personal.pop(0)
            self.loket2.append(nomor_antrian)
            self.suara(f"Nomor antrian {nomor_antrian} ke loket 2")
        else:
            self.suara("Tidak ada antrian yang dipanggil di Meja 2.")

    def tampilkan_antrian_di_meja(self):
        print("Antrian di Meja 1:", ", ".join(self.loket1))
        print("Antrian di Meja 2:", ", ".join(self.loket2))

    def suara(self, text):
        tts = gTTS(text, lang="id")
        tts.save("output.mp3")
        os.system("start output.mp3")

    def run(self):
        while True:
            print("\nMenu:")
            print("1. Tambah Antrian Bisnis")
            print("2. Tambah Antrian Personal")
            print("3. Meja 1 memanggil")
            print("4. Meja 2 memanggil")
            print("5. Keluar")

            pilihan = input("Pilih menu: ")

            if pilihan == '1':
                self.tambah_antrian_bisnis()
            elif pilihan == '2':
                self.tambah_antrian_personal()
            elif pilihan == '3':
                self.panggil_meja1()
            elif pilihan == '4':
                self.panggil_meja2()
            elif pilihan == '5':
                break
            else:
                print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")

            self.tampilkan_antrian_di_meja()

if __name__ == "__main__":
    antrian_bank = AntrianBank()
    antrian_bank.run()
