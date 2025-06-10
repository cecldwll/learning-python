# Strings

'''
Start up a REPL to test these out
'''

# Sequence Operations
S = 'Code'                  # Make a 4-character string, and assign it to a name
len(S)                      # Length: number of characters
# 4
S[0]                        # The first item in S, indexing by zero-based position
# 'C'
S[1]                        # The second item from the left
# 'o'

S[-1]                       # The last item from the end in S
# 'e'
S[-2]                       # The second-to-last item from the end
# 'd'
S[len(S) - 1]               # Negative indexing, the hard way
# 'e'

S
# 'Code'
S[1:3]                      # Slice of S from offsets 1 through 2 (not 3)
# 'od'

S[1:]                       # Everything past tge first (1:len(S))
# 'ode'
S[0:3]                      # Everything but the last
# 'Cod'
S[:3]                       # Same as S[0:3]
# 'Cod'
S[:-1]                      # Everything but the last again, but simpler (0:-1)
# 'Cod'
S[:]                        # All of S as a top-level copy (0:len(S))
# 'Code'

S + 'xyz'                   # Concatenation
# 'Codexyz'
S                           # S is unchanged
# 'Code'
S * 8                       # Repitition
# 'CodeCodeCodeCodeCodeCodeCodeCode'


# Immutability
# Immutable = Unchangeable
S
# 'Code'
S[0] = 'z'                 # Immutable objects cannot be changed
# ...error text omitted...
# TypeError: 'str' object does not support item assignment
S = 'Z' + S[1:]            # But we can run  expressions to make new objects
S
# 'Zode'

S = 'Python'             
L = list(S)                 # Expand to a list: [...]
L
# ['P', 'y', 't', 'h', 'o', 'n']
L[0] = 'C'                  # Change it in place
''.join(L)                  # Join with empty delimiter
# 'Cython'

B = bytearray(b'app')       # A bytes/list hybrid (ahead)
B.extend(b'lication')       # 'b' means bytes string
B                           # B[i] = ord(X) works here too
# bytearray(b'application')
B.decode()                  # Translate to normal string
# 'application'


# Type-Specific Methods
S = 'Code'
S.find('od')                # Find the offset of a substring in S'
# 1
S
'Code'
S.replace('od', 'abl')      # Replace all substrings 'od' in S with 'abl'
# 'Cable'
S
#'Code'

line = 'aaa,bbb,ccccc,dd'
line.split(',')             # Split on a delimiter into a list of substrings
# ['aaa', 'bbb', 'ccccc', 'dd']
S = 'code'
S.upper()                   # Upper- and lowercase conversions
# 'CODE'
S.isalpha()                 # Content tests: isalpha, isdigit, etc.
# True
line = 'aaa,bbb,ccccc,dd\n'
line.rstrip()               # Remove whitespace characters on the right side
# 'aaa,bbb,ccccc,dd'
line.rstrip().split(',')    # Combine two operations, run left to right
# ['aaa', 'bbb', 'ccccc', 'dd']

tool = 'Python'
major = 3
minor = 3
'Using %s version %s.%s' % (tool, major, minor + 9)         # Format expression
# 'Using Python version 3.12'
'Using {} version {}.{}'.format(tool, major, minor + 9)     # Format method
# 'Using Python version 3.12'
f'Using {tool} version {major}.{minor + 9}'                 # Format literal
# 'Using Python version 3.12'

'%.2f | %+05d' % (3.14159, -62)                         # Digits, signs, padding
# ' 3.14 | -0062'
'{1:,.2f} | {0}'.format('snapp'[1:], 296999.256)        # Commas, decimal digits
# '296,999.26 | app'
f'{296999.256:,.2f} | {'snapp'[1:]}'                    # Ditto, with nested quotes
# '296,999.26 | app'


# Getting Help
S = 'Code'
dir(S)
# ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', ...etc... 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

S + 'head!'
# 'Codehead!'
S .__add__('head!')
# 'Codehead!'

help(S.replace)                 # Or help(str.replace)
# Help on built-in funtion replace:
# replace(old, new, count=-1, /) method of builtins.str instance
# Return a copy with all occurrences of substring old replaced b new. ...etc...


# Other Ways to Code Strings
S = 'A\nB\tC'                   # Escapes: \n is newline, \t is tab
len(S)                          # Each stands for just one character
# 5
S = 'A\0B\0C'                   # \0, a binary zero byte, does not terminate string
len(S)
# 5
S                               # Nonprintables are displayed as \xNN hex escapes
# 'A\x00B\x00C'

msg = """
aaaaaaaaaaaa
bbb'''bbb""bbb
cccccccc
"""
msg
# '\naaaaaaaaaaaa\nbbb\'\'\'bbb""bbb\nccccccc\n'


# Unicode Strings
'hÄck'                          # Normal str strings are Unicode text
# 'hÄck'
b'a\x01c'                       # bytes strings are byte-based data
# b'a\x01c'

'Code'                          # Characters may be any size in memory
# 'Code'
'Code'.encode('utf-8')          # Encoded to 4 bytes in UTF-8 in files
# b'Code'
'Code'.encode('utf-16')         # But encoded to 10 byutes in UTF-16
#b'\xff\xfeC\x00o\x00d\x00e\x00'

hex(ord('🐍'))                       # Code point two big for a byte
# '0x1f40d'
len('🐍hÄck👏')                     # One character (code print) each
# 6
len('🐍hÄck👏'.encode('utf-8'))     # But encoded btyes sizes vary
# 13
len('🐍hÄck👏'.encode('utf-16'))
# 18