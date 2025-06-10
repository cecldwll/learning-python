# Numbers

'''
Start up a REPL to test these out
'''

123 + 222                       # Integer addition
# 345
1.5 * 4                         # Floating-point multiplication
# 6.0
1_234_567, 0x15, bin(21)        # Separators, hex, binary
# (1234567, 21, '0b10101')
2 ** 100                        # 2 to the power 100
# 1267650600228229401496703205376
len(str(2 ** 12345))            # How many digits in a really BIG number
# 3717

import math
math.pi                         
# 3.141592653589793
math.sqrt(85)
# 9.219544457292887

import random
random.random()
random.choice([1, 2, 3, 4])