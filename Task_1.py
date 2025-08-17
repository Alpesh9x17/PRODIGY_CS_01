# Caesar Cipher Implementation

def caesar_cipher(text, shift, mode):
    """
    Encrypts or decrypts the given text using the Caesar Cipher algorithm.

    Parameters:
        text (str): The input message.
        shift (int): The shift value.
        mode (str): 'encrypt' or 'decrypt'.

    Returns:
        str: The processed message.
    """
    result = ""

    # Adjust shift for decryption
    if mode == "decrypt":
        shift = -shift

    for char in text:
        if char.isalpha():
            # Shift only alphabetic characters
            start = ord('A') if char.isupper() else ord('a')
            # Compute shifted position
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            # Non-alphabet characters remain unchanged
            result += char

    return result


def main():
    print("=== Caesar Cipher ===")
    message = input("Enter your message: ")
    shift = int(input("Enter shift value (integer): "))
    choice = input("Do you want to encrypt or decrypt? ").strip().lower()

    if choice in ["encrypt", "decrypt"]:
        output = caesar_cipher(message, shift, choice)
        print(f"\nResult ({choice}ed message): {output}")
    else:
        print("Invalid choice! Please type 'encrypt' or 'decrypt'.")


if __name__ == "__main__":
    main()
