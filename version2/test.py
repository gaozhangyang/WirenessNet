import numpy as np
import pandas as pd
from numba import jit
from node import compare3,initAB
import time
import json
import argparse


if __name__ == '__main__':
    A, B = initAB(2,2,3,3)
    result = compare3(A, B)
    print(result)