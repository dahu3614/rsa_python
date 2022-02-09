# Python implementation of RSA Encryption / Decryption Algorithm
# Message Preprocessing Functions
# Author: David Hughes
# Last Modified: 31 Jan 2022

def Convert_Text(_string):
    """
    Takes in a simple 
    string such as "hello" and outputs the corresponding
    standard list of integers (ASCII) for each letter in the word.
    For example:
    _string = hello
    integer_list = [104, 101, 108, 108, 111]
    
    Args:
        _string (string): Input text
        
    Returns:
        integer_list (list): ASCII values for each character in the word
        
    """
    
    # Initialize empty list for integer (ASCII) conversions of characters in the string 
    integer_list = []
    
    # Iterate through input string, convert each char to ASCII, and append to list
    for char in _string:
        integer_list.append(ord(char))
    
    return integer_list

def Convert_Num(_list):
    """
    The opposite of the Convert_Text
    function defined above.
    
    Takes in a list of integers
    and outputs the corresponding string (ascii).
    
    For example:
    _list = [104, 101, 108, 108, 111]
    _string = hello
    
    Args:
        _list (list): Input list of ASCII values
        
    Returns:
        _string (string): Corresponding text string
        
    """
    
    # Initialize empty string for text conversion of list of ASCII integers
    _string = ''
    
    # Iterate through list of ASCII integers, convert each one to a character, and append to string
    for i in _list:
        _string += chr(i)
        
    return _string

def Convert_Binary_String(_int):
    """
    Converts an integer to
    a string of its binary expansion.
    
    For example:
    _int = 345
    bits = 101011001
    
    Args:
        _int (int): Input decimal integer
        
    Returns:
        bits (string): Binary representation of decimal input
        
    """
    
    # Initialize empty string to hold binary expansion
    bits = ""
    
    # Every iteration divides the integer by 2 using integer division to get the next binary digit.
    # Keep running the loop until the integer is 0.
    while _int > 0:
        
        # Get next binary digit
        k = _int % 2
        
        # Cast to string and add digit to binary expansion at the front of the current string
        bits = str(k) + bits
        
        # Divide current value of _int by two, to prepare to get next binary digit 
        _int = _int // 2
        
    return bits