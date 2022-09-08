import warnings
from typing import Optional

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from scipy.stats import chi2_contingency


def jupyter_settings(
    figsize: Optional[tuple] = (18, 9),
    fontsize: Optional[int] = 12,
    filterwarnings: Optional[bool] = False,
) -> None:
    """sets jupyter notebook settings.

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

    return None


def cramers_v(x: pd.Series, y: pd.Series) -> float:
    """calculates the cramer's v correlation between two variables.

    :param x: first variable.
    :param y: second varaible.
    :returns cramer's v correlation between x and y.
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
