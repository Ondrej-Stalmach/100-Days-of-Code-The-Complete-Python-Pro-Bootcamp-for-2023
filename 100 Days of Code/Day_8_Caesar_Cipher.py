
from Day_8_Caesar_Cipher_Art import logo
print(logo)

def caesar(text_input,shift_value,direction_type):
    text_output = ""
    
    for char in text_input:
        if char in alphabet:
            if direction_type == "encode":
                positon_shifted = alphabet.index(char) + shift_value
            elif direction_type == "decode":
                positon_shifted = alphabet.index(char) - shift_value
            text_output = text_output + alphabet[positon_shifted]
        else:
             text_output = text_output + char

    if text_output == "":
        print("Only 'encode' or 'decode' are available")
    else:
        print(f"The {direction_type}d text is {text_output}")


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

state = True

while state:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number (< 26):\n"))

    caesar(text,shift,direction)
    ask = input("Type 'yes' to continue. Otherwise type 'no'.\n").lower()

    if ask == "no":
        state = False
        print("Goodbye")
        
       