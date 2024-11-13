import tkinter as tk
from tkinter import messagebox

# Fungsi Enkripsi
def enkripsi(plain_text, shift):
    cipher_text = ""
    for char in plain_text:
        # Huruf Besar
        if char.isupper():
            cipher_text += chr((ord(char) + shift - 65) % 26 + 65)
        
        # Huruf Kecil
        elif char.islower():
            cipher_text += chr((ord(char) + shift - 97) % 26 + 97)
        
        # Karakter selain huruf tetap
        else:
            cipher_text += char
    return cipher_text

# Fungsi Deskripsi
def deskripsi(cipher_text, shift):
    plain_text = ""
    for char in cipher_text:
        # Huruf Besar
        if char.isupper():
            plain_text += chr((ord(char) - shift - 65) % 26 + 65)
        
        # Huruf Kecil
        elif char.islower():
            plain_text += chr((ord(char) - shift - 97) % 26 + 97)
        
        # Karakter selain huruf tetap
        else:
            plain_text += char
    return plain_text

# Fungsi untuk Enkripsi dan Menampilkan Hasil
def encrypt_text():
    plain_text = input_text.get("1.0", tk.END).strip()
    try:
        shift = int(shift_entry.get())
        if not (1 <= shift <= 25):
            messagebox.showerror("Error", "Nilai pergeseran harus antara 1 dan 25.")
            return
        cipher_text = enkripsi(plain_text, shift)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, cipher_text)
    except ValueError:
        messagebox.showerror("Error", "Masukkan nilai pergeseran yang valid.")

# Fungsi untuk Deskripsi dan Menampilkan Hasil
def decrypt_text():
    cipher_text = output_text.get("1.0", tk.END).strip()
    try:
        shift = int(shift_entry.get())
        if not (1 <= shift <= 25):
            messagebox.showerror("Error", "Nilai pergeseran harus antara 1 dan 25.")
            return
        plain_text = deskripsi(cipher_text, shift)
        input_text.delete("1.0", tk.END)
        input_text.insert(tk.END, plain_text)
    except ValueError:
        messagebox.showerror("Error", "Masukkan nilai pergeseran yang valid.")

# GUI menggunakan tkinter
root = tk.Tk()
root.title("Caesar Cipher")

# Label dan Input untuk teks asli (Plain Text)
tk.Label(root, text="Masukkan Teks (Plain Text):").grid(row=0, column=0, padx=10, pady=5)
input_text = tk.Text(root, height=5, width=40)
input_text.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

# Label dan Entry untuk pergeseran
tk.Label(root, text="Masukkan Nilai Pergeseran (1-25):").grid(row=2, column=0, padx=10, pady=5)
shift_entry = tk.Entry(root)
shift_entry.grid(row=2, column=1, padx=10, pady=5)

# Tombol Enkripsi dan Deskripsi
encrypt_button = tk.Button(root, text="Enkripsi", command=encrypt_text)
encrypt_button.grid(row=3, column=0, padx=10, pady=10)

decrypt_button = tk.Button(root, text="Deskripsi", command=decrypt_text)
decrypt_button.grid(row=3, column=1, padx=10, pady=10)

# Label dan Output untuk teks terenkripsi (Cipher Text)
tk.Label(root, text="Teks Terenkripsi/Terdekripsi:").grid(row=4, column=0, padx=10, pady=5)
output_text = tk.Text(root, height=5, width=40)
output_text.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

root.mainloop()
