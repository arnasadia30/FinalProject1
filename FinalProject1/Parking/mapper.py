#!/usr/bin/python

from operator import itemgetter
import sys
import csv

violations = {}

v = open("violations.csv")
reader = csv.DictReader(v)

for row in reader:
    plate = row["Plate ID"]
    vYear = row["Vehicle Year"]
    vColor = row["Vehicle Color"]
    vtype = row["Vehicle Body Type"]
    violationTime = row["Violation Time"]
    place = row["Violation County"]

    print(plate + "," + vYear + "," + vColor + "," + vType + "," + violationTime + "," + place + "\t" + "1")
v.close()



