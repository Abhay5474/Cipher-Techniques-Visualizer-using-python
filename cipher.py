import random
import string
import time
from tqdm import tqdm
from colorama import Fore, Back, Style, init
import pyperclip


def loading_user():
    for _ in tqdm(range(100),
                  desc="Please Wait....",
                  ascii=False, ncols=115):
        time.sleep(0.02)
    print("\n\n")
def ceaser():
    while True:
        print(Fore.CYAN+Style.BRIGHT + '''
                    1. Algorithm of Caeser Cipher ?
                    2. Encrypt Message Using Caeser Cipher.
                    3. Decrypt Message Using Caeser Cipher.
                    4. Visualization of ceaser cipher
                    5. Exit

            ''')

        ch1 = int(input("\nEnter Your Choice From Above Options: "))
        if (ch1 == 1):
            ceaser1()
        elif (ch1 == 2):
            ceaser2()
        elif (ch1 == 3):
            ceaser3()
        elif (ch1 == 4):
            ceaser4()
        elif (ch1 == 5):
            break
        else:
            print("\nEnter valid choice")
def ceaser1():
    print('''
    Algorithm for Caesar Cipher: 

1. Choose a shift value between 1 and 25.
2. Write down the alphabet in order from A to Z.
3. Create a new alphabet by shifting each letter of the original alphabet by the shift value. 
For example, if the shift value is 3, the new alphabet would be:
4. A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
   D E F G H I J K L M N O P Q R S T U V W X Y Z A B C
5. Replace each letter of the message with the corresponding letter from the new alphabet. 
For example, if the shift value is 3, the word “hello” would become “khoor”.
6. To decrypt the message, shift each letter back by the same amount. 
For example, if the shift value is 3, the encrypted message “khoor” would become “hello”.
    
    ''')

def ceaser2():
    def encrypt_caesar(text, shift):
        encrypted_text = ""
        for char in text:
            if char.isalpha():
                is_upper = char.isupper()
                char = char.lower()
                shifted = (ord(char) - ord('a') + shift) % 26
                shifted_char = chr(ord('a') + shifted)
                if is_upper:
                    shifted_char = shifted_char.upper()
                encrypted_text += shifted_char
            else:
                encrypted_text += char
        return encrypted_text

    # Input the text and the shift value
    text = input("Enter the text to encrypt: ")
    shift = int(input("Enter the Caesar cipher shift value: "))

    # Encrypt the text
    encrypted_text = encrypt_caesar(text, shift)
    print("Encrypted text:", encrypted_text)


def ceaser3():
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

