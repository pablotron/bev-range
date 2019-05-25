#!/usr/bin/python3

import csv
import sys
import numpy as np
import matplotlib.pyplot as plt

# check arguments
if len(sys.argv) < 3:
  print("Usage: {} input.csv output.svg".format(sys.argv[0]))
  exit(-1)

# read csv
rows = []
with open(sys.argv[1], newline = '') as fh:
  rows = [row for row in csv.DictReader(fh)]

# sort by range
# rows.sort(key = lambda row: int(row['range']))

# plot values
plt.barh(
  np.arange(len(rows)),
  [int(row['range']) for row in rows], 
  align = 'center',
  alpha = 0.5,
  tick_label = ['{} {} ({})'.format(row['make'], row['model'], row['year']) for row in rows]
)

# add label and title
plt.xlabel('Range (miles)')
plt.title('Battery Electric Vehicle Ranges (2019)', fontsize = 9)

# save image
plt.savefig(sys.argv[2])
