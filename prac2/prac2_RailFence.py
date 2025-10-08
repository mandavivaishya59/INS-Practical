def rail_fence_encrypt(text, key):
    # Create the matrix
    rail = [['\n' for _ in range(len(text))] for _ in range(key)]

    dir_down = False
    row, col = 0, 0

    # Fill the matrix with characters in zigzag form
    for i in range(len(text)):
        # Change direction if we hit the top or bottom
        if row == 0 or row == key - 1:
            dir_down = not dir_down

        rail[row][col] = text[i]
        col += 1

        if dir_down:
            row += 1
        else:
            row -= 1

    # Collect the encrypted text
    result = []
    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] != '\n':
                result.append(rail[i][j])
    return "".join(result)


def rail_fence_decrypt(cipher, key):
    # Create the matrix
    rail = [['\n' for _ in range(len(cipher))] for _ in range(key)]

    dir_down = None
    row, col = 0, 0

    # Mark the positions where characters will go
    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False

        rail[row][col] = '*'
        col += 1

        if dir_down:
            row += 1
        else:
            row -= 1

    # Now fill the marked positions with cipher text
    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if rail[i][j] == '*' and index < len(cipher):
                rail[i][j] = cipher[index]
                index += 1

    # Read the matrix in zigzag order to get the decrypted text
    result = []
    row, col = 0, 0
    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False

        if rail[row][col] != '\n':
            result.append(rail[row][col])
            col += 1

        if dir_down:
            row += 1
        else:
            row -= 1

    return "".join(result)


def main():
    while True:
        print("\n1. Encryption")
        print("2. Decryption")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            text = input("Enter text to encrypt: ")
            key = int(input("Enter the key (number of rails): "))
            encrypted_text = rail_fence_encrypt(text, key)
            print("Encrypted text:", encrypted_text)

        elif choice == "2":
            cipher = input("Enter text to decrypt: ")
            key = int(input("Enter the key (number of rails): "))
            decrypted_text = rail_fence_decrypt(cipher, key)
            print("Decrypted text:", decrypted_text)

        elif choice == "3":
            print("Exiting program...")
            break

        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
