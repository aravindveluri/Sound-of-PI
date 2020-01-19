#!/usr/bin/env python3
#
#   Use Machin's Formula
#   pi = 4*(4*arctan(1/5) - arctan(1/239))
#   to calculate pi to one any place after the decimal.
#
import sys
from pysine import sine

def ArctanDenom(d, ndigits):
    # Calculates arctan(1/d) = 1/d - 1/(3*d^3) + 1/(5*d^5) - 1/(7*d^7) + ...
    total = term = (10**ndigits) // d
    n = 0
    while term != 0:
        n += 1
        term //= -d*d
        total += term // (2*n + 1)
    # print('ArctanDenom({}) took {} iterations.'.format(d, n))
    return total

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('USAGE: sound_of_PI.py ndigits')
        sys.exit(1)

    xdigits = 10             # Extra digits to reduce trailing error
    ndigits = int(sys.argv[1])

    # Use Machin's Formula to calculate pi.
    pi = 4 * (4*ArctanDenom(5,ndigits+xdigits) - ArctanDenom(239,ndigits+xdigits))

    # We calculated extra digits to compensate for roundoff error.
    # Chop off the extra digits now.
    pi //= 10**xdigits

    pi = str(pi)
    # frequencies for C4, D4, E4, F4, G4, A4, B4, C5
    cMajor = [261.626, 293.665, 329.628, 349.228, 391.995, 440.000, 493.883, 523.251]

    for digit in pi:
        # play the sound of PI in C Major Scale
        sine(frequency=cMajor[int(digit)%8], duration=0.5)
        
    sys.exit(0)