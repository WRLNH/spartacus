import numpy as np
import pandas as pd

data = pd.read_csv('./examples_USP/circle_2D_hypersonic/data_usp/grid.usp.31000.dat', sep='\s+', skiprows=9)
data = data.to_numpy()

filtered_data = []

for row in data:
    if (row[3 : 10].any() != 0):
        filtered_data.append(row)

filtered_data = np.array(filtered_data)
print(filtered_data)

np.savetxt('./examples_USP/circle_2D_hypersonic/data_usp/filtered_data.csv', filtered_data, delimiter=',')