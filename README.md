# string-to-int-to-string
Deterministic method of converting any string to an int, and conversely converting any int to a string. 

## Description
Function ```string_to_int(s)``` converts any string to an integer. Conversely, function ```int_to_string(i)``` converts an integer to a string.
These two functions are both deterministic, and thus produce identical outputs for identical input.
Thus, we can convert a string,```"foo"```, to an int with:
```foo_int = string_to_int("foo")``` <br/>
We can then convert this back to the original string, ```"foo"```, with:
```int_to_string(foo_int)```<br/>
Thus, for any string, ```s```:
```s = int_to_string(string_to_int(s))```

### Installation
Install with pip: 
```pip install string_to_int_to_string```

Import into python file with:
 ```import string_to_int_to_string as stits```

### How to Use
* ```string_to_int(string_to_convert)```
    * Converts string to a base 10 integer, deterministically, using the unicode values of the characters in the string.
    * Arguments: string_to_convert: any string
    * Returns: A base 10 integer calculated from the unicode values of the characters in the string.

* ```int_to_string(integer_to_convert)```
    * Convert an integer of base 10 to a string, deterministically. Uses the *reverse process as string_to_int().
    * Arguments: string_to_convert: any string (no limit to character types of size)
    * Returns: The input string represented as a list of 0's and 1's

Convert a string, say ```bar```, to an integer with:
 ```bar_int = stits.string_to_int("bar")```.
Convert this integer back to the original string:
```original_string = sits.int_to_string(bar_int)```
