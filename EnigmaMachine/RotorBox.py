
'''
The RotorBox class describes the encryption done by the 3 rotors in the rotor
of the enigma. This only handles the rotors, not the plugboard or the reflector.

@author: Pyokyeong Son
@date: 2017-10

Limitations:
- Can only hold 3 rotors
- Rotor order is fixed
'''

from Rotor import Rotor

class RotorBox:

    alphabet = [
        "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
        "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", ]

    def __init__(self, initialStep): # assumes rotor order is I II III
        self.rotorStep = initialStep

        # Make 3 rotors, I, II, and III
        self.rotorA = Rotor(1)
        self.rotorB = Rotor(2)
        self.rotorC = Rotor(3)

    def getRotorBoxOutput(self, inputLetter): # Encrypts the letter through 3 forward rotor substitutions
        self.rotorStep[2] += 1

        inputLetter = self.inputTranslator(inputLetter, self.rotorStep[2])

        self.outputC = self.outputTranslator(self.rotorC.rotorSubstitution(inputLetter), self.rotorStep[2])
        self.outputC = self.inputTranslator(self.outputC, self.rotorStep[1])

        self.outputB = self.outputTranslator(self.rotorB.rotorSubstitution(self.outputC), self.rotorStep[1])
        self.outputB = self.inputTranslator(self.outputB, self.rotorStep[0])

        self.outputA = self.outputTranslator(self.rotorA.rotorSubstitution(self.outputB), self.rotorStep[0])

        return self.outputA

    def getInverseRotorBoxOutput(self, inputLetter): # Encrypts the letter through 3 backwards rotor substitutions
        inputLetter = self.inputTranslator(inputLetter, self.rotorStep[0])

        self.outputA = self.outputTranslator(self.rotorA.rotorInverseSubstitution(inputLetter), self.rotorStep[0])
        self.outputA = self.inputTranslator(self.outputA, self.rotorStep[1])

        self.outputB = self.outputTranslator(self.rotorB.rotorInverseSubstitution(self.outputA), self.rotorStep[1])
        self.outputB = self.inputTranslator(self.outputB, self.rotorStep[2])

        self.outputC = self.outputTranslator(self.rotorC.rotorInverseSubstitution(self.outputB), self.rotorStep[2])

        return self.outputC

    def outputTranslator(self, inputValue, step): # Corrects the output signal of the rotors for the Stepping
        index = self.alphabet.index(inputValue) - step
        while index < 0: index += 26 # Handling underflow; e.g. index = -10
        return self.alphabet[index]

    def inputTranslator(self, inputValue, step): # Corrects the input signal of the rotors for the Stepping
        index = self.alphabet.index(inputValue) + step # Handling overflow; e.g. index = 36
        while index > 25: index -= 26
        return self.alphabet[index]
