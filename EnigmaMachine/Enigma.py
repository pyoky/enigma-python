
'''
The Engima class describes an Enigma machine. An Engima machine has an input mechanism,
an output mechanism, a plugboard, a rotorbox containing 3 rotors, and a reflector.

@author: Pyokyeong Son
@date: 2017-10

'''


from RotorBox import RotorBox
from Reflector import Reflector
from Plugboard import Plugboard

class Enigma:

    def __init__(self, rotorSettings, plugBoardWiring):
        self.rotorBox1 = RotorBox(rotorSettings)
        self.reflector1 = Reflector("B")
        self.plugboard1 = Plugboard(plugBoardWiring)

    def encrypt(self, inputValue):
        inputValue = self.plugboard1.plugThrough(inputValue)
        self.beforeReflection = self.rotorBox1.getRotorBoxOutput(inputValue)
        self.afterReflection = self.reflector1.reflect(self.beforeReflection)
        return self.plugboard1.plugThrough(self.rotorBox1.getInverseRotorBoxOutput(self.afterReflection))

def main():
    rotorSetting = [0, 0, 0]
    for i in range(3):
        rotorSetting[i] = int(raw_input("Rotor Settings #" + str(i+1) + " : "))
        '''
    plugBoardWiring = {
        'A': 'B', 'C': 'D', 'B': 'A', 'E': 'F', 'D': 'C', 'G': 'H', 'F': 'E',
        'I': 'J', 'H': 'G', 'K': 'L', 'J': 'I', 'M': 'N', 'L': 'K', 'O': 'T',
        'N': 'M', 'Q': 'P', 'P': 'Q', 'S': 'R', 'R': 'S', 'T': 'O'}
'''
    plugBoardWiring = {
        "A":"E", "C":"F", "G":"L", "H":"I", "K":"P",
        "M":"S", "N":"R", "O":"U", "Q":"Y", "T":"W",
        # simply reversed
        "E":"A", "F":"C", "L":"G", "I":"H", "P":"K",
        "S":"M", "R":"N", "U":"O", "Y":"Q", "W":"T" }
    


    enigma1 = Enigma(rotorSetting, plugBoardWiring)
    plainText = raw_input("Input String: ")
    for i in range(len(plainText)): print enigma1.encrypt(plainText[i]),
    #while True:
    #    print enigma1.encrypt(raw_input("Letter: "))

if __name__ == "__main__": main()
