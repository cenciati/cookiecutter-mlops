from abc import ABC, abstractmethod


class Sanitizer(ABC):
    '''Provides resources to sanitize incoming data.'''

    def __init__(self):
        ...

    @abstractmethod
    def remove_special_characters(self):
        '''Removes special characters from text.'''
        raise NotImplementedError

    @abstractmethod
    def normalize_text(self):
        '''Normalizes text to a standard format.'''
        raise NotImplementedError

    @abstractmethod
    def ensure_dataframe_consistency(self):
        '''Ensures that the dataframe is consistent with the schema.'''
        raise NotImplementedError
