import itertools
import re
import sys
from collections import defaultdict

class DecoderRing(defaultdict):
    def __missing__(self, key):
        return key

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = range(1, 27)

inF = open(sys.argv[1])
lines = inF.readlines()

key = (lines[0].split(" ")[0], int(lines[0].split(" ")[1]))
message = lines[1].rstrip()

inF.close()

ring = DecoderRing()

letter_ring = itertools.cycle(letters)
number_ring = itertools.cycle(numbers)

ring[str(key[1])] = key[0]

while key[0] != letter_ring.next():
    continue
while key[1] != number_ring.next():
    continue

for i in range(26):
    ring[str(number_ring.next())] = letter_ring.next()

pattern = re.compile(r'\b(' + '|'.join(ring.keys()) + r')\b')
result = pattern.sub(lambda x: ring[x.group()], message)

print re.sub('-', '', result)
