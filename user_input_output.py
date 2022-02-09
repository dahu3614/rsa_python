# Python implementation of RSA Encryption / Decryption Algorithm
# User Input / Output Functions
# Author: David Hughes
# Last Modified: 31 Jan 2022

import random
import rsa_encode_decode
import factorization_algorithms
import rsa_math_functions

def Generate_Primes():
    """
    A function for picking two random prime numbers between 1 and 1000.
    
    Args:
        None
        
    Returns:
        p, q (int): prime integers between 1 and 1000
    """

    # List of prime numbers from 1 to 1000
    primes_1_to_1000 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

    # Choose two random prime numbers, p and q from this list
    # Randomly choose p from the list
    import random
    p = primes_1_to_1000[random.randint(0, len(primes_1_to_1000) - 1)]

    # Ensure q is not equal to p. While loop will terminate when a distinct value is chosen
    q = p
    while q == p:
        q = primes_1_to_1000[random.randint(0, len(primes_1_to_1000) - 1)]

    # Print output
    print("p = ", p)
    print("q = ", q)

    return (p, q)

def Generate_RSA_Keys():
    """
    A function for generating public and private key pairs using the RSA Algorithm.
    
    Args:
        None
        
    Returns:
        n, e (int): RSA Public Key
        d (int): RSA Private Key
    """

    # Get prime factors
    (p, q) = Generate_Primes()

    # Get public key
    (n, e) = rsa_encode_decode.Find_Public_Key_e(p,q)

    # Get private key
    d = rsa_encode_decode.Find_Private_Key_d(e,p,q)

    # Print output
    print("The prime factors are: {} and {}".format(p,q))
    print("Your public key (n, e) is:")
    print(n, e)
    print("Your private key (n, d) is:")
    print(n, d)
    return (n, e, d)

def Validate_Positive_Integer(input_text):
    """
    A function for validating input to be a positive integer
    
    Args:
        input_text (string): User input
        
    Returns:
        validation, integer (bool, int): Tuple containing a boolean flag if the user input was a positive integer
                                            and the corresponding integer (0 if invalid input)
    """

    # Validate input to be a positive integer
    try:
        n = int(input_text)

        # Check if n is greater than zero
        if n > 0:
            return (True, n)

        # If n is less than or equal to zero
        else:
            print("n must be a positive integer, please try again")
            return (False, 0)

    # If n is not an integer, test will fail
    except ValueError:
        print("Please enter an integer")
        return (False, 0)

def Encode_Message():
    """
    A function for encoding a message using the RSA Algorithm
    
    Args:
        None - Gets user input
    
    Returns:
        encrypted_message (list): List of integers representing ciphertext
    
    """

    # Get public key for encoding

    # Validate n to be a positive integer
    validation = False
    while validation == False:
        (validation, n) = Validate_Positive_Integer(input("Please enter public key \n n: "))

    # Validate e to be a positive integer
    validation = False
    while validation == False:
        (validation, e) = Validate_Positive_Integer(input("Please enter public key \n e: "))

    # If e is a positive integer, check if valid pair with n
    # Initialize gcd
    gcd = 0

    while gcd != 1:

        # Factorize n
        p = factorization_algorithms.pollards_rho(n)
        q = n // p

        print("p =", p)
        print("q =", q)

        # Check if relatively prime to (p - 1)(q - 1)
        gcd = rsa_math_functions.Euclidean_Alg(e, (p - 1) * (q - 1))

        print("gcd =", gcd)

        # If not relatively prime
        if gcd != 1:

            # Get new values of n and e
            print("Your value of e is not relatively prime to your value of n")
            print("Please re-enter your values for n and e")

            # Validate n to be a positive integer
            validation = False
            while validation == False:
                (validation, n) = Validate_Positive_Integer(input("Please enter public key \n n: "))

            # Validate e to be a positive integer
            validation = False
            while validation == False:
                (validation, e) = Validate_Positive_Integer(input("Please enter public key \n e: "))

    # If n and e are valid, move on to encoding

    # To allow encoding of multiple messages with the same public key, we will use a while loop with a flag
    # Set flag for encoding multiple messages. If True, continue encoding, if False, stop encoding
    continue_encoding = True

    while continue_encoding == True:

        # Get message
        message = input("Please enter a message: ")

        # Encode message
        encrypted_message = rsa_encode_decode.Encode(n, e, message)
        print("Encrypted Message:", encrypted_message, "\n")

        # Ask if user wants to continue
        if input("Do you want to encode another message? Enter 'Y' or 'N'").upper() != "Y":

            # If input is not 'Y', stop encoding
            continue_encoding = False

    return encrypted_message

def Get_Ciphertext():
    """
    A function for getting an encrypted ciphertext message
    
    Args:
        None - Gets user input
    
    Returns:
        ciphertext (list): List of integers representing ciphertext
    """

    # Get message
    encrypted_message = input("Please enter a list of ciphertext separated by commas and surrounded by brackets: ")

    # Convert to list of ciphertext
    # Strip brackets
    encrypted_message_no_brackets = encrypted_message.strip("[]")

    # Split on commas
    ciphertext_string = encrypted_message_no_brackets.split(",")

    # Cast list to integers
    ciphertext = []
    for cipher in ciphertext_string:
        ciphertext.append(int(cipher))

    return ciphertext

def Decode_Message():
    """
    A function for decoding a message using the RSA Algorithm
    
    Args:
        None - Gets user input
    
    Returns:
        decrypted_message (string): Plaintext decryption of input ciphertext
    """

    # Get private key for decoding

    # Validate n to be a positive integer
    validation = False
    while validation == False:
        (validation, n) = Validate_Positive_Integer(input("Please enter private key \n n: "))

    # Validate d to be a positive integer
    validation = False
    while validation == False:
        (validation, d) = Validate_Positive_Integer(input("Please enter private key \n d: "))

    # If n and d are valid, move on to decryption

    # To allow encoding of multiple messages with the same public key, we will use a while loop with a flag
    # Set flag for encoding multiple messages. If True, continue encoding, if False, stop encoding
    continue_encoding = True

    while continue_encoding == True:

        ciphertext = Get_Ciphertext()

        # Decode message
        decrypted_message = rsa_encode_decode.Decode(n, d, ciphertext)
        print("Decrypted Message:", decrypted_message, "\n")

        # Ask if user wants to continue
        if input("Do you want to decode another message? Enter 'Y' or 'N'").upper() != "Y":

            # If input is not 'Y', stop encoding
            continue_encoding = False

    return decrypted_message

def Break_Code(n, e, encrypted_message):
    """
    This function takes in a public key and ciphertext, and breaks the RSA encryption by factoring the modulo n in the public key.
    
    Args:
        n, e (int): RSA Public Key
        encrypted_message (list): List of integers representing ciphertext
    
    Returns:
        decrypted_message (string): Plaintext decryption of input ciphertext
    """
    # Get the first factor of n
    p = factorization_algorithms.pollards_rho(n)
    
    # Get the second factor of n
    q = n // p

    # Generate the private key using the Find_Private_Key_d function
    d = rsa_encode_decode.Find_Private_Key_d(e, p, q)
    print("Private Key d =", d)

    # Decrypt the message using the private key
    decrypted_message = rsa_encode_decode.Decode(n, d, encrypted_message)
    
    return decrypted_message