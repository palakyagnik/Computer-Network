'''
Program Name: Caesar Cipher Encryption

Description:
This Python program demonstrates the implementation of the
Caesar Cipher technique, a basic encryption method used in
computer networks and cryptography.

The program shifts each character of the message by a fixed
number (shift value) to produce an encrypted message.

Concepts Used:
• Cryptography Basics
• Caesar Cipher Algorithm
• ASCII value manipulation (ord, chr)
• String handling

Working:
- Uppercase and lowercase letters are shifted separately
- Non-alphabetic characters remain unchanged
- Uses modulo operation to wrap around alphabets

Author: Hamida Badamdi

'''

def caesar_cipher(message, shift):
    encrypted_message = ""

    for char in message:
        if char.isupper():
            encrypted_char = chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            encrypted_char = chr((ord(char) + shift - 97) % 26 + 97)
        else:
            encrypted_char = char
        encrypted_message += encrypted_char

    return encrypted_message

message = "Hello, world!"
shift = 3
encrypted_message = caesar_cipher(message, shift)

print("Original message:", message)
print("Shift:", shift)
print("Encrypted message:", encrypted_message)