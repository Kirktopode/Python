string = 'X-DSPAM-Confidence: 0.8475'
x = string.find(" ")
substring = str(string[x:])
datfloat = float(substring)
test = datfloat*1
print test
