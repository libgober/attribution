import os
import csv 
with open("consolidated.csv","w+") as target:
    header = open("result.3").readline()
    header = header[1:-2].replace("'","").split(",")
    t = csv.writer(target,delimiter =";")
    t.writerow(header)
    for fi in os.listdir("."):
        if fi.startswith("result"):
            with open(fi) as f:
                f.readline()
                data = f.readline()
                data = data[1:-2]
                data = data.split(",")
                data = data[0:10] + [data[10] + "," + data[11]] + data[12:]
                t.writerow(data)