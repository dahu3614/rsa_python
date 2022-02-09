# Python implementation of RSA Encryption / Decryption Algorithm
# RSA Encode and Decode Functions
# Author: David Hughes
# Last Modified: 31 Jan 2022

import random
import rsa_math_functions
import message_preprocessing

def Find_Public_Key_e(p, q):
    """
    Args: 
        p, q (int): 2 prime numbers
    
    Returns:
        n, e (int): Public key for RSA Encryption
    """
    
    # Calculate n: product of p and q
    n = p * q
    
    # Set initial value of e
    e = 0
    
    # Create temporary e variable for use inside the loop. Use a random integer between 3 and (p - 1) * (q - 1)
    temp_e = random.randint(3, (p - 1) * (q - 1))
    
    # Iteratively check to see if test value of e meets the conditions
    while e == 0:
        
        # Calculate GCD to see if it is relatively prime to (p - 1) * (q - 1)
        gcd = rsa_math_functions.Euclidean_Alg(temp_e, (p - 1) * (q - 1))
        
        # If GCD is 1 (relatively prime) and e is not equal to p or q, e meets conditions and loop can terminate
        if gcd == 1 and temp_e != p and temp_e != q:
            e = temp_e
            
        # If not, update value of temp_e and check again. Use a random integer between 3 and (p - 1) * (q - 1)
        else:
            temp_e = random.randint(3, (p - 1) * (q - 1))
    
    return (n, e)

def Find_Private_Key_d(e, p, q):
    """
    Finds the decryption exponent d such that d is the modular inverse of e. 
    Uses the Extended Euclidean Algorithm.
    
    Args: 
        p, q (int): 2 prime numbers used to generate public key
        e (int): First half of RSA Public Key
    
    Returns:
        d (int): Private key for RSA Encryption (modular inverse of e)
    """
    
    # We want to calculate the inverse of e, mod (p - 1) * (q - 1)
    
    # Calculate (p - 1) * (q - 1)
    m = (p - 1) * (q - 1)
    
    # Use Extended Euclidean Algorithm function to find Bezout Coefficients (s, t) of m and e
    (gcd, s, t) = rsa_math_functions.Extended_Euclidean_Algorithm(m, e)
    
    # t is modular inverse of e (Bezout's Theorem)
    d = t

    # If modular inverse is negative, keep adding m until you get a positive number
    while d <= 0:
        d += m
        
    return d

def Encode(n, e, message):
    """    
    Args: 
        n, e (int): RSA Public Key
        message (string): Input message for encryption
    
    Returns:
        cipher_text (list): List of integers corresponding to the encrypted message
    """
    # Initialize empty list to hold ciphertext
    cipher_text = []
    
    # Convert message to a list of numbers
    num_message = message_preprocessing.Convert_Text(message)
    
    # Iterate through list of number representations of characters in message, and encode each one by one
    for message_char in num_message:
        
        # Use Fast Modular Exponentiation to get ciphertext representation of character
        cipher = rsa_math_functions.FME(message_char, e, n)
        
        # Append to ciphertext list
        cipher_text.append(cipher)
    
    return cipher_text

def Decode(n, d, cipher_text):
    """
    Args: 
        n, d (int): RSA Private Key
        cipher_text (string): Input ciphertext for decryption
    
    Returns:
        message (string): Decrypted message
    """
    
    # Initialize empty list to hold decoded numbers
    decoded_num_list = []
    
    # Iterate through list of encoded numbers representing the characters in message, and decode each one by one
    for cipher_char in cipher_text:
        
        # Use Fast Modular Exponentiation with private key to decode character
        decoded_num = rsa_math_functions.FME(cipher_char, d, n)
        
        # Append to list of decoded numbers
        decoded_num_list.append(decoded_num)

    # Convert list of decoded numbers to string of decoded characters
    message = message_preprocessing.Convert_Num(decoded_num_list)
    
    return message