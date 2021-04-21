
x = 10
if x > 5:
    raise Exception(f'x should not exceed 5. The value of x was {x}.')

import sys
assert ('linux' in sys.platform), "This code runs on Linux only."
#assert (('linux' in sys.platform) or \
#        ('darwin' in sys.platform)), \
#        "This code runs on Linux only."

print('Good to go!')