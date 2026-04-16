import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

shift1 = int(input("Enter shift1: "))
shift2 = int(input("Enter shift2: "))


def encrypt_char(char):
   
    if 'a' <= char <= 'z':
       
        position = ord(char) - ord('a')

        if 'a' <= char <= 'm':
            
            new_position = (position + shift1 * shift2) % 26
        else:
          
            new_position = (position - (shift1 + shift2)) % 26

        return chr(new_position + ord('a'))


    elif 'A' <= char <= 'Z':
        position = ord(char) - ord('A')

        if 'A' <= char <= 'M':
            
            new_position = (position - shift1) % 26
        else:
           
            new_position = (position + shift2 * shift2) % 26

        return chr(new_position + ord('A'))

  
    else:
        return char


def encrypt():
    try:
        # Setup input path
        input_path = os.path.join(BASE_DIR, 'raw_text.txt')
        output_path = os.path.join(BASE_DIR, 'encrypted_text.txt')

        print("Looking for file at:", input_path)
        
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


# Call all the functions
print("")
encrypt()
