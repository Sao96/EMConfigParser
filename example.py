from parseconfigfile import parseConfigFile

configFilePath = "./test.config"
print("Successfully parsed config file\n")
configVals = parseConfigFile(configFilePath)
for field in configVals:
    print(field, ":", configVals[field])