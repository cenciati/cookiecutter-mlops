'''
Set of useful functions.

Author: Gabriel O. Cenciati
LinkedIn: https://www.linkedin.com/in/cenciati/
GitHub: https://github.com/cenciati/
'''

# data manipulation
from typing import Optional
import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency

# data visualization
from matplotlib import pyplot as plt

# other
import warnings


def jupyter_settings(figsize: Optional[tuple]=(18, 9),
                     fontsize: Optional[int]=12,
                     filterwarnings: Optional[bool]=False) -> None:
    '''Sets jupyter notebook settings.
    
    Params
    ------
    figsize : tuple, default=(24, 12)
        Default size of all figures.
    fontsize : int, default=12
        Default size of all labels.
    filterwarnings : boolean, default=False
        Defines whether labraries warnings will be displayed.
    
    Returns
    -------
    None
    '''
    # pandas settings
    pd.options.display.max_columns = None
    pd.options.display.max_rows = 20
    pd.options.display.float_format = '{:.4f}'.format
    
    # numpy settings
    np.random.seed(0)
    np.set_printoptions(precision=4)
    
    # matplotlib settings
    plt.rc('figure', figsize=figsize)
    plt.rc('font', size=fontsize)
    
    # warnings settings
    if filterwarnings:
        warnings.filterwarnings('ignore')
    
    # success message
    print('Jupyter settings set.')
    
    return None


def cramers_v(x: pd.Series, y: pd.Series) -> float:
    '''Calculates the Cramer's V correlation between two variables.

    Params
    ------
    x : pandas series
    y : pandas series
            
    Returns
    -------
    Cramer's V correlation between x and y.
    '''
    # create confusion matrix
    cm = pd.crosstab(x, y).to_numpy()
    
    # calculate chi-squared
    n = cm.sum()
    r, k = cm.shape
    chi2 = chi2_contingency(cm)[0]
    
    # correct bias
    chi2corr = max(0, chi2 - (k-1)*(r-1) / (n-1))
    kcorr = k - (k-1)**2 / (n-1)
    rcorr = r - (r-1)**2 / (n-1)
    
    return np.sqrt((chi2corr / n) / (min(kcorr-1, rcorr-1)))
