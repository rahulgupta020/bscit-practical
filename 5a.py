#Write a Python script to sort (ascending and descending) a dictionary by value

import operator
d= {'python':90, 'cpp':100, 'java':80, 'php':60}
print("Original dictionary = ",d)

asc = dict(sorted(d.items(), key=operator.itemgetter(1)))
print("ascending = ",asc)

dsc = dict(sorted(d.items(), key=operator.itemgetter(1), reverse=True))
print("descending = ",dsc)