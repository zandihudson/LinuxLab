
import sys

def caesar_cipher(text, shift):
    encrypted_message = []
    for char in text:
        if char.isalpha():
            if char.islower():
                base = ord('a')
            else:
                base = ord('A')
            
            index = ord(char) - base
            new_index = (index + shift) % 26
            new_char = chr(base + new_index)
            encrypted_message.append(new_char)
    
    return ''.join(encrypted_message) 

def print_message(encoded_message):
    block_size = 5
    blocks = [encoded_message[i:i+block_size] for i in range(0, len(encoded_message), block_size)]
    
    for i in range(0, len(blocks), 10):
        for j in range(10):
            if i + j < len(blocks):
                print(''.join(blocks[i + j]), end=' ')
        print()

def main():
    if len(sys.argv) != 2:
        print("Usage: python cipher.py <shift_amount>")
        return
    
    try:
        shift_amount = int(sys.argv[1])
    except ValueError:
        print("Shift amount must be an integer")
        return

    print("Enter a message to encrypt (Submit by pressing Enter, then Ctrl+D):")
    input_lines = sys.stdin.readlines() 
    print("\n Encoded message:")
    for line in input_lines:
        input_message = line.strip().upper()
        encoded_message = caesar_cipher(input_message, shift_amount)
        print_message(encoded_message)
        
    sys.exit(0) 

if __name__ == "__main__":
    main()