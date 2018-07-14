
'''
The Plugboard class describes an Enigma's plugboard. The wiriing is currently
set to the wiring for 1941-08-17, during Operation Barbarossa, accoring to
http://cryptocellar.org/bgac/HillClimbEnigma.pdf this article.

@author: Pyokyeong Son
@data: 2017-10

'''

class Plugboard:

    def __init__(self, plugBoardWiring):
        self.plugBoardWiring = plugBoardWiring

    def plugThrough(self, inputValue): # Simple substitution according to the wiring
        if inputValue in self.plugBoardWiring: return self.plugBoardWiring[inputValue]
        else: return inputValue
