# Typles

'''
Start up a REPL to test these out
'''

T = (1, 2, 3, 4)                                    # A 4-item tuple
len(T)                                              # Length
# 4
T + (5, 6)                                          # Concatenation: a new tuple
# (1, 2, 3, 4, 5, 6)
T[0], T[1:]                                         # Indexing, slicing, and more
#(1, (2, 3, 4,))

T.index(4)                                          # Tuple methods: 4 appears at offset 3
# 3
T.count(4)                                          # 4 appears once
# 1

T[0] = 2                                            # Tuples are immutable
# TypeError: 'typle' object does not support item assignment
T = (2,) + T[1:]                                    # Make a new tuple for a new value
T
# (2, 2, 3, 4)

T = 'hack', 3.0, [11, 22, 33]
T
# ('hack', 3.0, [11, 22, 33])
T[1]
# 3.0
T[2][1]
# 22
T.append(4)
# AttributeError: 'tuple' object has no attribute 'append'