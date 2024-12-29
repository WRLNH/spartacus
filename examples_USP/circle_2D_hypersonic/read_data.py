import numpy as np
import pandas as pd

data = pd.read_csv('./data_usp/grid.usp.30000.dat', skiprows=9, delim_whitespace=True)
data = data.to_numpy()
print(np.max(data[:, 1]))
