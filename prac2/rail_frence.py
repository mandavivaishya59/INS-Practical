def encrypt(text, rails):
    rows = [''] * rails
    row, step = 0, 1
    for char in text:
        rows[row] += char
        row += step
        if row == 0 or row == rails - 1:
            step *= -1
    return ''.join(rows)

def decrypt(cipher, rails):
    pattern, row, step = [], 0, 1
    for _ in cipher:
        pattern.append(row)
        row += step
        if row == 0 or row == rails - 1:
            step *= -1

    rails_list, idx = [], 0
    for i in range(rails):
        rails_list.append(list(cipher[idx:idx + pattern.count(i)]))
        idx += pattern.count(i)

    return ''.join(rails_list[row].pop(0) for row in pattern)

# --- Main Program ---
text = input("Enter text to encrypt: ")
key = int(input("Number of rails: "))

enc = encrypt(text, key)
print("Encrypted text:", enc)

dec = decrypt(enc, key)
print("Decrypted text:", dec)
