import tensorflow as tf
import numpy as np
from config import COMMAND_LABELS, CONFIDENCE_THRESHOLD
from utils.logger import log_info, log_warn

def load_brain_model(path):
    log_info(f"[Model] Loading brain signal decoder from {path}")
    model = tf.keras.models.load_model(path)
    log_info("[Model] Model loaded successfully")
    return model

def decode_command(prediction):
    confidence = np.max(prediction)
    if confidence < CONFIDENCE_THRESHOLD:
        log_warn(f"[Model] Low confidence ({confidence:.2f}) — ignoring prediction")
        return None
    idx = np.argmax(prediction)
    command = COMMAND_LABELS[idx]
    log_info(f"[Model] Decoded command '{command}' with confidence {confidence:.2f}")
    return command
