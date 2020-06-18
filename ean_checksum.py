#!/usr/bin/env python3
def ean_checksum():
    import sys
    for line in sys.stdin:
        fields = line.rstrip().split(',')
        if len(fields) >= 2:
            if validateCheckDigit(fields[0]):
                if fields[1] in ['5%','8%','23%']:
                    print(line.rstrip())


def checkDigit(digits):
    total = sum(digits) + sum([d*2 for d in digits[-1::-2]])
    return (10 - (total % 10)) % 10

def validateCheckDigit(bar):
    if len(bar) in (8,12,13,14) and bar.isdigit():
        digits = [ int(i) for i in bar]
        cd = checkDigit( digits[0:-1] )
        return cd == digits[-1]
    return False

if __name__ == "__main__":
    ean_checksum()
