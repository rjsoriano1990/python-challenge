import os

filepath = os.path.join('downloads','budget_data.csv')

import csv

with open(filepath, 'r') as f:

    budget_df = csv.reader(f, delimiter=',')

    for row in budget_df:
        print(row)


