from parseconfigfile import parseConfigFile

configFilePath = "./test.config"
print("Successfully parsed config file")
configVals = parseConfigFile(configFilePath)
print(configVals)

print("Unsuccessfully parsed config file")
invalidFilePath = "not an existing file"
badConfigVals = parseConfigFile(invalidFilePath)
print(badConfigVals)