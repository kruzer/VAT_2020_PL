#!/usr/bin/env python3
def duble():
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

if __name__ == "__main__":
    duble()
