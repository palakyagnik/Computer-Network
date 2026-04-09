'''
Program Name: XOR Cipher Demonstration

Description:
This Python program demonstrates the use of the XOR (Exclusive OR)
operation on each character of a string. XOR is a fundamental concept
used in computer networks and cryptography for simple encryption
and decryption techniques.

The program applies XOR operation with a fixed key (1) to each
character in the string and displays the transformed result.

Concepts Used:
• Bitwise XOR Operation (^)
• ASCII value manipulation using ord() and chr()
• Basic Cryptography Concept

Working:
- Each character is converted to its ASCII value
- XOR operation is applied with key (1)
- Result is converted back to character
- Same operation can be used again to decrypt

Note:
XOR with the same key twice returns the original message.

Author: Hamida Badamdi

'''

string = "abcd"
result = ""

for char in string:
    # XOR the character with 1
    xor_char = chr(ord(char) ^ 1)
    result += xor_char
print(result)