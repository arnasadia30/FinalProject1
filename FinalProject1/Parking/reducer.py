#!/usr/bin/python
from operator import itemgetter
import sys
import re
import errno

for line in sys.stdin:
    line = line.strip()
    line = line.split()
    num = line[1]
    num = int(num)

violations[plate] = violations.get(plate, 0) + num
violations[vYear] = violations.get(vYear, 0) + num
violations[vColor] = violations.get(vColor, 0) + num
violations[vtype] = violations.get(vtype, 0) + num
violations[violationTime] = violations.get(violationTime, 0) + num
violations[place] = violations.get(place, 0) + num

# question 1
sorted_time = sorted(violations[violationTime].items(), key=itemgetter(1), reverse=True)

for violationTime, freq in sorted_time[0:20]:
    print(violationTime, freq)

# question 2

sorted_years = sorted(violations[vYear].items(), key=itemgetter(1), reverse=True)
sorted_types = sorted(violations[vType].items(), key=itemgetter(1), reverse=True)

for vYear, freq in sorted_years[0:20]:
    print(vYear, freq)

for vType, freq in sorted_types[0:20]:
    print(vType, freq)


# question 3

sorted_place = sorted(violations[place].items(), key=itemgetter(1), reverse=True)

for place, freq in sorted_place[0:20]:
    print(place, freq)

# question 4

sorted_color = sorted(violations[vColor].items(), key=itemgetter(1), reverse=True)

for vColor, freq in sorted_color[0:20]:
    print(vColor, freq)

