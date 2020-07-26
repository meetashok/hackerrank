# https://www.hackerrank.com/challenges/repeated-string

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    count2 = 0
    length = len(s)
    dividend = n // length
    remainder = n % length

    count1 = s.count("a")
    if remainder < length:
        count2 = s[:remainder].count("a")

    # print(dividend, count1, count2)
    return count1*dividend + count2

if __name__ == '__main__':
    s = "abcac"
    n = 10

    print(repeatedString(s, n))

    s = "ceebbcb"
    n = 817723
    print(repeatedString(s, n))