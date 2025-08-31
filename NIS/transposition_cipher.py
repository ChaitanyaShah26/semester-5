def transpose_cipher(plaintext, row_perm, col_perm):
    text = plaintext.replace(" ", "")
    rows = len(row_perm)
    cols = len(col_perm)

    if len(text) < rows * cols:
        text += 'x' * (rows * cols - len(text))

    matrix = [list(text[i*cols:(i+1)*cols]) for i in range(rows)]

    row_rearranged = [None] * rows
    for orig_row_idx, new_row_pos in enumerate(row_perm):
        row_rearranged[new_row_pos - 1] = matrix[orig_row_idx]

    cipher_matrix = []
    for r in row_rearranged:
        if r is None:  
            continue
        new_row = [None] * cols
        for orig_col_idx, new_col_pos in enumerate(col_perm):
            new_row[new_col_pos - 1] = r[orig_col_idx]
        cipher_matrix.append(new_row)
    ciphertext = ''.join(''.join(row) for row in cipher_matrix)
    return ciphertext

plaintext = input("Enter plaintext: ")

rows = int(input("Enter number of rows for matrix: "))
cols = int(input("Enter number of columns for matrix: "))

print("\nEnter row permutation (each row number mapped to new position):")
row_perm = []
for i in range(1, rows + 1):
    new_pos = int(input(f"Row {i} → New position: "))
    row_perm.append(new_pos)

print("\nEnter column permutation (each column number mapped to new position):")
col_perm = []
for j in range(1, cols + 1):
    new_pos = int(input(f"Column {j} → New position: "))
    col_perm.append(new_pos)

cipher = transpose_cipher(plaintext, row_perm, col_perm)
print("\nCiphertext:", cipher)