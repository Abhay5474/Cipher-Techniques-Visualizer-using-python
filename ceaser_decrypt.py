def decrypt_caesar(encrypted_text, shift):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            shifted = (ord(char) - ord('a') - shift) % 26
            shifted_char = chr(ord('a') + shifted)
            if is_upper:
                shifted_char = shifted_char.upper()
            decrypted_text += shifted_char
        else:
            decrypted_text += char
    return decrypted_text

# Input the encrypted text and the shift value
encrypted_text = input("Enter the encrypted text to decrypt: ")
shift = int(input("Enter the Caesar cipher shift value: "))

# Decrypt the text
decrypted_text = decrypt_caesar(encrypted_text, shift)
print("Decrypted text:", decrypted_text)
