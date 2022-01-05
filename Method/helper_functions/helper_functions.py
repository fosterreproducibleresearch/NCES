import numpy as np, pandas as pd
from scipy.stats import wilcoxon


def wilcoxon_statistical_test(data1, data2):
    stat, p = wilcoxon(data1, data2)
    print('stat=%.3f, p=%.3f' % (stat, p))
    if p > 0.05:
        print('Probably the same distribution')
    else:
        print('Probably different distributions')
    return stat, p
        

