import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler
import pandas as pd

class AICore:
    def __init__(self):
        self.model = None
        self.scaler = MinMaxScaler()
        
    def preprocess_data(self, data):
        """Preprocesses cashflow data for model input."""
        data = pd.DataFrame(data)
        scaled_data = self.scaler.fit_transform(data)
        return scaled_data
        
    def build_model(self):
        """
        Builds a simple LSTM model.
        Returns:
            tf.keras.Model: The compiled model.
        """
        model = tf.keras.Sequential([
            tf.keras.layers.LSTM(64, input_shape=(None, 1)),
            tf.keras.layers.Dense(1)
        ])
        model.compile(loss='mean_squared_error', optimizer='adam')
        return model
        
    def train_model(self, data):
        """Trains the LSTM model on preprocessed cashflow data."""
        X = data[:-1]
        y = data[1:]
        self.model.fit(X, y, epochs=10, batch_size=32)