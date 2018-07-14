
'''
The Reflector class describes the Reflector in the Enigma. There are two types
of reflectors that can be used: the B, or C, both used by the German military.

@author: Pyokyeong Son
@date: 2017-10

'''


class Reflector:

    reflectorWiring = {
    "B": {
        # reflector B
        "A":"Y", "B":"R", "C":"U", "D":"H", "E":"Q", "F":"S", "G":"L", "H":"D",
        "I":"P", "J":"X", "K":"N", "L":"G", "M":"O", "N":"K", "O":"M", "P":"I",
        "Q":"E", "R":"B", "S":"F", "T":"Z", "U":"C", "V":"W", "W":"V", "X":"J",
        "Y":"A", "Z":"T"},
    "C": {
        # reflector C
        "A":"F", "B":"V", "C":"P", "D":"J", "E":"I", "F":"A", "G":"O", "H":"Y",
        "I":"E", "J":"D", "K":"R", "L":"Z", "M":"X", "N":"W", "O":"G", "P":"C",
        "Q":"T", "R":"K", "S":"U", "T":"Q", "U":"S", "V":"B", "W":"N", "X":"M",
        "Y":"H", "Z":"L"}}

    def __init__(self, reflectorType):
        # Choose between the two reflectors
        self.reflectorDictionary = self.reflectorWiring[reflectorType]

    def reflect(self, inputValue): # Simply reflects
        return self.reflectorDictionary[inputValue]
