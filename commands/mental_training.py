import numpy as np
import tensorflow as tf
from utils.logger import log_info

def mental_command_training(dev, model, epochs=10, samples=100):
    log_info("[TRAINING] Starting mental command training session...")
    signals = []
    for _ in range(samples):
        raw_signal = dev.read_signal()
        from brain_interface.signal_processing import preprocess_signal
        processed_signal = preprocess_signal(raw_signal).flatten()
        signals.append(processed_signal)
    labels = np.zeros(len(signals))  # Label '0' for demonstration
    labels_categorical = tf.keras.utils.to_categorical(labels, num_classes=4)
    model.fit(np.array(signals), labels_categorical, epochs=epochs)
    log_info("[TRAINING] Training complete and model updated.")
