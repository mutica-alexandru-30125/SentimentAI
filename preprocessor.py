from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

class Preprocessor:
    def __init__(self, max_words=10000, max_length=50):
        self.tokenizer = Tokenizer(num_words=max_words, oov_token='<OOV>')
        self.max_length = max_length

    def fit(self, texts):
        self.tokenizer.fit_on_texts(texts)

    def transform(self, texts):
        sequences = self.tokenizer.texts_to_sequences(texts)
        return pad_sequences(sequences, maxlen=self.max_length, padding='post')
