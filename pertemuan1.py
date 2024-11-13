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

# Interface Pengguna
def main():
    print("Selamat datang!")
    plain_text = input("Masukkan teks asli (plain text): ")
    shift = int(input("Masukkan nilai pergeseran (1-25): "))

    # Panggil fungsi enkripsi
    cipher_text = enkripsi(plain_text, shift)
    print("Teks terenkripsi:", cipher_text)

    # Panggil fungsi deskripsi
    deskripsi_text = deskripsi(cipher_text, shift)
    print("Teks terdekripsi:", deskripsi_text)

if __name__ == "__main__":
    main()
