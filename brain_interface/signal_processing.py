import numpy as np
from scipy.signal import butter, lfilter
from utils.logger import log_info, log_warn

def butter_bandpass(lowcut, highcut, fs, order=4):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a

def bandpass_filter(data, lowcut=0.5, highcut=40.0, fs=256, order=4):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    log_info("[Signal] Bandpass filter applied")
    return y

def remove_artifacts(signal):
    # Simple threshold-based artifact removal
    artifact_threshold = 3.0
    cleaned_signal = np.where(np.abs(signal) > artifact_threshold, 0, signal)
    log_info("[Signal] Artifact removal performed")
    return cleaned_signal

def preprocess_signal(signal):
    filtered = bandpass_filter(signal)
    cleaned = remove_artifacts(filtered)
    normalized = (cleaned - np.mean(cleaned)) / np.std(cleaned)
    processed = normalized[:128]
    if len(processed) < 128:
        processed = np.pad(processed, (0, 128 - len(processed)))
    log_info("[Signal] Signal preprocessed and ready for model")
    return processed.reshape(1, 128)
