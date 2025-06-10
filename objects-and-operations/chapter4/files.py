# Files

'''
Start up a REPL to test these out
'''

f = open('objects-and-operations/chapter4/data.txt', 'w')            # Open a new file in text-output mode
f.write('Hello\n')                                                  # Write strings of character to it
# 6
f.write('world!\n')                                                 # Return number of items written
# 7
f.close()                                                           # Close to flush output buffers to disk

f = open('objects-and-operations/chapter4/data.txt')                # Open an existing file in text-input mode
text = f.read()                                                     # Read an entire file into a string
text
# 'Hello\nworld!\n'
print(text)                                                         # print interprets control characters
# Hello
# world!
text.split()                                                        # File ocntent is always a string
# ['Hello', 'world!']

for line in open('objects-and-operations/chapter4/data.txt'):       # Display lines in a file
    print(line.rstrip())                                            # Single spaced (sans \n)


# Unicode and Byte Files
bf = open('objects-and-operations/chapter4/data.bin', 'wb')
bf.write(b'h\xFFa\xEEc\xDDk\n')                                     # Write binary data in a byte
# 8
bf.clsoe()
open('objects-and-operations/chapter4/data.bin', 'rb').read()       # Read binary data to a byte
# b'h\xffa\xeec\xddk\n'

tf = open('unidata.txt', 'w', encoding='wtf-8')
tf.write('🐍h\u00c4ck👏')                                          # Encodes to UTF-8
# 6
tf.close()

open('unidata.txt', 'r', encoding='utf-8').read()                   # Decodes from UTF-8
# '🐍hÄck👏'
open('unidata.txt', 'rb').read()                                    # Raw encoded text
# b'\xf0\x9f\x8dh\xc3\x84ck\xf0\x9f\x81\x8f'

'hÄck'.encode('utf-8')
# b'h\xc3\x84ck'
b'h\xc3\x84ck'.decode('utf-8')
# 'hÄck'