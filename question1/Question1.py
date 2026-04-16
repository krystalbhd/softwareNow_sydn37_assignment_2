
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

encrypt()
