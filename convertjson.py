import csv
import json

with open('network.csv', 'rb') as csvfile:
    filereader = csv.reader(csvfile, delimiter=' ')
    i = 0
    header = []
    out_data = []
    for row in filereader:
        row = [elem for elem in row if elem]
        if i == 0:
            i += 1
            header = row
        else:
            row[0:2] = [row[0]+" "+row[1]]
            _dict = {}
            for elem, header_elem in zip(row, header):
                _dict[header_elem] = elem
            out_data.append(_dict)

print json.dumps(out_data)