import numpy as np
import re

data = np.loadtxt('./data_usp/grid.usp.30000.dat', delimiter=re.compile(r'\s'), skiprows=9)
print(data)
