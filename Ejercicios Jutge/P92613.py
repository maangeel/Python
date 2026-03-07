from decimal import ROUND_HALF_UP, Decimal
import math

num = float(input())
while not num >= 0:
    num = float(input())

numInf = math.floor(num)
numSup = math.ceil(num)
numRed = Decimal(str(num)).quantize(Decimal("1"), ROUND_HALF_UP)
print(numInf, numSup, numRed)