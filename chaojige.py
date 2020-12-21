import numpy as np
from scipy import stats

list_p = []
for count in range(1, 31):
    p = stats.binom.pmf(np.arange(count, 30, 1), 30, 0.133)
    list_p.append(p.sum())

count = 1
for p in list_p:
    print(str(count) + '   :   ' + str(p * 100) + '%')
    print(' ')
    count = count + 1