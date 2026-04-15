# HIT137 Assignment 2 - Question 1
# Simple Encryption and Decryption Program

# -------------------------------------------------------
# STEP 1: Get shift values from the user
# -------------------------------------------------------

shift1 = int(input("Enter shift1: "))
shift2 = int(input("Enter shift2: "))

# -------------------------------------------------------
# STEP 2: Encryption function
# -------------------------------------------------------
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
  
    input_file = open('raw_text.txt', 'r')
    original_text = input_file.read()
    input_file.close()


    encrypted_text = ""
    for char in original_text:
        encrypted_text = encrypted_text + encrypt_char(char)

  
    output_file = open('encrypted_text.txt', 'w')
    output_file.write(encrypted_text)
    output_file.close()

    print("Encryption done! File saved: encrypted_text.txt")



# -------------------------------------------------------
# STEP 3: Decryption function
# (Just reverse everything we did in encryption)
# -------------------------------------------------------

def decrypt_char(char):
    # --- Lowercase letters ---
    if 'a' <= char <= 'z':
        position = ord(char) - ord('a')

        # Try reversing the first-half shift (subtract what we added)
        guess = (position - shift1 * shift2) % 26
        if 'a' <= chr(guess + ord('a')) <= 'm':
            return chr(guess + ord('a'))

        # Otherwise reverse the second-half shift (add what we subtracted)
        guess = (position + shift1 + shift2) % 26
        return chr(guess + ord('a'))

    # --- Uppercase letters ---
    elif 'A' <= char <= 'Z':
        position = ord(char) - ord('A')

        # Try reversing the first-half shift (add what we subtracted)
        guess = (position + shift1) % 26
        if 'A' <= chr(guess + ord('A')) <= 'M':
            return chr(guess + ord('A'))

        # Otherwise reverse the second-half shift (subtract what we added)
        guess = (position - shift2 * shift2) % 26
        return chr(guess + ord('A'))

    else:
        return char


def decrypt():
    # Open and read the encrypted file
    input_file = open('encrypted_text.txt', 'r')
    encrypted_text = input_file.read()
    input_file.close()

    # Decrypt each character one by one
    decrypted_text = ""
    for char in encrypted_text:
        decrypted_text = decrypted_text + decrypt_char(char)

    # Write the result to a new file
    output_file = open('decrypted_text.txt', 'w')
    output_file.write(decrypted_text)
    output_file.close()

    print("Decryption done! File saved: decrypted_text.txt")


# -------------------------------------------------------
# STEP 4: Verification function
# (Verify with the original text)
# -------------------------------------------------------
def verify():
  
    file1 = open('raw_text.txt', 'r')
    original = file1.read()
    file1.close()


    file2 = open('decrypted_text.txt', 'r')
    decrypted = file2.read()
    file2.close()


    if original == decrypted:
        print("Verification PASSED - the decrypted text matches the original!")
    else:
        print("Verification FAILED - the texts do not match.")



# Call function
print("")
encrypt()
decrypt()
verify()