def ceaser4():
    key1 = {
        'a': 'b', 'b': 'c', 'c': 'd', 'd': 'e', 'e': 'f',
        'f': 'g', 'g': 'h', 'h': 'i', 'i': 'j', 'j': 'k',
        'k': 'l', 'l': 'm', 'm': 'n', 'n': 'o', 'o': 'p',
        'p': 'q', 'q': 'r', 'r': 's', 's': 't', 't': 'u',
        'u': 'v', 'v': 'w', 'w': 'x', 'x': 'y', 'y': 'z',
        'z': 'a',  # To handle wrapping from 'z' back to 'a'
    }
    key2 = {
        'a': 'c', 'b': 'd', 'c': 'e', 'd': 'f', 'e': 'g',
        'f': 'h', 'g': 'i', 'h': 'j', 'i': 'k', 'j': 'l',
        'k': 'm', 'l': 'n', 'm': 'o', 'n': 'p', 'o': 'q',
        'p': 'r', 'q': 's', 'r': 't', 's': 'u', 't': 'v',
        'u': 'w', 'v': 'x', 'w': 'y', 'x': 'z', 'y': 'a',
        'z': 'b',  # To handle wrapping from 'z' back to 'a'
    }
    key3= {
        'a': 'd', 'b': 'e', 'c': 'f', 'd': 'g', 'e': 'h',
        'f': 'i', 'g': 'j', 'h': 'k', 'i': 'l', 'j': 'm',
        'k': 'n', 'l': 'o', 'm': 'p', 'n': 'q', 'o': 'r',
        'p': 's', 'q': 't', 'r': 'u', 's': 'v', 't': 'w',
        'u': 'x', 'v': 'y', 'w': 'z', 'x': 'a', 'y': 'b',
        'z': 'c',  # To handle wrapping from 'z' back to 'a'
    }
    key4 = {
        'a': 'e', 'b': 'f', 'c': 'g', 'd': 'h', 'e': 'i',
        'f': 'j', 'g': 'k', 'h': 'l', 'i': 'm', 'j': 'n',
        'k': 'o', 'l': 'p', 'm': 'q', 'n': 'r', 'o': 's',
        'p': 't', 'q': 'u', 'r': 'v', 's': 'w', 't': 'x',
        'u': 'y', 'v': 'z', 'w': 'a', 'x': 'b', 'y': 'c',
        'z': 'd',
    }
    key5 = {
        'a': 'f', 'b': 'g', 'c': 'h', 'd': 'i', 'e': 'j',
        'f': 'k', 'g': 'l', 'h': 'm', 'i': 'n', 'j': 'o',
        'k': 'p', 'l': 'q', 'm': 'r', 'n': 's', 'o': 't',
        'p': 'u', 'q': 'v', 'r': 'w', 's': 'x', 't': 'y',
        'u': 'z', 'v': 'a', 'w': 'b', 'x': 'c', 'y': 'd',
        'z': 'e',
    }
    key6 = {
        'a': 'g', 'b': 'h', 'c': 'i', 'd': 'j', 'e': 'k',
        'f': 'l', 'g': 'm', 'h': 'n', 'i': 'o', 'j': 'p',
        'k': 'q', 'l': 'r', 'm': 's', 'n': 't', 'o': 'u',
        'p': 'v', 'q': 'w', 'r': 'x', 's': 'y', 't': 'z',
        'u': 'a', 'v': 'b', 'w': 'c', 'x': 'd', 'y': 'e',
        'z': 'f',
    }
    key7 = {
        'a': 'h', 'b': 'i', 'c': 'j', 'd': 'k', 'e': 'l',
        'f': 'm', 'g': 'n', 'h': 'o', 'i': 'p', 'j': 'q',
        'k': 'r', 'l': 's', 'm': 't', 'n': 'u', 'o': 'v',
        'p': 'w', 'q': 'x', 'r': 'y', 's': 'z', 't': 'a',
        'u': 'b', 'v': 'c', 'w': 'd', 'x': 'e', 'y': 'f',
        'z': 'g',
    }
    key8 = {
        'a': 'i', 'b': 'j', 'c': 'k', 'd': 'l', 'e': 'm',
        'f': 'n', 'g': 'o', 'h': 'p', 'i': 'q', 'j': 'r',
        'k': 's', 'l': 't', 'm': 'u', 'n': 'v', 'o': 'w',
        'p': 'x', 'q': 'y', 'r': 'z', 's': 'a', 't': 'b',
        'u': 'c', 'v': 'd', 'w': 'e', 'x': 'f', 'y': 'g',
        'z': 'h',
    }
    key9 = {
        'a': 'j', 'b': 'k', 'c': 'l', 'd': 'm', 'e': 'n',
        'f': 'o', 'g': 'p', 'h': 'q', 'i': 'r', 'j': 's',
        'k': 't', 'l': 'u', 'm': 'v', 'n': 'w', 'o': 'x',
        'p': 'y', 'q': 'z', 'r': 'a', 's': 'b', 't': 'c',
        'u': 'd', 'v': 'e', 'w': 'f', 'x': 'g', 'y': 'h',
        'z': 'i',
    }
    key10 = {
        'a': 'k', 'b': 'l', 'c': 'm', 'd': 'n', 'e': 'o',
        'f': 'p', 'g': 'q', 'h': 'r', 'i': 's', 'j': 't',
        'k': 'u', 'l': 'v', 'm': 'w', 'n': 'x', 'o': 'y',
        'p': 'z', 'q': 'a', 'r': 'b', 's': 'c', 't': 'd',
        'u': 'e', 'v': 'f', 'w': 'g', 'x': 'h', 'y': 'i',
        'z': 'j',
    }

    text=input(Fore.BLUE+"\nEnter the message to encrypt: ")
    key=int(input("Enter Key: "))
    next=input("\nPRESS Y FOR NEXT...")
    keyis = f'''

                ---------                 ---------
               |   KEY   |   =======>    |  {key}     |
                ---------                 ---------

               '''
    print(keyis)
    next = input(Fore.RED+Style.BRIGHT+"\nPRESS Y FOR NEXT...")
    if key==1:
        letters = []  # Create an empty list to store the extracted letters
        # Define the alphabet
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        print("\nKEY IS 1\n")
        # Create a dictionary for the combinations
        combinations = {}
        for i in range(len(alphabet)):
            letter = alphabet[i]
            shifted_letter = alphabet[(i + 1) % len(alphabet)]
            combinations[letter] = shifted_letter

        # Print the combinations
        for letter, shifted_letter in combinations.items():
            print(f"{letter} ==> {shifted_letter}")

        for char in text:
            if char.isalpha():  # Check if the character is a letter
                letters.append(char)
        length = len(letters)
        shifted=[]
        print("\n\n Now we will shift letters according to key..")
        loading_user()
        for i in range(length):
            letter = letters[i]
            if letter in key1:
                shifted_letter = key1[letter]
                shifted.append(shifted_letter)
                print("\n")
                print(" ---------                  ----------")
                print(f"|    " + letter + "    |   =======>     |    " + shifted_letter + "      |")
                print(" ---------                  ----------")
            else:
                print(f"The letter '{letter}' is not in the dictionary")
        combined_word = ''.join(shifted)
        print(Fore.BLACK+"\nEncrypted Word:", combined_word)
    elif key==2:
        letters = []  # Create an empty list to store the extracted letters
        # Define the alphabet
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        print("\nKEY IS 2\n")
        # Create a dictionary for the combinations
        combinations = {}
        for i in range(len(alphabet)):
            letter = alphabet[i]
            shifted_letter = alphabet[(i + 2) % len(alphabet)]  # Circular shift to handle 'z' wrapping to 'a'
            combinations[letter] = shifted_letter

        # Print the combinations
        for letter, shifted_letter in combinations.items():
            print(f"{letter} ==> {shifted_letter}")

        for char in text:
            if char.isalpha():  # Check if the character is a letter
                letters.append(char)
        length = len(letters)
        shifted = []
        print("\n\n Now we will shift letters according to key..")
        loading_user()
        for i in range(length):
            letter = letters[i]
            if letter in key2:
                shifted_letter = key2[letter]
                shifted.append(shifted_letter)
                print("\n")
                print(" ---------                  ----------")
                print(f"|    " + letter + "    |   =======>     |    " + shifted_letter + "      |")
                print(" ---------                  ----------")
            else:
                print(f"The letter '{letter}' is not in the dictionary")
        combined_word = ''.join(shifted)
        print(Fore.BLACK + "\nEncrypted Word:", combined_word)
    elif key==3:
        letters = []  # Create an empty list to store the extracted letters
        # Define the alphabet
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        print("\nKEY IS 3\n")
        # Create a dictionary for the combinations
        combinations = {}
        for i in range(len(alphabet)):
            letter = alphabet[i]
            shifted_letter = alphabet[(i + 3) % len(alphabet)]  # Circular shift to handle 'z' wrapping to 'a'
            combinations[letter] = shifted_letter

        # Print the combinations
        for letter, shifted_letter in combinations.items():
            print(f"{letter} ==> {shifted_letter}")
        next = input("\nPRESS Y FOR continue...")
        for char in text:
            if char.isalpha():  # Check if the character is a letter
                letters.append(char)
        length = len(letters)
        shifted = []
        print("\n\n Now we will shift letters according to key..")
        loading_user()
        for i in range(length):
            letter = letters[i]

            if letter in key3:
                shifted_letter = key3[letter]
                shifted.append(shifted_letter)
                print("\n")
                print(" ---------                  ----------")
                print(f"|    " + letter + "    |   =======>     |    " + shifted_letter + "      |")
                print(" ---------                  ----------")
            else:
                print(f"The letter '{letter}' is not in the dictionary")
        combined_word = ''.join(shifted)
        print(Fore.BLACK + "\nEncrypted Word:", combined_word)
    elif key==4:
        letters = []  # Create an empty list to store the extracted letters
        # Define the alphabet
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        print("\nKEY IS 4\n")
        # Create a dictionary for the combinations
        combinations = {}
        for i in range(len(alphabet)):
            letter = alphabet[i]
            shifted_letter = alphabet[(i + 4) % len(alphabet)]  # Circular shift to handle 'z' wrapping to 'a'
            combinations[letter] = shifted_letter

        # Print the combinations
        for letter, shifted_letter in combinations.items():
            print(f"{letter} ==> {shifted_letter}")

        for char in text:
            if char.isalpha():  # Check if the character is a letter
                letters.append(char)
        length = len(letters)
        shifted = []
        print("\n\n Now we will shift letters according to key..")
        loading_user()
        for i in range(length):
            letter = letters[i]
            if letter in key4:
                shifted_letter = key4[letter]
                shifted.append(shifted_letter)
                print("\n")
                print(" ---------                  ----------")
                print(f"|    " + letter + "    |   =======>     |    " + shifted_letter + "      |")
                print(" ---------                  ----------")
            else:
                print(f"The letter '{letter}' is not in the dictionary")
        combined_word = ''.join(shifted)
        print(Fore.BLACK + "\nEncrypted Word:", combined_word)
    elif key==5:
        letters = []  # Create an empty list to store the extracted letters
        # Define the alphabet
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        print("\nKEY IS 5\n")
        # Create a dictionary for the combinations
        combinations = {}
        for i in range(len(alphabet)):
            letter = alphabet[i]
            shifted_letter = alphabet[(i + 5) % len(alphabet)]  # Circular shift to handle 'z' wrapping to 'a'
            combinations[letter] = shifted_letter

        # Print the combinations
        for letter, shifted_letter in combinations.items():
            print(f"{letter} ==> {shifted_letter}")

        for char in text:
            if char.isalpha():  # Check if the character is a letter
                letters.append(char)
        length = len(letters)
        shifted = []
        print("\n\n Now we will shift letters according to key..")
        loading_user()
        for i in range(length):
            letter = letters[i]
            if letter in key5:
                shifted_letter = key5[letter]
                shifted.append(shifted_letter)
                print("\n")
                print(" ---------                  ----------")
                print(f"|    " + letter + "    |   =======>     |    " + shifted_letter + "      |")
                print(" ---------                  ----------")
            else:
                print(f"The letter '{letter}' is not in the dictionary")
        combined_word = ''.join(shifted)
        print(Fore.BLACK + "\nEncrypted Word:", combined_word)
    elif key==6:
        letters = []  # Create an empty list to store the extracted letters
        # Define the alphabet
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        print("\nKEY IS 6\n")
        # Create a dictionary for the combinations
        combinations = {}
        for i in range(len(alphabet)):
            letter = alphabet[i]
            shifted_letter = alphabet[(i + 6) % len(alphabet)]  # Circular shift to handle 'z' wrapping to 'a'
            combinations[letter] = shifted_letter

        # Print the combinations
        for letter, shifted_letter in combinations.items():
            print(f"{letter} ==> {shifted_letter}")

        for char in text:
            if char.isalpha():  # Check if the character is a letter
                letters.append(char)
        length = len(letters)
        shifted = []
        print("\n\n Now we will shift letters according to key..")
        loading_user()
        for i in range(length):
            letter = letters[i]
            if letter in key6:
                shifted_letter = key6[letter]
                shifted.append(shifted_letter)
                print("\n")
                print(" ---------                  ----------")
                print(f"|    " + letter + "    |   =======>     |    " + shifted_letter + "      |")
                print(" ---------                  ----------")
            else:
                print(f"The letter '{letter}' is not in the dictionary")
        combined_word = ''.join(shifted)
        print(Fore.BLACK + "\nEncrypted Word:", combined_word)
    elif key==7:
        letters = []  # Create an empty list to store the extracted letters
        # Define the alphabet
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        print("\nKEY IS 7\n")
        # Create a dictionary for the combinations
        combinations = {}
        for i in range(len(alphabet)):
            letter = alphabet[i]
            shifted_letter = alphabet[(i + 7) % len(alphabet)]  # Circular shift to handle 'z' wrapping to 'a'
            combinations[letter] = shifted_letter

        # Print the combinations
        for letter, shifted_letter in combinations.items():
            print(f"{letter} ==> {shifted_letter}")

        for char in text:
            if char.isalpha():  # Check if the character is a letter
                letters.append(char)
        length = len(letters)
        shifted = []
        print("\n\n Now we will shift letters according to key..")
        loading_user()
        for i in range(length):
            letter = letters[i]
            if letter in key7:
                shifted_letter = key7[letter]
                shifted.append(shifted_letter)
                print("\n")
                print(" ---------                  ----------")
                print(f"|    " + letter + "    |   =======>     |    " + shifted_letter + "      |")
                print(" ---------                  ----------")
            else:
                print(f"The letter '{letter}' is not in the dictionary")
        combined_word = ''.join(shifted)
        print(Fore.BLACK + "\nEncrypted Word:", combined_word)
    elif key==8:
        letters = []  # Create an empty list to store the extracted letters
        # Define the alphabet
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        print("\nKEY IS 8\n")
        # Create a dictionary for the combinations
        combinations = {}
        for i in range(len(alphabet)):
            letter = alphabet[i]
            shifted_letter = alphabet[(i + 8) % len(alphabet)]  # Circular shift to handle 'z' wrapping to 'a'
            combinations[letter] = shifted_letter

        # Print the combinations
        for letter, shifted_letter in combinations.items():
            print(f"{letter} ==> {shifted_letter}")

        for char in text:
            if char.isalpha():  # Check if the character is a letter
                letters.append(char)
        length = len(letters)
        shifted = []
        print("\n\n Now we will shift letters according to key..")
        loading_user()
        for i in range(length):
            letter = letters[i]
            if letter in key8:
                shifted_letter = key8[letter]
                shifted.append(shifted_letter)
                print("\n")
                print(" ---------                  ----------")
                print(f"|    " + letter + "    |   =======>     |    " + shifted_letter + "      |")
                print(" ---------                  ----------")
            else:
                print(f"The letter '{letter}' is not in the dictionary")
        combined_word = ''.join(shifted)
        print(Fore.BLACK + "\nEncrypted Word:", combined_word)
    elif key==9:
        letters = []  # Create an empty list to store the extracted letters
        # Define the alphabet
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        print("\nKEY IS 9\n")
        # Create a dictionary for the combinations
        combinations = {}
        for i in range(len(alphabet)):
            letter = alphabet[i]
            shifted_letter = alphabet[(i + 9) % len(alphabet)]  # Circular shift to handle 'z' wrapping to 'a'
            combinations[letter] = shifted_letter

        # Print the combinations
        for letter, shifted_letter in combinations.items():
            print(f"{letter} ==> {shifted_letter}")

        for char in text:
            if char.isalpha():  # Check if the character is a letter
                letters.append(char)
        length = len(letters)
        shifted = []
        print("\n\n Now we will shift letters according to key..")
        loading_user()
        for i in range(length):
            letter = letters[i]
            if letter in key9:
                shifted_letter = key9[letter]
                shifted.append(shifted_letter)
                print("\n")
                print(" ---------                  ----------")
                print(f"|    " + letter + "    |   =======>     |    " + shifted_letter + "      |")
                print(" ---------                  ----------")
            else:
                print(f"The letter '{letter}' is not in the dictionary")
        combined_word = ''.join(shifted)
        print(Fore.BLACK + "\nEncrypted Word:", combined_word)
    elif key==10:
        letters = []  # Create an empty list to store the extracted letters
        # Define the alphabet
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        print("\nKEY IS 10\n")
        # Create a dictionary for the combinations
        combinations = {}
        for i in range(len(alphabet)):
            letter = alphabet[i]
            shifted_letter = alphabet[(i + 10) % len(alphabet)]  # Circular shift to handle 'z' wrapping to 'a'
            combinations[letter] = shifted_letter

        # Print the combinations
        for letter, shifted_letter in combinations.items():
            print(f"{letter} ==> {shifted_letter}")

        for char in text:
            if char.isalpha():  # Check if the character is a letter
                letters.append(char)
        length = len(letters)
        shifted = []
        print("\n\n Now we will shift letters according to key..")
        loading_user()
        for i in range(length):
            letter = letters[i]
            if letter in key10:
                shifted_letter = key10[letter]
                shifted.append(shifted_letter)
                print("\n")
                print(" ---------                  ----------")
                print(f"|    " + letter + "    |   =======>     |    " + shifted_letter + "      |")
                print(" ---------                  ----------")
            else:
                print(f"The letter '{letter}' is not in the dictionary")
        combined_word = ''.join(shifted)
        print(Fore.BLACK + "\nEncrypted Word:", combined_word)
    else:
        print("Invalid!!")


    next = input("\nPRESS Y FOR continue...")
