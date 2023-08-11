# pylint: disable=invalid-name, import-error
import random
import warnings
from typing import Any, Optional, Tuple

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from scipy.stats import chi2_contingency

from src.__logs__.logging import logger


def set_jupyter_settings(
    max_columns: Optional[int] = None,
    max_rows: Optional[int] = 50,
    figsize: Optional[Tuple[int, int]] = (18, 9),
    fontsize: Optional[int] = 12,
    filterwarnings: Optional[bool] = False,
) -> None:
    """Sets jupyter notebook settings.
    Args:
        max_columns (int): Defines the maximum number of columns
            that will be showed in pandas objects.
        max_rows (int): Defines the maximum number of rows
            that will be showed in pandas objects.
        figsize (tuple): Defines default size of all figures.
        fontsize (int): Defines default size of all labels.
        filterwarnings (bool): Defines whether warnings will be displayed.
    """

    def set_seeds(seed: Optional[int] = 0) -> None:
        """Reproducibility (randomness) configurations."""
        np.random.seed(seed)
        random.seed(seed)

    def set_pandas_settings(
        max_columns: Optional[int] = None, max_rows: Optional[int] = 50
    ) -> None:
        """Pandas configurations."""
        pd.set_option('display.max_columns', max_columns)
        pd.set_option('display.max_rows', max_rows)

    def set_plots_settings(
        figsize: Optional[Tuple[int, int]] = (18, 9),
        fontsize: Optional[int] = 12,
    ) -> None:
        """Matplotlib configurations."""
        plt.rc('figure', figsize=figsize)
        plt.rc('font', size=fontsize)

    set_seeds()
    set_pandas_settings(max_columns=max_columns, max_rows=max_rows)
    set_plots_settings(figsize=figsize, fontsize=fontsize)
    if filterwarnings:
        warnings.filterwarnings('ignore')
    logger.info('Jupyter has been successfully configured.')


def cramers_v(X: Any, y: Any) -> float:
    """Calculates the Cramer's V correlation between two variables.
    Args:
        X (any): First variable.
        y (any): Second variable.
    Returns:
        Float value indicating the Cramer's V correlation between X and y.
    """
    # Calculate contingency table
    confusion_matrix: np.ndarray = pd.crosstab(X, y).to_numpy()
    sum_of_observations: int = confusion_matrix.sum()
    n_rows, n_columns = confusion_matrix.shape
    chi2 = chi2_contingency(confusion_matrix)[0]

    # Correct bias
    chi2_correlation: float = max(
        0, chi2 - (n_columns - 1) * (n_rows - 1) / (sum_of_observations - 1)
    )
    columns_correlation = n_columns - (n_columns - 1) ** 2 / (n_columns - 1)
    rows_correlation = n_rows - (n_rows - 1) ** 2 / (n_rows - 1)

    # Compute correlation
    cramer_v: float = np.sqrt(
        (chi2_correlation / sum_of_observations)
        / (min(columns_correlation - 1, rows_correlation - 1))
    )
    return cramer_v
