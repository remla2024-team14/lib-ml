from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np

class TextPreprocessor:
    def __init__(self, config):
        self.tokenizer = Tokenizer(lower=config.get('lower', True),
                                   char_level=config.get('char_level', True),
                                   oov_token=config.get('oov_token', '-n-'))
        self.sequence_length = config.get('sequence_length', 200)

    def fit_text(self, text_list):
        """Fits the tokenizer on the text."""
        self.tokenizer.fit_on_texts(text_list)
        self.char_index = self.tokenizer.word_index
        return self.char_index

    def transform_text(self, text_list):
        """Transforms text to padded sequences."""
        sequences = self.tokenizer.texts_to_sequences(text_list)
        padded_sequences = pad_sequences(sequences, maxlen=self.sequence_length)
        return padded_sequences