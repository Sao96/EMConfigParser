# Einstein Medical Parser Assessment
My solution to the configuration parser.

## Important Notes
This is a parser written for python3. This was written and tested on a linux
machine, but is also likely portable with Windows OS and Mac OS out of the box.

## What it does
This parser reads through a configuration file, and returns a python dict
object which maps all config variables to their respective value in the file.

## How to use
Simply import the `parseConfigFile` function from `parseconfigfile.py`, and then
to parse and convert the config file into a dict object, execute 
`parseConfigFile(file_path_name)`, and that is all.

For a direct example of usage, please see the file `example.py`.

## Implementation Details
The configuration file is parsed line by line, and is examined for validity.
We consider a line valid if it is of the format variableName = some value,
and does not have a leading # character. All leading whitespace and trailing
whitespace from variable name and value are removed.

### Booleans
Any value who is either on, yes, or true is converted to True.

Any value who is either off, no, or false is converted to False.

### Integers
Any variable who holds a pure numeric value that has no decimal point is
converted into an integer.

### Floats
Any variable who holds a decimal value number is converted as a float. 
The exact format is any who matches a pattern of numbers to the left of a 
decimal point, to the right, or both.

### Strings
Any value who is not a boolean, integer, or float is automatically left
as the parsed string itself.