import numpy as np
import pandas as pd

data = pd.read_csv('./examples_USP/circle_2D_hypersonic/data_dsmc/grid.dsmc.31000.dat', sep='\s+', skiprows=8)
data = data.to_numpy()

filtered_data = []

for row in data:
    if (row[3 : 10].any() != 0):
        filtered_data.append(row)

filtered_data = np.array(filtered_data)
filtered_data = np.delete(filtered_data, -1, axis=1)
filtered_data = np.delete(filtered_data, -1, axis=1)
filtered_data = np.delete(filtered_data, 2, axis=1)
filtered_data = np.delete(filtered_data, -3, axis=1)

np.savetxt('./examples_USP/circle_2D_hypersonic/data_dsmc/filtered_data.csv', filtered_data, delimiter=',')