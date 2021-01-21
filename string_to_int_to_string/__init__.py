import string_to_int_to_string

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


def int_to_string(integer_to_convert):
    """
    Wrapper function for above four funtions to convert an integer of base 10 to a string based on the ASCII values of 
    its characters
    """
    binary = bin(integer_to_convert)[2:]
    bitSeq = binstring_to_bit_list(binary)
    return bit_list_to_string(pad_bits(bitSeq,(len(bitSeq)+(8-(len(bitSeq)%8)))))