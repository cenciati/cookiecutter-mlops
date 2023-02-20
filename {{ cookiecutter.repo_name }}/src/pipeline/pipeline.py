import numpy as np
import pandas as pd
from src.pipeline.stages.interfaces.pipeline_interface import PipelineInterface


class Pipeline:
    """Responsible for the workflow of a given pipeline."""

    def __init__(self, pipeline: PipelineInterface, raw_data: pd.DataFrame) -> None:
        self._pipeline = pipeline
        self._raw_data = raw_data

    def execute(self) -> np.ndarray:
        """Executes the pipeline flow.
        Returns:
            Array containing the predictions made by the model.
        """
        cleaned_data = self._pipeline.clean_data(self._raw_data)
        featured_data = self._pipeline.create_features(cleaned_data)
        preprocessed_data = self._pipeline.preprocess_data(featured_data)
        return self._pipeline.make_predictions(preprocessed_data)
