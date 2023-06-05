## Day 8 - Beginner | Function Parameters & Caesar Cipher
## 05.06.2023
## ----
## DAY 8 PROJECT PRACTICE | Ceasar Cipher
## ----

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
#TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
    #e.g.
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

def encrypt(text, shift):
    encrypted_text = ''
    for letter in text:
        if letter != ' ':
            if alphabet.index(letter) + shift > len(alphabet):     ##TODO - 2
                new_idx = len(alphabet) - (alphabet.index(letter) + shift)
            else:
                new_idx = alphabet.index(letter) + shift
            encrypted_text += alphabet[new_idx]
        else:
            encrypted_text += ' '

    return encrypted_text

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
## TEST
#if direction == 'encode':
#    new_text = encrypt(text, shift)
#    print(f'The encoded text is {new_text}')

#TODO-4: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(text, shift):
    decrypted_text = ''
    for letter in text:
        if letter != ' ':
            new_idx = alphabet.index(letter) - shift
            decrypted_text += alphabet[new_idx]
        else:
            decrypted_text += ' '

    return decrypted_text
  #TODO-5: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.
  #e.g.
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"
  ## TEST
#if direction == 'decode':
#    original_text = decrypt(text, shift)
#    print(f'The decoded text is {original_text}')

#TODO-6: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
if direction == "encode":
    encrypt(text = text, shift = shift)
elif direction == "decode":
    decrypt(text = text, shift = shift)

#TODO-7: Combine the encrypt() and decrypt() functions into a single function called caesar().

def caesar(start_text, shift, direction):
    end_text = ""
    if direction == "decode":
        shift *= -1
    for letter in start_text:
        position = alphabet.index(letter)
        new_position = position + shift
        end_text += alphabet[new_position]
    print(f"Here's the {direction}d result: {end_text}")

caesar(text=text, shift=shift, direction=direction)