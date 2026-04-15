shift1 = int(input("Enter shift1: "))
shift2 = int(input("Enter shift2: "))

def encrypt_char(char):
    # For lowercase letters
    if 'a' <= char <= 'z':
        # This will find where this letter sits in the alphabet (such as 0 = a, 25 = z)
        position = ord(char) - ord('a')

        if 'a' <= char <= 'm':
            # The first half (a to m) is shifted forward : shift FORWARD by shift1 * shift2
            new_position = (position + shift1 * shift2) % 26
        else:
            # The second half (n to z) is shifted backwards : shift BACKWARD by shift1 + shift2
            new_position = (position - (shift1 + shift2)) % 26

        return chr(new_position + ord('a'))

    # For uppercase letters
    elif 'A' <= char <= 'Z':
        position = ord(char) - ord('A')

        if 'A' <= char <= 'M':
            # The first half (A to M) is shifted backwards: shift BACKWARD by shift1
            new_position = (position - shift1) % 26
        else:
            # The second half (N to Z) is shifted forward: shift FORWARD by shift2 squared
            new_position = (position + shift2 * shift2) % 26

        return chr(new_position + ord('A'))

    # For everything else: nothing will change
    else:
        return char