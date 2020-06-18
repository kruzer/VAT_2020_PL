#!/usr/bin/env python3
def main():
    import sys
    oldCode=''
    oldVat=''
    for line in sys.stdin:
        fields = line.rstrip().split(',')
        if len(fields) >= 2:
            if oldCode == fields[0]:
                print(f"{oldCode},{oldVat}\n{fields[0]},{fields[1]}")
            else:
                oldCode, oldVat=fields


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
    main()