#################################################

def rail():
    while True:
        print(Fore.CYAN + Style.BRIGHT + '''
                                1. Algorithm of Rail fence Cipher ?
                                2. Visualization of Rail fence cipher
                                3. Exit

                        ''')

        ch1 = int(input("\nEnter Your Choice From Above Options: "))
        if (ch1 == 1):
            ceaser1()
        elif (ch1 == 2):
            rail4()
        elif (ch1 == 3):
            break
        else:
            print("\nEnter valid choice")
def rail1():
    print('''In the rail fence cipher, the plain-text is written downwards and diagonally on successive rails of an imaginary fence.
             When we reach the bottom rail, we traverse upwards moving diagonally, after reaching the top rail, the direction is changed again. Thus the alphabets of the message are written in a zig-zag manner.
             After each alphabet has been written, the individual rows are combined to obtain the cipher-text.''')
def rail4():
    def rail_fence_cipher_visualization(text, depth):
        encrypted_text = [[' ' for _ in range(len(text))] for _ in range(depth)]

        row, col, direction = 0, 0, 1  # direction: 1 for down, -1 for up

        for char in text:
            encrypted_text[row][col] = char
            row += direction

            # Change direction if we've reached the top or bottom rail
            if row == 0 or row == depth - 1:
                direction *= -1

            col += 1

        # Print the visualization
        for i in range(depth):
            for j in range(len(text)):
                print(' ' * 3 * j, end='')  # Add spaces before each letter
                if encrypted_text[i][j] != ' ':
                    print(Fore.RED+'---', end='')
                else:
                    print('   ', end='')
                print(' ' * 3 * (len(text) - j - 1), end='')  # Add spaces after each letter
            print()

            for j in range(len(text)):
                print(' ' * 3 * j, end='')  # Add spaces before each letter
                if encrypted_text[i][j] != ' ':
                    time.sleep(2)
                    print(Fore.RED+f'|{encrypted_text[i][j]}|', end='')
                else:
                    print('   ', end='')
                print(' ' * 3 * (len(text) - j - 1), end='')  # Add spaces after each letter
            print()

            for j in range(len(text)):
                print(' ' * 3 * j, end='')  # Add spaces before each letter
                if encrypted_text[i][j] != ' ':
                    print('---', end='')
                else:
                    print('   ', end='')
                print(' ' * 3 * (len(text) - j - 1), end='')  # Add spaces after each letter
            print()


    # Input
    text = input("\nEnter the text: ")
    depth = int(input("Enter the depth (key): "))

    rail_fence_cipher_visualization(text, depth)

    def read(text,depth):
        print("\n Now read the message horizontally...")
        y = input("\nPRESS Y FOR NEXT")

        def rail_fence_cipher_encrypt(text, depth):
            # Create an empty rail fence matrix
            matrix = [[' ' for _ in range(len(text))] for _ in range(depth)]

            # Fill the matrix with the text using the Rail Fence pattern
            row, col, direction = 0, 0, 1
            for char in text:
                matrix[row][col] = char
                row += direction

                # Change direction if we've reached the top or bottom rail
                if row == 0 or row == depth - 1:
                    direction *= -1

                col += 1

            # Read the encrypted text from the matrix
            encrypted_text = []
            for i in range(depth):
                for j in range(len(text)):
                    if matrix[i][j] != ' ':
                        encrypted_text.append(matrix[i][j])
            for j in encrypted_text:
                time.sleep(2)
                print(Fore.BLACK+Style.BRIGHT+"               ______")
                print(f'              |   {j}  |')
                print("               ______")
                print("                 ||     ")
                print("                 ||     ")
                print("                 \/     \n")
            return ''.join(encrypted_text)

        # Input
        text1 = text
        depth1 = depth

        # Encrypt the text
        encrypted_text = rail_fence_cipher_encrypt(text, depth)

        print("\nEncrypted Text:", encrypted_text)
    read(text,depth)




##################################################



while True:
    print(Fore.RED + Style.BRIGHT + "\n\nChoose Cipher Technique Form Below Options: ")
    print(Fore.CYAN + '''
            1. Caeser Cipher
            2. Rail Fence Cipher
            3. Exit
      ''')
    choice = int(input(Fore.RED + Style.BRIGHT + "Enter Your Choice: "))
    if choice == 1:
        ceaser()
    elif choice == 2:
        rail()
    elif choice == 3:
        break
    else:
        print("Invalid Choice, try again..")