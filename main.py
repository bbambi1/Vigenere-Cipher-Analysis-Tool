import vigenere
import utils

def main():
    print("Welcome to the Vigenere Cipher tool!")

    action = input("Choose an action (encrypt, decrypt, analyze): ").lower()

    if action == 'encrypt':
        text = input("Enter the plaintext: ")
        key = input("Enter the key: ")
        cipher_text = vigenere.encrypt(text, key)
        utils.display_output(cipher_text)

    elif action == 'decrypt':
        text = input("Enter the ciphertext: ")
        key = input("Enter the key: ")
        plain_text = vigenere.decrypt(text, key)
        utils.display_output(plain_text)

    elif action == 'analyze':
        text = input("Enter the ciphertext for analysis: ")
        text = utils.clean_input(text)

        print("\nAnalysis Methods:")
        print("1. Kasiski Examination")
        print("2. IoC (Index of Coincidence)")
        print("3. Both")
        
        method = int(input("Choose your analysis method (1/2/3): "))
        
        possible_lengths = []

        if method == 1 or method == 3:
            key_length = vigenere.kasiski_examination(text)
            print(f"\nSuggested key length based on Kasiski examination: {key_length}")
            possible_lengths.append(key_length)
        
        if method == 2 or method == 3:
            ioc_lengths = vigenere.deduce_key_length(text)
            print(f"\nSuggested key lengths based on IoC: {ioc_lengths}")
            possible_lengths.extend(ioc_lengths)
            
        # Deduce the key and decrypt for each possible length
        for length in set(possible_lengths):  # Using set to remove duplicates
            deduced_key = vigenere.deduce_key(text, length)
            print(f"\nDeduced key of length {length}: {deduced_key}")
            decrypted_text = vigenere.decrypt(text, deduced_key)
            print(f"Decrypted text using deduced key: {decrypted_text[:100]}...")  # Displaying the first 100 characters for brevity
        
        # Calculate and display the index of coincidence
        ic = vigenere.index_of_coincidence(text)
        print(f"\nIndex of Coincidence: {ic:.4f}")

    else:
        print("Invalid action.")

if __name__ == "__main__":
    main()
