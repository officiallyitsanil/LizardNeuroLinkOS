import numpy as np
from utils.logger import log_info, log_warn

class BCIInterface:
    def __init__(self, port, baudrate, sampling_rate, signal_length):
        self.port = port
        self.baudrate = baudrate
        self.sampling_rate = sampling_rate
        self.signal_length = signal_length
        self.connected = False

    def connect(self):
        log_info(f"[BCI] Connecting to device at {self.port} @ {self.baudrate} baudrate")
        # Insert real connection code here
        self.connected = True
        log_info("[BCI] Device connected.")

    def read_signal(self):
        if not self.connected:
            raise Exception("Device not connected")
        # Simulate EEG raw data with noise/artifacts
        raw_signal = np.sin(np.linspace(0, 2 * np.pi, self.signal_length))  # base sine wave
        noise = np.random.normal(0, 0.5, self.signal_length)
        artifact = np.zeros(self.signal_length)
        artifact[np.random.randint(0, self.signal_length)] = 5  # simulate spike artifact
        signal = raw_signal + noise + artifact
        log_info("[BCI] Raw EEG signal read")
        return signal
