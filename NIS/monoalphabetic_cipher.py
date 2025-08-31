import string

def monoalpha_sub(plaintext, key):
    alphabet = string.ascii_lowercase
    key = key % 26
    result = []
    for ch in plaintext:
        if ch.lower() in alphabet:
            is_upper = ch.isupper()
            idx = alphabet.index(ch.lower())
            new_char = alphabet[(idx + key) % 26]
            result.append(new_char.upper() if is_upper else new_char)
        else:
            result.append(ch)
    return ''.join(result)

plaintext = input("Enter plaintext: ")
key = int(input("Enter the key (number): "))
print("Ciphertext:", monoalpha_sub(plaintext, key))
