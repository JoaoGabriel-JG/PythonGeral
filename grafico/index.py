import csv
import sys
import matplotlib.pyplot as plt
from datetime import datetime
from sortedcontainers import sortedList, sortedcontainers

dates = ['JAN', 'FEV', 'MAR', 'ABR', 'MAI', 'JUN', 'JUL', 'AGO', 'SET', 'OUT', 'NOV', DEZ]
qntd = sortedList()

with open ('backlogGeral.csv', 'r') as csvfile:
    csv.filed_size_limit(sys.maxsize)
    path = csv.reader(csvfile, delimiter = ',')

    for row in path:
        S = row[3]
        D = row[7]

    if 'Done' or 