import re
from collections import Counter

from utils import find_gcd_of_list
def encrypt(plain_text, key):
    """
    Encrypt the plaintext using the Vigenere cipher with a given key.
    """
    encrypted_text = ""
    key_length = len(key)
    key_index = 0
    for i in range(len(plain_text)):
        char = plain_text[i]
        if char.isalpha():
            shift = ord(key[key_index % key_length].upper()) - 65
            key_index += 1 
            if char.isupper():
                encrypted_text += chr((ord(char) + shift - 65) % 26 + 65)
            else:
                encrypted_text += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(cipher_text, key):
    """
    Decrypt the ciphertext using the Vigenere cipher with a given key.
    """
    decrypted_text = ""
    key_length = len(key)
    key_index = 0  # New variable to keep track of the key's position
    for i in range(len(cipher_text)):
        char = cipher_text[i]
        if char.isalpha():
            shift = ord(key[key_index % key_length].upper()) - 65
            if char.isupper():
                decrypted_text += chr((ord(char) - shift - 65) % 26 + 65)
            else:
                decrypted_text += chr((ord(char) - shift - 97) % 26 + 97)
            key_index += 1  # Increment only when an alphabetic character is encountered
        else:
            decrypted_text += char
    return decrypted_text

def kasiski_examination(cipher_text):
    """
    Performs the Kasiski examination on a given ciphertext.
    Returns suggested key lengths based on repeated sequences.
    """
    max_length = 25
    sequences = []

    for seq_len in range(3, max_length + 1):
        sequences.extend(re.findall(r'(?=(\w{' + str(seq_len) + '}))', cipher_text))

    distances = []

    for seq in set(sequences):
        matches = [m.start() for m in re.finditer(seq, cipher_text)]
        if len(matches) > 1:
            distances.extend([matches[i+1] - matches[i] for i in range(len(matches)-1)])

    factors = []
    for dist in distances:
        factors.append(find_gcd_of_list([dist, distances[0]]))

    # Return the most common factor
    return Counter(factors).most_common(1)[0][0]



def index_of_coincidence(text):
    """
    Calculate and return the index of coincidence for a given text.
    """
    frequency = [text.count(chr(i + 65)) for i in range(26)]
    total_chars = len(text)
    ic = sum([(freq * (freq - 1)) for freq in frequency]) / (total_chars * (total_chars - 1))
    return ic

def deduce_key_length(cipher_text, max_key_length=25):
    """
    Use Index of Coincidence to deduce the potential key length.
    """
    key_lengths = []
    for key_length in range(1, max_key_length + 1):
        segments = [cipher_text[i::key_length] for i in range(key_length)]
        avg_ioc = sum(index_of_coincidence(segment) for segment in segments) / key_length
        # Assume English text IoC as a threshold
        if 0.060 < avg_ioc < 0.075:
            key_lengths.append(key_length)
    return key_lengths

def deduce_key(cipher_text, key_length):
    """
    Deduce the key using frequency analysis.
    """
    key = ""
    for i in range(key_length):
        segment = cipher_text[i::key_length]
        freqs = Counter(segment)
        most_common = freqs.most_common(1)[0][0]
        shift = (ord(most_common.upper()) - ord('E')) % 26  
        key_char = chr(ord('A') + shift)
        key += key_char
    return key


def vigenere_analysis(cipher_text):
    key_lengths = deduce_key_length(cipher_text)
    print("Suggested Key Lengths:", key_lengths)

    for key_length in key_lengths:
        deduced_key = deduce_key(cipher_text, key_length)
        print(f"Key of length {key_length}: {deduced_key}")
