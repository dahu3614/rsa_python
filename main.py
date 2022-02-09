# Python implementation of RSA Encryption / Decryption Algorithm
# Main Function
# Author: David Hughes
# Last Modified: 31 Jan 2022

import random
import rsa_encode_decode
import factorization_algorithms
import user_input_output

def main():
    """
    This function allows the user to navigate an interactive menu to develop RSA keys, encode messages, decode messages, and break codes.
    """
        
    # Introduction to the program
    print("Welcome to David Hughes' RSA Project!")
    
    # Initialize choice list
    choice_list = [1, 2, 3, 4]
    
    # Get user input and validate choice
    validation = False    
    while validation == False:
        (validation, choice) = user_input_output.Validate_Positive_Integer(input("""What do you want to do? \n 
            (1) Generate Public and Private Key Pairs \n 
            (2) Encode a Message \n 
            (3) Decode a Message \n 
            (4) Break a Code \n
            \n
Enter your choice (1, 2, 3, or 4):"""))
        if choice not in choice_list:
            validation = False
            print("Please enter a valid response")
        
    # Run program
    # Case 1: Generating Public and Private Keys
    if choice == 1:
        user_input_output.Generate_RSA_Keys()
    
    # Case 2: Encoding a Message
    elif choice == 2:
        user_input_output.Encode_Message()
        
    # Case 3: Decoding a Message
    elif choice == 3:
        user_input_output.Decode_Message()
        
    # Case 4: Breaking a Code
    elif choice == 4:
        
        # Initialize subchoice list
        subchoice_list = [1, 2, 3]
        
        # Get user input and validate choice
        validation = False    
        while validation == False:
            (validation, subchoice) = user_input_output.Validate_Positive_Integer(input("""What information do you have? \n 
            (1) Public Key and Ciphertext Only \n
            (2) Prime Factors and Ciphertext \n
            (3) Private Key and Ciphertext \n
Enter your choice (1, 2, or 3):"""))
            if subchoice not in subchoice_list:
                validation = False
                print("Please enter a valid response")
        
        # Run Program
        # Case 1: Public Key and Ciphertext Only
        if subchoice == 1:
            
            # Get n and validate to be a positive integer
            validation = False
            while validation == False:
                (validation, n) = user_input_output.Validate_Positive_Integer(input("Please enter public key \n n: "))

            # Get e and validate to be a positive integer
            validation = False
            while validation == False:
                (validation, e) = user_input_output.Validate_Positive_Integer(input("Please enter public key \n e: "))
            
            # Find a prime factor
            p = factorization_algorithms.pollards_rho(n)
            
            # Check if factorization function is valid
            if p != 0:
                
                # Find q
                q = n // p
                
                # Find d
                d = rsa_encode_decode.Find_Private_Key_d(e, p, q)
                print("Private Key d =", d)
                
                # Decode Message
                # To allow encoding of multiple messages with the same public key, we will use a while loop with a flag
                # Set flag for encoding multiple messages. If True, continue encoding, if False, stop encoding
                continue_encoding = True

                while continue_encoding == True:

                    ciphertext = user_input_output.Get_Ciphertext()

                    # Decode message
                    decrypted_message = rsa_encode_decode.Decode(n, d, ciphertext)
                    print("Decrypted Message:", decrypted_message, "\n")

                    # Ask if user wants to continue
                    if input("Do you want to decode another message? Enter 'Y' or 'N'").upper() != "Y":

                        # If input is not 'Y', stop encoding
                        continue_encoding = False
                
            else:
                print("Prime factor not found")
                        
        # Case 2: Prime Factors and Ciphertext
        elif subchoice == 2:
            
            # Get Public Key and Factor
            # Set flag to check if p is a factor
            is_p_a_factor = False
            
            while is_p_a_factor == False:
                
                # Get n and validate to be a positive integer
                validation = False
                while validation == False:
                    (validation, n) = user_input_output.Validate_Positive_Integer(input("Please enter public key \n n: "))

                # Get p and validate to be a positive integer
                validation = False
                while validation == False:
                    (validation, p) = user_input_output.Validate_Positive_Integer(input("Please enter one prime factor \n p: "))

                    # Check if p is actually a factor
                    if n % p != 0:
                        print("p is not a factor of n. Did you type them in correctly?")
                    
                    # If p is a factor, exit loop
                    if n % p == 0:
                        is_p_a_factor = True
                
            # Get e and validate to be a positive integer
            validation = False
            while validation == False:
                (validation, e) = user_input_output.Validate_Positive_Integer(input("Please enter public key \n e: "))
            
            # Find q
            q = n // p
            
            # Find d
            d = rsa_encode_decode.Find_Private_Key_d(e, p, q)
            print("Private Key d =", d)
            
            # Decode Message
            # To allow encoding of multiple messages with the same public key, we will use a while loop with a flag
            # Set flag for encoding multiple messages. If True, continue encoding, if False, stop encoding
            continue_encoding = True

            while continue_encoding == True:

                ciphertext = user_input_output.Get_Ciphertext()

                # Decode message
                decrypted_message = rsa_encode_decode.Decode(n, d, ciphertext)
                print("Decrypted Message:", decrypted_message, "\n")

                # Ask if user wants to continue
                if input("Do you want to decode another message? Enter 'Y' or 'N'").upper() != "Y":

                    # If input is not 'Y', stop encoding
                    continue_encoding = False
            
        # Case 3: Private Key and Ciphertext
        elif subchoice == 3:
            user_input_output.Decode_Message()
        
        # Other
        else:
            print("Quitting Program")
            
    # Other
    else:
        print("Quitting Program")
        
if __name__ == '__main__':
    main()