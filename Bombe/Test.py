
import itertools
import datetime

def all_pairs(lst):
    if len(lst) < 2:
        yield lst
        return
    a = lst[0]
    for i in range(1,len(lst)):
        pair = (a,lst[i])
        for rest in all_pairs(lst[1:i]+lst[i+1:]):
            yield [pair] + rest


alphabet = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", ]

count = 0
choose10 = list(itertools.combinations(alphabet, 20))
for lst in choose10:
    print "################ current list: " + str(lst) + "\n################ Time : " + str(datetime.datetime.now())
    for x in all_pairs(list(lst)):
        count += 1
        if count == 1000000:
            count = 0
            print "################ Time : " + str(datetime.datetime.now())
