import tkinter as tk
from tkinter import ttk

# Ana pencere oluşturma
root = tk.Tk()
root.title("İlahi İşlemler Arayüzü")
root.geometry("700x600")  # Pencere boyutu genişletildi

# Stil oluşturma
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12), padding=10)
style.configure("TLabel", font=("Helvetica", 12))

# İnsan nüfusu ve sıcaklık başlangıç değerleri
insan_nufusu = 8_000_000_000
cehennem_sicaklik = 5000
cennet_sicaklik = 30

# İşlem geçmişi listesi
islem_gecmisi = []

# Fonksiyonlar
def insan_yarat():
    global insan_nufusu
    insan_nufusu += 10_000
    islem_gecmisi.append(f"Yeni insan yaratıldı. Yeni nüfus: {insan_nufusu}")
    islem_gecmisi_listbox.insert(tk.END, f"Yeni insan yaratıldı. Yeni nüfus: {insan_nufusu}")

def cehennemi_harla():
    global cehennem_sicaklik
    cehennem_sicaklik += 50
    islem_gecmisi.append(f"Cehennem harlandı. Yeni sıcaklık: {cehennem_sicaklik} °C")
    cehennem_sicaklik_progressbar['value'] = cehennem_sicaklik

def cenneti_serinlet():
    global cennet_sicaklik
    cennet_sicaklik -= 1
    islem_gecmisi.append(f"Cennet serinletildi. Yeni sıcaklık: {cennet_sicaklik} °C")
    cennet_sicaklik_progressbar['value'] = cennet_sicaklik

def sel_gonder():
    ulke_isimleri.insert(tk.END, "Sel Gönderildi")
    islem_gecmisi.append("Sel gönderildi.")
    islem_gecmisi_listbox.insert(tk.END, "Sel gönderildi.")

def deprem_gonder():
    ulke_isimleri.insert(tk.END, "Deprem Gönderildi")
    islem_gecmisi.append("Deprem gönderildi.")
    islem_gecmisi_listbox.insert(tk.END, "Deprem gönderildi.")

def yangin_gonder():
    ulke_isimleri.insert(tk.END, "Yangın Gönderildi")
    islem_gecmisi.append("Yangın gönderildi.")
    islem_gecmisi_listbox.insert(tk.END, "Yangın gönderildi.")

def bereket_gonder():
    ulke_isimleri.insert(tk.END, "Bereket Gönderildi")
    islem_gecmisi.append("Bereket gönderildi.")
    islem_gecmisi_listbox.insert(tk.END, "Bereket gönderildi.")

# Ana çerçeve oluşturma
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Butonlar ve göstergeler
ttk.Button(frame, text="İnsan Yarat", command=insan_yarat).grid(row=0, column=0, padx=10, pady=10)
ttk.Button(frame, text="Cehennemi Harla", command=cehennemi_harla).grid(row=0, column=1, padx=10, pady=10)
ttk.Button(frame, text="Cenneti Serinlet", command=cenneti_serinlet).grid(row=0, column=2, padx=10, pady=10)

islem_gecmisi_label = ttk.Label(frame, text="İşlem Geçmişi")
islem_gecmisi_label.grid(row=1, column=0, columnspan=3, pady=10)

islem_gecmisi_listbox = tk.Listbox(frame, height=10, width=60)
islem_gecmisi_listbox.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

ttk.Button(frame, text="Sel Gönder", command=sel_gonder).grid(row=3, column=0, padx=10, pady=10)
ttk.Button(frame, text="Deprem Gönder", command=deprem_gonder).grid(row=3, column=1, padx=10, pady=10)
ttk.Button(frame, text="Yangın Gönder", command=yangin_gonder).grid(row=3, column=2, padx=10, pady=10)
ttk.Button(frame, text="Bereket Gönder", command=bereket_gonder).grid(row=4, column=0, columnspan=3, pady=10)

ulke_isimleri_label = ttk.Label(frame, text="Ülke İsimleri")
ulke_isimleri_label.grid(row=5, column=0, columnspan=3, pady=10)

ulke_isimleri = tk.Listbox(frame, height=10, width=60)
ulke_isimleri.grid(row=6, column=0, columnspan=3, padx=10, pady=10)

# Cehennem sıcaklık göstergesi
cehennem_sicaklik_label = ttk.Label(frame, text="Cehennem Sıcaklığı")
cehennem_sicaklik_label.grid(row=7, column=0, padx=10, pady=10)
cehennem_sicaklik_progressbar = ttk.Progressbar(frame, orient=tk.HORIZONTAL, length=200, mode='determinate')
cehennem_sicaklik_progressbar['value'] = cehennem_sicaklik
cehennem_sicaklik_progressbar.grid(row=7, column=1, columnspan=2, padx=10, pady=10)

# Cennet sıcaklık göstergesi
cennet_sicaklik_label = ttk.Label(frame, text="Cennet Sıcaklığı")
cennet_sicaklik_label.grid(row=8, column=0, padx=10, pady=10)
cennet_sicaklik_progressbar = ttk.Progressbar(frame, orient=tk.HORIZONTAL, length=200, mode='determinate')
cennet_sicaklik_progressbar['value'] = cennet_sicaklik
cennet_sicaklik_progressbar.grid(row=8, column=1, columnspan=2, padx=10, pady=10)

# Arayüz döngüsü
root.mainloop()

# Konsola işlem geçmişini yazdırma
print("\n--- İşlem Geçmişi ---")
for islem in islem_gecmisi:
    print(islem)
