from abc import ABC, abstractmethod
from typing import Any


class PipelineInterface(ABC):
    """Interface for creating new ML/Data pipelines."""

    @abstractmethod
    def clean_data(self, raw_data: Any) -> Any:
        """Cleans a given dataset."""
        raise NotImplementedError

    @abstractmethod
    def create_features(self, cleaned_data: Any) -> Any:
        """Performs feature engineering."""
        raise NotImplementedError

    @abstractmethod
    def preprocess_data(self, featured_data: Any) -> Any:
        """Prepares the data for ML training."""
        raise NotImplementedError

    @abstractmethod
    def make_predictions(self, preprocessed_data: Any) -> Any:
        """Predicts values given a dataset."""
        raise NotImplementedError
