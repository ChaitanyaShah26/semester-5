import string

def vigenere_cipher(plaintext, key):
    alphabet = string.ascii_lowercase
    cipher_text = ""
    key_len = len(key)
    
    j = 0 
    for ch in plaintext:
        if ch.lower() in alphabet:  
            shift = key[j % key_len] % 26
            idx = alphabet.index(ch.lower())
            new_char = alphabet[(idx + shift) % 26]
            cipher_text += new_char.upper() if ch.isupper() else new_char
            j += 1
        else:
            cipher_text += ch
    return cipher_text

plaintext = input("Enter plaintext: ")
key_input = input("Enter the key as space-separated numbers: ")
key = list(map(int, key_input.strip().split()))

print("Ciphertext:", vigenere_cipher(plaintext, key))