# Python implementation of RSA Encryption / Decryption Algorithm
# Factorization Functions
# Author: David Hughes
# Last Modified: 31 Jan 2022

import random
import rsa_math_functions

def brute_force_factorize(n):
    """
    Naive brute force factorization algorithm to find the smallest factor of input n
    
    Args:
        n (int): Input integer to factorize
        
    Returns:
        i (int): Smallest factor of n (if n is prime, returns 0)
        
    """
    
    # Check each number from 2 to (n - 1) to see if it divides n
    for i in range(2, n - 1):
        
        # If i divides n, it is a factor
        if n % i == 0:
            return i
        
    # If factor is not found:
    print("Factor Not Found")
    return 0

def prime_list_factorize(n):
    """
    Slightly less naive factorization algorithm to find the smallest factor of input n using a list of primes to 1000
    
    Args:
        n (int): Input integer to factorize
        
    Returns:
        i (int): Smallest factor of n (if n is prime, returns 0)
        
    """
    
    # Initialize list of prime numbers from 1 to 1000
    primes_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
    
    # Find max prime
    max_prime = max(primes_list)
    
    # Check if n is small enough to be broken
    if n > max_prime ** 2:
        print("WARNING: Key may too large to be broken")
        
    # Either way, we will try it
    
    # Check each prime in the primes list
    for prime in primes_list:

        # If the prime divides n, it is a factor
        if n % prime == 0:
            return prime

    # If all prime numbers are exhausted, we have not found a factor
    print("Prime Factor Not Found")
    return 0

def factorize_tennessee_get_prime_list():
    """
    Reads in a list of first 100,008 prime numbers from University of Tennessee website
    
    Args:
        None
        
    Returns:
        prime_list (list): List of 100,008 prime numbers
    """
    
    # Define file with primes list
    prime_list_file = "primes_list.txt"
    
    # Define empty prime list
    prime_list = []

    # Open file
    with open(prime_list_file, 'r') as prime_list_text:

        # Initialize line reader
        prime_list_line = prime_list_text.readline()
        
        while prime_list_line:
            
            # Split into list
            split_line = prime_list_line.split()
            
            # Append to list
            for prime in split_line:                
                prime_list.append(int(prime.strip()))

            # Next line
            prime_list_line = prime_list_text.readline()
            
            # Skip blank lines
            prime_list_line = prime_list_text.readline()
            
    return prime_list

def prime_list_factorize_tennessee(n):
    """
    Slightly less naive factorization algorithm to find the smallest factor of input n using a list of the first 100,008 primes
    
    Args:
        n (int): Input integer to factorize
        
    Returns:
        prime (int): Smallest prime factor of n (if n is prime, returns 0)
    """
    
    # Initialize list of prime numbers from factorize_tennessee_get_prime_list
    primes_list = factorize_tennessee_get_prime_list()
    
    # Find max prime
    max_prime = max(primes_list)
    
    # Check if n is small enough to be broken
    if n > max_prime ** 2:
        print("WARNING: Key may too large to be broken")
        
    # Either way, we will try it
    
    # Check each prime in the primes list
    for prime in primes_list:

        # If the prime divides n, it is a factor
        if n % prime == 0:
            return prime

    # If all prime numbers are exhausted, we have not found a factor
    print("Prime Factor Not Found")
    return 0

def pollards_rho_pseudorandom(x, y, n):
    """
    Helper function for Pollard's Rho factorization algorithm.
    Generates a pseudorandom number.
    
    Args:
        x, y (int): Seeds for pseudorandom number generation
        n (int): Number to be factored using Pollard's Rho algorithm
        
    Returns:
        z (int): A pseudorandom number
    """
    
    # Generate next pseudorandom number
    z = (x * x + y) % n
    
    return z

def pollards_rho(n):
    """
    Factorization of a number n using Pollard's Rho Algorithm
    
    Args:
        n (int): Input integer to factorize
        
    Returns:
        p (int): Factor of n (if n is prime, returns 0)
    """
    
    # Initialize two "runners" to check for cycles
    a = random.randint(1, n)
    b = a
    
    # Initialize input for pseudorandom function
    y = random.randint(1, n)
    
    # First iteration
    
    # a goes through pseudorandom function once
    a = pollards_rho_pseudorandom(a, y, n)
    
    # b goes through psuedorandom function twice
    b = pollards_rho_pseudorandom(pollards_rho_pseudorandom(b, y, n), y, n)
    
    # Attempt to find prime factor
    p = rsa_math_functions.Euclidean_Alg(abs(b - a), n)
    
    # If p is a factor
    if p > 1:
        return p
    
    # Else, continue algorithm
    
    # Detect cycles
    while b != a:
        
        # a goes through pseudorandom function once
        a = pollards_rho_pseudorandom(a, y, n)
        
        # b goes through psuedorandom function twice
        b = pollards_rho_pseudorandom(pollards_rho_pseudorandom(b, y, n), y, n)
        
        # Attempt to find prime factor
        p = rsa_math_functions.Euclidean_Alg(abs(b - a), n)
        
        # If p is a factor
        if p > 1:
            return p
    
    # If cycle is found without generating a factor
    print("No factor found.")
    return 0