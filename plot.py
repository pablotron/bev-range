#!/usr/bin/python3

# generate chart.svg for data

import csv
import sys
import numpy as np
import matplotlib.pyplot as plt

def read_csv(path):
  with open(sys.argv[1], newline = '') as fh:
    return list(reversed(list([row for row in csv.DictReader(fh)])))

# check arguments
if len(sys.argv) < 3:
  print("Usage: {} input.csv output.svg".format(sys.argv[0]))
  exit(-1)

# read csv
rows = read_csv(sys.argv[1])

# sort by range
# rows.sort(key = lambda row: int(row['range']))

# plot values
plt.barh(
  np.arange(len(rows)),
  [int(row['Range']) for row in rows], 
  align = 'center',
  alpha = 0.5,
  tick_label = ['{} {}'.format(row['Make'], row['Model']) for row in rows]
)

# add label and title
plt.yticks(fontsize = 5)
plt.xlabel('Range (miles)')
plt.title('Battery Electric Vehicle Ranges (2019)', fontsize = 9)
plt.tight_layout()

# save image
plt.savefig(sys.argv[2])
