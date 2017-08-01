def stringToBitList(message):
    """Converts a string with alphabetic, numeric and special characters to a list of 0's and 1's"""
    total = []
    for character in message:
        # Store Unicode code point of the character in c
        c = ord(character) 
        indiv = []
        # Convert the value in c to binary, and store this binary as a list of 0's and 1's
        while c > 0:
            indiv = [(c % 2)] + indiv
            c = c / 2
        # Pad the binary representation to 8 bits
        indiv = padBits(indiv,8)
        # Sum the padded binary representations of each character 
        total = total + indiv
    return total

def bitListToInt(bitList):
    """Converts a list of 0's and 1's, to an int of base 2"""
    return int(''.join([('0','1')[b] for b in bitList]),2)

def stringToInt(message):
    """Wrapper function for above two funtions to convert a 
    string to a base 10 integer based on the ASCII values of
     its characters"""
    return bitListToInt(stringToBitList(message))

def binstringToBitList(binstring): 
    """Converts a string of '0's and '1's to a list of 0's and 1's"""
    bitList = []
    for bit in binstring:
        bitList.append(int(bit))
    return bitList

def padBits(bits, padding):
    """Pad the input bits with 0's so that it is of length padding"""
    return [0] * (padding-len(bits)) + bits

def bitListToString(paddedBitSeq):
    """Converts a list of 0's and 1's to a string of alpha/numeric characters"""
    charBuilder = ''
    # Iterate through by 8's becaause each padded bit sequence is 8 bits long
    for segment in range(0,len(paddedBitSeq),8): 
        # concatenate each new char onto the built up string
        charBuilder = charBuilder + bitsToChar(paddedBitSeq[segment: segment+8]) 
    return charBuilder

def bitsToChar(bitSeq):
    """Converts each 8 bit length padded bit sequences 
    back to a char based on its unicode value"""
    value = 0
    for bit in bitSeq:
        value = (value * 2) + bit # This for loop will determine the numeric value of the binary bit sequence input
    return chr(value)

def intToString(integer):
    """Wrapper function for above four funtions to convert an i
    nteger of base 10 to a string based on the ASCII values of 
    its characters"""
    binary = bin(integer)[2:]
    bitSeq = binstringToBitList(binary)
    return bitListToString(padBits(bitSeq,(len(bitSeq)+(8-(len(bitSeq)%8)))))

###### Example of converting a string to an int, and back to a string ######
exampleString = "orange"
exampleNum = stringToInt(exampleString)
backToString = intToString(exampleNum)
print "{} {} {}\n".format(exampleString, exampleNum, backToString)
