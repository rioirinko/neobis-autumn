import math
import os
import random
import re
import sys
from collections import Counter
if __name__ == '__main__':
    s = Counter(input()).most_common()
    b = sorted(s, key=lambda x: (-x[1], x[0]))
    for x in range(3):
        print(b[x][0], b[x][1])
    
