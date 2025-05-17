# Configuration constants

BCI_PORT = "/dev/ttyUSB0"
BCI_BAUDRATE = 115200

MODEL_PATH = "models/brain_signal_decoder.h5"

COMMAND_LABELS = [
    "open_browser",
    "open_email",
    "type_text",
    "shutdown"
]

EEG_SAMPLING_RATE = 256       
EEG_SIGNAL_LENGTH = 256      
PREPROCESS_SIGNAL_LENGTH = 128 

CONFIDENCE_THRESHOLD = 0.75   

COMMAND_EXECUTION_DELAY = 0.5  
