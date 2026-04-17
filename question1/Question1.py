import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

shift1 = int(input("Enter shift1: "))
shift2 = int(input("Enter shift2: "))

#Encryption process
def encrypt_char(char):

    if 'a' <= char <= 'z':
       
        position = ord(char) - ord('a')

        if 'a' <= char <= 'm':
            
            new_position = (position + shift1 * shift2) % 13
        else:
          
            position_in_half = position - 13
            new_position_in_half = (position_in_half - (shift1 + shift2)) % 13
            return chr(new_position_in_half + 13 + ord('a'))  
        
        return chr(new_position + ord('a'))          


    elif 'A' <= char <= 'Z':
        position = ord(char) - ord('A')

        if 'A' <= char <= 'M':
            new_position = (position - shift1) % 13
            return chr(new_position + ord('A'))            

        else:
            pos_in_half = position - 13                    
            new_pos_in_half = (pos_in_half + shift2 * shift2) % 13
            return chr(new_pos_in_half + 13 + ord('A'))     

def encrypt():
    try:
        # Setting up input path
        input_path = os.path.join(BASE_DIR, 'raw_text.txt')
        output_path = os.path.join(BASE_DIR, 'encrypted_text.txt')
        
        # Check if file exists
        if not os.path.exists(input_path):
            raise FileNotFoundError("raw_text.txt not found!")

        # Read input file
        with open(input_path, 'r') as input_file:
            original_text = input_file.read()

        # Encrypt text
        encrypted_text = ""
        for char in original_text:
            encrypted_text += encrypt_char(char)

        # Write output file
        with open(output_path, 'w') as output_file:
            output_file.write(encrypted_text)

        print("Encryption done! File saved: encrypted_text.txt")

    except FileNotFoundError as e:
        print("File Error:", e)

    except PermissionError:
        print("Permission denied: Unable to access the file.")

    except Exception as e:
        print("An unexpected error occurred:", e)


# Decryption process
def decrypt_char(char):
    # Lowercase letters
    if 'a' <= char <= 'z':
        position = ord(char) - ord('a')

        if char <= 'm':
            orig_position = (position - shift1 * shift2) % 13
            return chr(orig_position + ord('a'))

        else:
            pos_in_half = position - 13
            orig_pos_in_half = (pos_in_half + shift1 + shift2) % 13
            return chr(orig_pos_in_half + 13 + ord('a'))

    # Uppercase letters
    elif 'A' <= char <= 'Z':
        position = ord(char) - ord('A')

        if char <= 'M':
            orig_position = (position + shift1) % 13
            return chr(orig_position + ord('A'))

        else:
            pos_in_half = position - 13
            orig_pos_in_half = (pos_in_half - shift2 * shift2) % 13
            return chr(orig_pos_in_half + 13 + ord('A'))
    else:
        return char


def decrypt():
    try:
        # Check if file exists
        input_path = os.path.join(BASE_DIR, 'encrypted_text.txt')
        output_path = os.path.join(BASE_DIR, 'decrypted_text.txt')

        if not os.path.exists(input_path):
            raise FileNotFoundError("encrypted_text.txt not found!")

        # Read encrypted file
        with open(input_path, 'r') as input_file:
            encrypted_text = input_file.read()

        # Decrypt text
        decrypted_text = ""
        for char in encrypted_text:
            decrypted_text += decrypt_char(char)

        # Write decrypted file
        with open(output_path, 'w') as output_file:
            output_file.write(decrypted_text)

        print("Decryption done! File saved: decrypted_text.txt")

    except FileNotFoundError as e:
        print("File Error:", e)

    except PermissionError:
        print("Permission denied: Unable to access the file.")

    except Exception as e:
        print("An unexpected error occurred:", e)
       
#verification
def verify():
    try:
        input_path = os.path.join(BASE_DIR, 'raw_text.txt')
        decrypted_path = os.path.join(BASE_DIR, 'decrypted_text.txt')

        # Check both files exist
        if not os.path.exists(input_path):
            raise FileNotFoundError("raw_text.txt not found!")

        if not os.path.exists(decrypted_path):
            raise FileNotFoundError("decrypted_text.txt not found!")

        # Read both files
        with open(input_path, 'r') as file1:
            original_text = file1.read()

        with open(decrypted_path, 'r') as file2:
            decrypted_text = file2.read()

        # Compare
        if original_text == decrypted_text:
            print("Verification successful: Files match!")
        else:
            print("Verification failed: Files do NOT match!")

    except FileNotFoundError as e:
        print("File Error:", e)

    except Exception as e:
        print("Unexpected error:", e)

# Calling all the functions
print("")
encrypt()
decrypt()
verify()
