import tkinter as tk
from tkinter import messagebox

# Fungsi untuk enkripsi Caesar Cipher
def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char
    return encrypted_text

# Fungsi untuk dekripsi Caesar Cipher
def decrypt(text, shift):
    return encrypt(text, -shift)

# Fungsi untuk tombol enkripsi
def handle_encrypt():
    text = entry_text.get()
    shift = int(entry_shift.get())
    encrypted_text = encrypt(text, shift)
    result_var.set("Hasil Enkripsi: " + encrypted_text)

# Fungsi untuk tombol dekripsi
def handle_decrypt():
    text = entry_text.get()
    shift = int(entry_shift.get())
    decrypted_text = decrypt(text, shift)
    result_var.set("Hasil Dekripsi: " + decrypted_text)

# Pengaturan antarmuka
window = tk.Tk()
window.title("Caesar Cipher Encryption & Decryption")
window.geometry("450x300")
window.configure(bg="#2b2d42")

# Label judul aplikasi
title_label = tk.Label(window, text="Caesar Cipher Kriptografi", font=("Helvetica", 18, "bold"), fg="#edf2f4", bg="#2b2d42")
title_label.pack(pady=10)

# Label dan input teks
tk.Label(window, text="Masukkan teks:", font=("Helvetica", 10), fg="#edf2f4", bg="#2b2d42").pack(pady=5)
entry_text = tk.Entry(window, width=40, font=("Helvetica", 10))
entry_text.pack(pady=5)

# Label dan input shift
tk.Label(window, text="Masukkan Shift :", font=("Helvetica", 10), fg="#edf2f4", bg="#2b2d42").pack(pady=5)
entry_shift = tk.Entry(window, width=10, font=("Helvetica", 10))
entry_shift.pack(pady=5)

# Frame untuk tombol Enkripsi dan Dekripsi
frame_buttons = tk.Frame(window, bg="#2b2d42")
frame_buttons.pack(pady=15)

button_encrypt = tk.Button(frame_buttons, text="Enkripsi", font=("Helvetica", 10, "bold"), width=12, bg="#8d99ae", fg="#edf2f4", command=handle_encrypt)
button_encrypt.pack(side=tk.LEFT, padx=10)

button_decrypt = tk.Button(frame_buttons, text="Dekripsi", font=("Helvetica", 10, "bold"), width=12, bg="#8d99ae", fg="#edf2f4", command=handle_decrypt)
button_decrypt.pack(side=tk.RIGHT, padx=10)

# Label hasil
tk.Label(window, text="Hasil:", font=("Helvetica", 10), fg="#edf2f4", bg="#2b2d42").pack(pady=5)
result_var = tk.StringVar()
label_result = tk.Label(window, textvariable=result_var, fg="#ef233c", bg="#2b2d42", font=("Helvetica", 12, "bold"))
label_result.pack(pady=5)

# Menjalankan antarmuka
window.mainloop()
