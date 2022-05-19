# impor semua metode dan kelas dari tkinter
from tkinter import *
# impor semua metode dan kelas dari tkcalendar
from tkcalendar import *

# Buat jendela GUI
root = Tk()
# Atur judul GUI
root.title('Calender-Mens')
# Atur konfigurasi jendela GUI
root.geometry("600x400")

# Buat dan atur label kalender untuk menampilkan tanggal yang dipilih
cal = Calendar(root, selectmode="day", year=2022, month=5, day=18)
cal.pack()

# Fungsi untuk menampilkan tanggal tertentu
def grab_date():
    my_label.config(text="Siklus Mens Pertama" + cal.get_date())

# Buat tombol Mulai Mens untuk menampilkan tanggal yang dipilih
my_button = Button(root, text="Mulai Mens", command=grab_date)
my_button.pack(pady=20)

# Buat Label untuk menunjukkan text
my_label = Label(root, text="Masukkan tanggal menstruasi Anda")
my_label.pack(pady=20)

# Start The GUI
root.mainloop()