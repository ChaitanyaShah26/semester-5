import numpy as np

def hill_cipher(plaintext, key_matrix):
    block_size = len(key_matrix)
    plaintext = plaintext.upper().replace(" ", "")
    while len(plaintext) % block_size != 0:
        plaintext += 'X'
    plaintext_matrix = []
    for i in range(0, len(plaintext), block_size):
        block = [ord(c) - ord('A') for c in plaintext[i:i+block_size]]
        plaintext_matrix.append(block)
    ciphertext = ''
    for block in plaintext_matrix:
        p = np.array(block)
        c = np.dot(p, key_matrix) % 26
        for num in c:
            ciphertext += chr(num + ord('A'))
    return ciphertext

plaintext = input("Enter plaintext: ")
n = int(input("Enter matrix size (n for nxn key matrix): "))
key_values = list(map(int, input(f"Enter {n*n} numbers for the key matrix (row-wise): ").split()))
key_matrix = np.array(key_values).reshape(n, n)
cipher = hill_cipher(plaintext, key_matrix)
print("Ciphertext:", cipher)