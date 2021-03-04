# Chiffre de Vigenère
import string

encrypted_str = 'bcx vdjh hr sadhqw hkwquv ci mriughzi phtrfh mri foq rr hksp'
key_word = 'do'
alphabet = list(string.ascii_lowercase)
len_alphabet = len(alphabet)

def key_letter():
    i = 0
    while True:
        yield alphabet.index(key_word[i])
        i += 1
        if i == len(key_word):
            i = 0

key = key_letter()
decrypted_str = ''

for letter in encrypted_str:
    if letter in (alphabet):
        n = alphabet.index(letter) - next(key)
        if n >= len_alphabet:
            n -= len_alphabet
        decrypted_str += alphabet[n]
    else:
        decrypted_str += letter

print(decrypted_str)
        
