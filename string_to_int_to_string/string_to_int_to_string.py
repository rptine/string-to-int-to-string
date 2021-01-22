import math

def string_to_bit_list(string_to_convert):
    """
    Converts any string to a list of 0's and 1's, deterministaclly. Obtains the unicode value 
    for each character in the string, converts each unicode value to a binary value represented
    as a list of 0's and 1's, pads the binary reprsentation to 8 bits, and concatenates the list
    of binaries for each character together.

    Args:
        string_to_convert: any string (no limit to character types of size)

    Returns:
        The input string represented as a list of 0's and 1's
    """
    total_uni_val_bit_list = []
    for char in string_to_convert:
        char_uni_val = ord(char) 
        char_uni_val_bit_list = []
        while char_uni_val >=1:
            char_uni_val_bit_list = [char_uni_val % 2] + char_uni_val_bit_list
            char_uni_val = math.floor(char_uni_val / 2)
        # Pad the binary representation to 8 bits
        char_uni_val_bit_list = pad_bits(char_uni_val_bit_list,8)
        total_uni_val_bit_list += char_uni_val_bit_list
    return total_uni_val_bit_list


def bit_list_to_int(bit_list):
    """
    Converts binary number represented as a list of 0's and 1's into its corresponding base 10
    integer value.

    Args:
        bit_list: a binary number represented as a list of 0's and 1's

    Returns:
        The base 10 integer value of the input binary number
    """
    bit_string = ''.join([('0','1')[b] for b in bit_list])
    return int(bit_string, 2)


def string_to_int(string_to_convert):
    """
    Orchestrator function to convert a string to a base 10 integer, using the unicode values of the
    characters in the string.

    Args:
        string_to_convert: any string

    Returns:
        A base 10 integer calculated from the unicode values of the characters in the string.
    """
    bit_list = string_to_bit_list(string_to_convert)
    return bit_list_to_int(bit_list)


def binstring_to_bit_list(binstring): 
    """
    Converts a string composed of only 0's and 1's, into a list of 0's and 1's ()

    Args:
        binstring: a string containing only 0's and 1's

    Returns:
        A list of 0's and 1's, with identical frequency and ordering the 0's and 1's in the 
        input string. 
    """
    bit_list = []
    for bit in binstring:
        bit_list.append(int(bit))
    return bit_list


def pad_bits(bit_list, desired_size):
    """
    Adds 0's to the head of bit_list so that bit_list has a length equal to desired_size. In other
    words, adds [desired_size - len(bit_list)] 0's to the bit_

    Args:
        bit_list: a list of 0's and 1's
        desired_size: an integer representing the desired size of the bit list

    Returns:
        The input bit_list with leading 0's inserted so that bit_list is of size desired_size.
    
    Raises:
        ValueError: The desired size of the padded list is smaller than the binary to be padded
    """
    if len(bit_list) > desired_size:
        raise ValueError("Binary number is larger than desired size!")
    num_zeros_needed = desired_size-len(bit_list)
    padded_list = [0] * (num_zeros_needed) + bit_list
    return padded_list


def bit_list_to_string(padded_bit_seq):
    """
    Converts a list of 0's and 1's to a string of alpha/numeric characters

    Args:
        padded_bit_seq: a list of 0's and 1's, such that the: (size of the list) mod 8 = 0

    Returns:
        A string of alpha/numeric characters
    """
    char_builder = ''
    # Iterate through by 8's, as each padded bit sequence is 8 bits long
    for segment in range(0,len(padded_bit_seq), 8): 
        # concatenate each new char onto the built up string, following the pattern for encoding
        char_builder = char_builder + bits_to_char(padded_bit_seq[segment: segment+8]) 
    return char_builder

def bits_to_char(bit_seq):
    """
    Converts a list of size 8, composed of 0's and 1's, into a character. Obtains the base 10 value
    represented by the list of 0's and 1's, and finds the corresponding unicode char for that base
    10 value.

    Args:
        bit_seq: a list of size 8, composed of 0's and 1's

    Returns:
        A character, whose unicode value is equal to the binary value encoded by the list of 0's 
        and 1's
    """
    value = 0
    for bit in bit_seq:
        value = (value * 2) + bit # This for loop will determine the numeric value of the binary bit sequence input
    return chr(value)

def int_to_string(integer_to_convert):
    """
    Wrapper function for above four funtions to convert an integer of base 10 to a string based on the ASCII values of 
    its characters
    """
    binary = bin(integer_to_convert)[2:] # convert input to string representing input's binary value
    bit_seq = binstring_to_bit_list(binary)
    bit_seq_size = len(bit_seq)
    desired_bit_seq_size = bit_seq_size + (8-bit_seq_size % 8) # desired size is min size, such that size mod 8 = 0
    padded_bit_seq = pad_bits(bit_seq, desired_bit_seq_size)
    converted_string = bit_list_to_string(padded_bit_seq)
    return converted_string

###### Example of converting a string to an int, and back to a string ######
exampleString = "orange"
exampleNum = string_to_int(exampleString)
backToString = int_to_string(exampleNum)
print("{} {} {}".format(exampleString, exampleNum, backToString))
