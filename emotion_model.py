import tensorflow as tf
import numpy as np

class EmotionModel:
    def __init__(self, num_classes, max_length):
        self.model = tf.keras.Sequential([
            tf.keras.layers.Embedding(10000, 64, input_length=max_length),
            tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(64, return_sequences=True)),
            tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(32)),
            tf.keras.layers.Dense(64, activation='relu'),
            tf.keras.layers.Dense(num_classes, activation='softmax')
        ])
        self.model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    def train(self, train_data, train_labels, val_data, val_labels, epochs=10, batch_size=32):
        self.model.fit(
            train_data,
            np.array(train_labels),
            epochs=epochs,
            validation_data=(val_data, np.array(val_labels)),
            batch_size=batch_size
        )

    def evaluate(self, test_data, test_labels):
        loss, accuracy = self.model.evaluate(test_data, np.array(test_labels))
        print(f"Loss: {loss}, Accuracy: {accuracy}")

    def predict(self, text, preprocessor, label_encoder):
        sequence = preprocessor.transform([text])
        prediction = self.model.predict(sequence)
        predicted_label = label_encoder.inverse_transform([np.argmax(prediction)])
        return predicted_label[0]
