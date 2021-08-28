#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    def is_even(n):
        if n % 2 == 0:
            return True
        return False

    if not is_even(n):
        print("Weird")

    if is_even(n) and n in range(2, 6):
        print("Not Weird")

    if is_even(n) and n in range(6, 21):
        print("Weird")

    if is_even(n) and n > 20:
        print("Not Weird")