# Dictionaries

'''
Start up a REPL to test these out
'''

# Mapping Operations
D = {'name': 'Pat', 'job': 'dev', 'age': 40}

D['name']                                           # Fetch value of key 'name'
# 'Pat'
D['job'] = 'mgr'                                    # Change Pat's job description
D
# {'name': 'Pat', 'job': 'mgr', 'age': 40}

D = {}
D['name'] = 'Pat'                                   # Create keys by assignment
D['job'] = 'dev'
D['age'] = 40
D
# {'name': 'Pat', 'job': 'dev', 'age': 40}

pat1 = dict(name='Pat', job='dev', age=40)                         # Keywords
pat1
# {'name': 'Pat', 'job': 'dev', 'age': 40}
pat2 = dict(zip(['name', 'job', 'age'], ['Pat', 'dev', 40]))        # Zipping
pat2
# {'name': 'Pat', 'job': 'dev', 'age': 40}


# Nesting Revisited
rec = {'name': {'first': 'Pat', 'last': 'Smith'},
       'jobs': ['dev', 'mgr'],
       'age': 40.5}

rec['name']                                         # 'name' is a nested dictionary
# {'first': 'Pat', 'last': 'Smith'}
rec['name']['last']                                 # Index the nested dictionary
# 'Smith'
rec['jobs']                                         # 'jobs' is a nested list
# ['dev', 'mgr']
rec['jobs'][-1]                                     # Index the nested list
# 'mgr'
rec['jobs'].append('janitor')                       # Expand Pat's job description in place
rec
# {'name': {'first': 'Pat', 'last': 'Smith'}, 'jobs': ['dev', 'mgr', 'janitor'], 'age': 40.5}

rec = 0                                             # Now the prior object's space is reclaimed


# Missing Keys: if Tests
D = {'a': 1, 'b': 2, 'c': 3}
D['d'] = 4                                          # Assigning new keys grows dictionaries
D
# {'a': 1, 'b': 2, 'c': 3, 'd': 4}
D['e']                                              # Referencing a nonexistent key is an error
# KeyError: 'e'

'e' in D                                            # Boolean result: True or False
# False
if not 'e' in D:                                    # Python's main selection statement
    print('missing key!')
# missing key!

if not 'e' in D:
    print('missing')                                # Statement blocks are indented
    print('no, really...')
# missing
# no, really...

D.get('a', 'missing')                               # Like D['a'] but with a default
# 1
D.get('e', 'missing')                               # Default returned if absent
# 'missing'
D['e'] if 'e' in D else 0                           # if/else ternary expression form
# 0


# Item Iterations: for Loops
D = dict(a=1, b=2, c=3)
D
# {'a': 1, 'b': 2, 'c': 3}
list(D.keys())                                      # Keys, values, and key/value pairs
# ['a', 'b', 'c']
list(D.values())                                    # list forces results generation
# [1, 2, 3]
list(D.items())
# [('a', 1), ('b': 2), ('c': 3)]

D.keys()                                            # Get an iterable object
# dict_keys(['a', 'b', 'c'])
I = iter(D.keys())                                  # Get an iterator from an iterable
next(I)                                             # Get one result at a time from iterator
# 'a'
next(I)                                             # This is most of the iteration protocol
# 'b'

for key in D.keys():                                # Auto run the iteration protocol
    print(key, '=>', D[key])                        # Display multiple items, space between
# a => 1
# b => 2
# c => 3

for key in D:                                       # Implicit keys() iteration
    print(key, '=>', D[key])

for (key, value), in D.items():                     # Key/value-pair tuples iteration
    print(key, '=>', value)