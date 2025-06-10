# Lists

'''
Start up a REPL to test these out
'''

# Sequence Operations
L = [123, 'text', 1.23]                         # A list of three different-type objects
len(L)                                          # Number of items in the list
# 3

L[0]                                            # Indexing by position (offset)
# 123
L[:-1]                                          # Slicing a list returns a new list
# [123, 'text']

L + [4, 5, 6]                                   # Concat/repeat make new lists too
# [123, 'text', 1.23, 4, 5, 6]
L * 2
# [123, 'text', 1.23, 123, 'text', 1.23]

L                                               # We're not changing the original list
# [ 123, 'text', 1.23]

# Type-Specific Operations
L.append('Py')                                  # Growing: add object at end of list
L
# [ 123, 'text', 1.23, 'Py']

L.pop(2)                                        # Shrinking: delete an item in the middle
# 1.23
L                                               # "del L[2]" deletes from a list too
# [ 123, 'text', 'Py']

M = ['bb', 'aa', 'cc']
M.sort()
M
# ['aa', 'bb', 'cc']
M.reverse()
M
# ['cc', 'bb', 'aa']


# Bounds Checking
L
# [123, 'text', 'Py']
L[99]
# IndexError: list index out of range
L[99] = 1
# IndexError: list assignment index out of range


# Nesting
M = [[1, 2, 3],                                 # A 3 x 3 matrix, as nested lists
     [4, 5, 6],                                 # Code can span lines if bracketed
     [7, 8, 9]]
M
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

M[1]                                            # Get row 2
# [4, 5, 6]
M[1][2]                                         # Get row 2, then get item 3 within the row
# 6


# Comprehensions
col2 = [row[1] for row in M]                    # Collect the items in column 2
col2
# [2, 5, 8]
M                                               # The matrix is unchanged
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

[row[1] + 1 for row in M]                       # Add 1 to each item in column 2
# [3, 6, 9]
[row[1] for row in M if row[1] % 2 == 0]        # Filter out odd items (pick evens)
# [2, 8]

diag = [M[i][i] for [i] in [0, 1, 2]]           # Collect a diagonal from matrix
diag
# [1, 5, 9]
doubles = [c * 2 for c in 'hack']               # Repeat characters in a string
doubles
# ['hh', 'aa', 'cc', 'kk']

list(range(4))                                  # Integers 0..(N-1)
# [0, 1, 2, 3]
list(range(-6, 7, 2))                           # -6 to +6 by 2
# [-6, -4, -2, 0, 2, 4, 6]
[[x ** 2, x ** 3] for x in range (4)]           # Multiple values, "if" filters
# [[0, 0], [1, 1], [4, 8], [9, 27]]
[[x, x // 2, x * 2] for x in range(-6, 7, 2) if x > 0]
# [[2, 1, 4], [4, 2, 8], [6, 3, 12]]

M
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
G = (sum(row) for row in M)                     # Make a generator of row sums
next(G)                                         # Run the iteration protocol (ahead)
# 6
next(G)                                         # A new row sum on each call
# 15
next(G)                                         # Row 3: 7 + 8 + 9
# 24

{sum(row) for row in M}                         # Makes an unordered set of row sums
# {24, 6, 15}
{i: sum(M[i]) for i in range(3)}                # Makes key:value table of row sums
# {0: 6, 1: 15, 2: 24}