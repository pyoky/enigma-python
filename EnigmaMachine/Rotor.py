
'''
The Rotor class describes an Enigma rotor. It can be one of the three rotors
that was used by the German military during WW2.

@author: Pyokyeong Son
@date: 2017-10

Limitations:
- Ignores ring settings
- Only has 3 rotors to choose from

'''

class Rotor:

    rotorWiring = [{
        # M3 Rotor I
        "A":"E", "B":"K", "C":"M", "D":"F", "E":"L", "F":"G", "G":"D", "H":"Q",
        "I":"V", "J":"Z", "K":"N", "L":"T", "M":"O", "N":"W", "O":"Y", "P":"H",
        "Q":"X", "R":"U", "S":"S", "T":"P", "U":"A", "V":"I", "W":"B", "X":"R",
        "Y":"C", "Z":"J"}, {
        # M3 Rotor II
        "A":"A", "B":"J", "C":"D", "D":"K", "E":"S", "F":"I", "G":"R", "H":"U",
        "I":"X", "J":"B", "K":"L", "L":"H", "M":"W", "N":"T", "O":"M", "P":"C",
        "Q":"Q", "R":"G", "S":"Z", "T":"N", "U":"P", "V":"Y", "W":"F", "X":"V",
        "Y":"O", "Z":"E"}, {
        # M3 Rotor III
        "A":"B", "B":"D", "C":"F", "D":"H", "E":"J", "F":"L", "G":"C", "H":"P",
        "I":"R", "J":"T", "K":"X", "L":"V", "M":"Z", "N":"N", "O":"Y", "P":"E",
        "Q":"I", "R":"W", "S":"G", "T":"A", "U":"K", "V":"M", "W":"U", "X":"S",
        "Y":"Q", "Z":"O"
        }
    ]

    def __init__(self, rotorNumber):
        # The rotor's dictionary is set according to what it is
        self.rotorDictionary = self.rotorWiring[rotorNumber-1]

        # An inverse dictionary, for when the signal is traveling backwards
        self.rotorInverseDictionary = {v: k for k, v in self.rotorDictionary.iteritems()}

    def rotorSubstitution(self, inputValue): # Performs a forward substitution
        return self.rotorDictionary[inputValue]

    def rotorInverseSubstitution(self, inputValue): # Performs a backward substitution
        return self.rotorInverseDictionary[inputValue]
