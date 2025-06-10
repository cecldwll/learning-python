# Other Object Types

'''
Start up a REPL to test these out
'''

# Sets
X = set('hack')                                         # Sequence => set
Y = {'a', 'p', 'p'}                                     # Set literal
X, Y
# ({'c', 'k', 'a', 'h'}, {'p', 'a'})
X & Y, X | Y                                            # Intersection, union
# ({'a'}, {'p', 'c', 'k', 'h', 'a'})
X - Y, X > Y                                            # Difference, superset
# ({'c', 'k', 'h'}, False)

list(set([3, 1, 2, 1, 3, 1]))                           # Duplicates removal
# [1, 2, 3]
set('code') - set('hack')                               # Collection difference
# {'d', 'o', 'e'}
set('code') == set('deoc')                              # Order-neutral equality
# True


# Booleans and None
1 > 2, 1 < 2                                            # Booleans
# (False, True)
bool('hack')                                            # All objects have a Boolean value
# True                                                  # Nonempty means true
X = None                                                # None placeholder
print(X)                                                # But None is a thing
# None
L = [None] * 100                                        # Initialize a list of 100 Nones
L
# [None, None, None, None, None, None, None, None, None, ...etc: a list of 100 Nones...]


# Types
L = [1, 2, 3]
type(L)                                                 # The type of a list object
# <class 'list'>
type(type(L))                                           # Even types are objects!
# <class 'type'>

type(L) == type([])                                     # Type testing, if you must...
# True                                                  # Using a real object
type(L) == list                                         # Using a type name
# True
isinstance(L, list)                                     # The object-oriented way
# True


# Type Hinting
x: int = 1                                              # Optional hint: x might be an integer
x = 'anything'                                          # But it doesn't have to be!


# User-Defined Objects
'''
class Worker:
    # ..............

sue = Worker ('Sue Jones', 60000)                       # Make two new objects
bob = Worker ('Bob Smith', 50000)                       # Each has a name and pay
sue.lastName()                                          # Call a method to process sue
# 'Jones'
bob.lastName()                                          # call a method to process bob
# 'Smith'
sue.giveRaise(.10)                                      # Update sue's pay
sue.pay                                                 # Display sue's pay
# 66000.0
'''