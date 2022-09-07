"""
Set of useful functions.

Author: Gabriel O. Cenciati
LinkedIn: https://www.linkedin.com/in/cenciati/
GitHub: https://github.com/cenciati/
"""

# other
import warnings

# data manipulation
from typing import Optional

import numpy as np
import pandas as pd

# data visualization
from matplotlib import pyplot as plt
from scipy.stats import chi2_contingency


def jupyter_settings(
    figsize: Optional[tuple] = (18, 9),
    fontsize: Optional[int] = 12,
    filterwarnings: Optional[bool] = False,
) -> None:
    """Sets jupyter notebook settings.

    :param figsize: default size of all figures.
    :param fontsize: default size of all labels.
    :param filterwarnings: defines whether warnings will be displayed.
    :return: none.
    """
    # pandas settings
    pd.options.display.max_columns = None
    pd.options.display.max_rows = None

    # numpy settings
    np.random.seed(0)

    # matplotlib settings
    plt.rc("figure", figsize=figsize)
    plt.rc("font", size=fontsize)

    # warnings settings
    if filterwarnings:
        warnings.filterwarnings("ignore")

    # success message
    print("Jupyter settings set.")

    return None


def cramers_v(x: pd.Series, y: pd.Series) -> float:
    """Calculates the Cramer's V correlation between two variables.

    Params
    ------
    x : pandas series
    y : pandas series

    Returns
    -------
    Cramer's V correlation between x and y.
    """
    # create confusion matrix
    cm = pd.crosstab(x, y).to_numpy()

    # calculate chi-squared
    n = cm.sum()
    r, k = cm.shape
    chi2 = chi2_contingency(cm)[0]

    # correct bias
    chi2corr = max(0, chi2 - (k - 1) * (r - 1) / (n - 1))
    kcorr = k - (k - 1) ** 2 / (n - 1)
    rcorr = r - (r - 1) ** 2 / (n - 1)

    return np.sqrt((chi2corr / n) / (min(kcorr - 1, rcorr - 1)))
