import re
import os.path

# @func parseConfigFile
# @param filePath: The path of the config file to parse
# Returns a dictionary object, where each value name is a field and maps to
# the value in the config file. If @filePath does not exist, returns an empty
# dict object.
def parseConfigFile(filePath):
    # @func convertValue
    # @param s: The string to convert
    # Checks if @s is an integer, float, bool, or string, and returns
    # the appropriate conversion.
    def convertValue(s):
        floatRegex = "^(\d+\.\d*$)|(\d*\.\d+$)"
        boolTrueRegex = "^(on|yes|true)$"
        boolFalseRegex = "^(off|no|false)$"
        if re.match(floatRegex, s):
            return float(s)
        if re.match(boolTrueRegex, s.lower()):
            return True
        if re.match(boolFalseRegex, s.lower()):
            return False
        if s.isnumeric():
            return int(s)
        return s  # keep as a raw string value
    if not os.path.exists(filePath):
        return {}
    config = {}
    with open(filePath, 'r') as configFile:
        for line in configFile:
            tokens = line.split('=')  # expect 2 tokens if not comment
            if not line or line[0] == '#' or len(tokens) != 2:
                continue
            fieldName = tokens[0].lstrip(' \t').rstrip()
            fieldVal = tokens[1].lstrip(' \t').rstrip()
            config[fieldName] = convertValue(fieldVal)
    return config