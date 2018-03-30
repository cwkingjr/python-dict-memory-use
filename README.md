# Python Dictionary Memory Use

## Purpose

Evaluate the impact of using a dictionary for long-running record storage and deletion. From what I've read, the dictionary (hash table) will not clean up deletions since those slots may be used in links to other hash locations. Currently, I work with a project that uses a dictionary to store and dispose of 50M+ records per day, in a daemon process. This project is to attempt to have a look at the potential impact of this type of dict usage to see what the overall impact of memory use is and to inform whether/not we need to take mitigating actions to prevent ever-growing memory consumption.

## Results

The included txt file shows the results of the dict measurements after each million iterations. Each iteration inserts a random key-value pair, and immediately deletes the kv pair for 9 of 10 insertions. The total memory value is based upon the processes' maximum resident set size (https://docs.python.org/3/library/resource.html), so it continues to grow. The dict size is based specifically upon the byte size of the dictionary at that iteration count, so it grows as Python expands the dict capacity as needed, but shrinks when I explicitly make a deepcopy of the dict to produce a new dict without the deleted entry holes.

The first 50M iterations do not employ the deepcopy and are considerably faster than the second set of iterations that does include the deep copy. See the time taken output lines.

So, my conclusion is that the dictionary does indeed retain memory space for the deleted items, which can be mitigatged by an occasional deepcopy. However, the deepcopy is expensive, so one should use it sparingly for large objects. In our case, it is likely that I will decide to only regenerate the dictionary via deep copy once per day, at a slow processing time (perhaps the middle of the night).

Cheers,

Chuck King
