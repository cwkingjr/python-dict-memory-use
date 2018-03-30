#!/usr/local/bin/python3

import copy
import random
import resource
import sys
import time

def get_memory_size():
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

print("Memory use with 9/10 dict deletes")
records = {}
start = time.time()
for i in range(50000000):
    randnum = random.random()
    records[randnum] = randnum
    if i % 10 != 0:
        del records[randnum]
    if i % 1000000 == 0:
        print("Iteration %15s, total memory %15s, sizeof dict %15s, dict len %15s" % (i, get_memory_size(), sys.getsizeof(records), len(records)))
print("time taken was %s seconds" % (time.time() - start))

print("Memory use with 9/10 dict deletes and rebuilding the dict every 5M iterations")
records = {}
start = time.time()
for i in range(50000000):
    randnum = random.random()
    records[randnum] = randnum
    if i % 10 != 0:
        del records[randnum]
    if i % 5000000 == 0:
        records = copy.deepcopy(records)
    if i % 1000000 == 0:
        print("Iteration %15s, total memory %15s, sizeof dict %15s, dict len %15s" % (i, get_memory_size(), sys.getsizeof(records), len(records)))
print("time taken was %s seconds" % (time.time() - start))
