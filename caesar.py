def caesar (message, offset):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''
   
    for char in message.lower():
        if char == '':
          encrypted_text += char
        elif char in alphabet:
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
            encrypted_text += alphabet[new_index]
        else:
          encrypted_text += char
    return encrypted_text

text = input('Enter the message to encrypt: ')
try:
    shift = int(input('Enter the shift value (e.g., 3 ): '))
    encrypted = caesar(text, shift)
    print('\nEncrypted message: ', encrypted)
except ValueError:
    print('Invalid input. The shift must be an integer.')

