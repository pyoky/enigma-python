
import sys, os
sys.path.append(os.path.abspath(".."))

from EnigmaMachine.Enigma import Enigma
import itertools
import datetime

class Bombe:

    alphabet = [
        "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
        "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", ]

    def __init__(self, cypherText, plainText):
        self.cypherText = cypherText
        self.plainText = plainText
        self.counter = 0

    def iterateRotor(self):
        for i in range(26):
            for j in range(26):
                for k in range(26):
                    enigma1 = Enigma([i, j, k], self.plugBoardWiring)
                    count = 0
                    while True:
                        if enigma1.encrypt(self.plainText[count]) == self.cypherText[count]:
                            if count >= (len(self.plainText)-1): return [i, j, k]
                            count += 1
                            continue
                        else:
                            break
        return -1

    def iteratePlugboard(self):
        choose10 = list(itertools.combinations(self.alphabet, 20))
        for lst in choose10:
            for x in self.all_pairs(list(lst)):
                self.plugBoardWiring = dict(x)
                self.plugBoardWiring.update({v: k for k, v in self.plugBoardWiring.iteritems()})
                self.iterateRotor()

                self.counter += (26*26*26)
                if (self.counter % 100) == 0:
                    print "\n# Current Time: " + str(datetime.datetime.now())
                    print "# Current Testing Plugboard Wiring: " + str(x)
                    print "# Current Test Key Count: " + str(self.counter)

                isPlugCorrect = self.iterateRotor()

                if isPlugCorrect != -1:
                    return [isPlugCorrect, self.plugBoardWiring]

    def all_pairs(self, lst):
        if len(lst) < 2:
            yield lst
            return
        a = lst[0]
        for i in range(1,len(lst)):
            pair = (a,lst[i])
            for rest in self.all_pairs(lst[1:i]+lst[i+1:]):
                yield [pair] + rest


bombe1 = Bombe("WETTERBERICHT", "ODHCOKPPIVESP")

print "Enigma Settings are : " + str(bombe1.iteratePlugboard())
