
"""
Program Name: Rail Fence Cipher Encryption

Description:
This Python program implements the Rail Fence Cipher algorithm,
a classical transposition cipher used in cryptography.

The Rail Fence Cipher rearranges the characters of the plaintext
in a zig-zag (rail) pattern across multiple rows (rails) and then
reads them row by row to generate the ciphertext.

Concepts Used:
• Cryptography (Transposition Cipher)
• String manipulation
• Lists and loops

Working:
- The plaintext is written in a zig-zag pattern across given rails
- Direction changes when top or bottom rail is reached
- Characters are then read row-wise to form ciphertext

Example (3 rails):
Plaintext: HELLO WORLD

H   L   O   L
 E L W R D
  L   O

Ciphertext: HLOLELWRDLO

Note:
- Spaces are treated as characters
- Number of rails must be ≥ 2

Author: Hamida Badamdi
"""

# Function to implement Rail Fence Cipher Encryption
def rail_fence_cipher(plaintext, rails):
    # Create empty rails (list of lists)
    fence = [[] for i in range(rails)]
    
    rail = 0              # Current rail index
    direction = 1         # Direction: 1 = down, -1 = up
    
    # Place characters in zig-zag pattern
    for letter in plaintext:
        fence[rail].append(letter)
        rail += direction
        
        # Change direction at top and bottom rails
        if rail == rails - 1 or rail == 0:
            direction = -direction
    
    # Read characters row by row to form ciphertext
    ciphertext = ""
    for rail in fence:
        for letter in rail:
            ciphertext += letter
    
    return ciphertext


# Example usage
plaintext = "HELLO WORLD"
rails = 3

ciphertext = rail_fence_cipher(plaintext, rails)

print("Plaintext:", plaintext)
print("Rails:", rails)
print("Ciphertext:", ciphertext)