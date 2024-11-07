# train_keras.py
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np

# Data dummy untuk pelatihan
X_train = np.random.rand(100, 4)
y_train = np.random.randint(0, 3, 100)

# Definisikan model Keras
model = Sequential([
    Dense(10, input_shape=(4,), activation="relu"),
    Dense(3, activation="softmax")
])

# Kompilasi dan pelatihan
model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
model.fit(X_train, y_train, epochs=10)

# Simpan model ke file .h5
model.save("keras_model.h5")
print("Model Keras disimpan sebagai keras_model.h5")
