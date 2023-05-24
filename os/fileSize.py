import os
from os.path import join, getsize
for root, dirs, files in os.walk('/Users/motes/python/argv/'):
    print(root, "consumes", end=" ")
    print(sum([getsize(join(root,name)) for name in files]), end=" ")
    print("bytes in", len(files), "non-directory files")
print()
print(root)
print(dirs)
print(files)