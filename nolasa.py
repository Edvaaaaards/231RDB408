import csv
reg_name = None
with open("people.csv","r") as f:
    next(f)
    for line in f:
        row=line.rstrip().split(",")
        if row[1]==reg_name:
            region.append(int(row[3]))