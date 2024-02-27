text = 'Hello Zaira'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
encrypted_text = ''

def cipher_key(text, shift):
    for char in text.lower():
     if char == ' ':
        encrypted_text += char
     else:
        index = alphabet.find(char)
        new_index = index + shift
        encrypted_text += alphabet[new_index]
    print( 'encrypted text:', encrypted_text)
cipher_key(text,13)

