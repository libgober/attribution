import os
import csv 
with open("robustness.csv","w+") as target:
    header = open("result.3").readline()
    header = [entry.strip() for entry in header[:-1].split(";")]
    t = csv.writer(target,delimiter =";")
    t.writerow(header)
    for fi in os.listdir("."):
        if fi.startswith("result"):
            with open(fi) as f:
                f.readline()
                data = f.readline()
                data = [entry.strip() for entry in data[:-1].split(";")]
                t.writerow(data)