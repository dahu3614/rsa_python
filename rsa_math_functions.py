# Python implementation of RSA Encryption / Decryption Algorithm
# Basic Math Functions for RSA
# Author: David Hughes
# Last Modified: 31 Jan 2022

import message_preprocessing

def FME(b, n, m):
    """
    Returns b**n mod m using the Fast Modular Exponentiation algorithm.
    
    Args:
        b (int): Base
        n (int): Exponent
        m (int): Modulus
        
    Returns:
        result (int): b**n mod m
        
    """  
    
    # Initialize variable for result
    result = 1
    
    # Get binary expansion for n as a string
    n_binary_string = message_preprocessing.Convert_Binary_String(n)
    
    # Initialize value for start of modular exponentiation
    mod_exp = b % m
    
    # Iterate through binary expansion from least significant digit to most significant digit
    for binary_digit in reversed(n_binary_string):
        
        # If this modular exponentiation coefficient is part of the binary expansion, update result
        if binary_digit == '1':
            result = (result * mod_exp) % m
        
        # Update modular exponentiation coefficient (Square and Mod)
        mod_exp = (mod_exp * mod_exp) % m
        
    return result

def Euclidean_Alg(a, b):
    """
    Returns the Greatest Common Divisor of a and b.
    
    Unless b==0, the result will have the same sign as b
    (so that when b is divided by it, the result comes out positive).
    
    Args:
        a, b (int): Integers for which the function will find the GCD
        
    Returns:
        gcd (int): GCD of input integers
        
    """
        
    # Deal with possible negative inputs. Since GCD is always positive, convert to positive numbers
    a = abs(a)
    b = abs(b)
    
    # Check that a is greater than b, if not, switch a and b
    if b > a:
        placeholder = b
        b = a
        a = placeholder

    # Successively take mod operation until remainder is zero
    while b > 0:
        
        # Find remainder of a mod b
        c = a % b
        
        # Set modulo (b) as new (a)
        a = b
        
        # Set remainder (c) as new modulo (b)
        b = c

    gcd = a
    return gcd

def Extended_Euclidean_Algorithm(m, n):
    """
    Finds the gcd of m, n
    Returns gcd, as well as the Bezout coefficients s, t
    
    Args:
        m, n (int): Integers for which the function will find the GCD
        
    Returns:
        gcd (int): GCD of input integers
        s, t (int): Bezout coefficients (s * m + t * n = gcd)
        
    """
    
    # Store initial values of m and n
    (m0, n0) = (m, n)
    
    # Initialize values for Bezout coefficients to be updated by Extended Euclidean Algorithm
    (s1, t1) = (1, 0)
    (s2, t2) = (0, 1)
    
    # Use Extended Euclidean Algorithm to iteratively update Bezout coefficients to find modular inverse
    while n > 0:
        
        # Loop invariant
        m_invariant = s1 * m0 + t1 * n0
        n_invariant = s2 * m0 + t2 * n0
    
        # Find remainder of m mod n
        k = m % n
        
        # Find quotient of m // n
        q = m // n
        
        # Set modulus (n) as new value of m as per Euclid's Algorithm
        m = n
        
        # Set remainder (k) as new modulus (n) as per Euclid's Algorithm
        n = k
        
        # Calculate new Bezout coefficients and assign to placeholder variables
        (s1_hat, t1_hat) = (s2, t2)
        (s2_hat, t2_hat) = (s1 - q * s2, t1 - q * t2)
        
        # Update values of Bezout coefficients from placeholder variables
        (s1, t1) = (s1_hat, t1_hat)
        (s2, t2) = (s2_hat, t2_hat)
        
    # GCD of m and n is the final value of m when loop terminates
    gcd = m
    
    # Bezout coefficients are final values of s1 and t1 when loop terminates
    (s, t) = (s1, t1)
    
    return (gcd, s, t)