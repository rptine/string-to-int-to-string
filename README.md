# string-to-int-to-string
Deterministic method of converting any string to an int, and also converting any int to a string. 

## Description
Function ```stringToInt(s)``` converts any string to an integer. Conversely, function ```intToString(i)``` converts an integer to a string.  <br/>
These two functions are both deterministic, and will always produce identical outputs for the same input.
Thus, we can convert a string,```s```, to an int with the call ```stringToInt(s)```.  We could then convert this back to the original string, ```s```, with a call to ```intToString()```.  Thus, ```s = intToString(stringToInt(s))```.
