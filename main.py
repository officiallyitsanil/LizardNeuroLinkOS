import threading
import time
from brain_interface.bci_device import BCIInterface
from brain_interface.signal_processing import preprocess_signal
from models.model_utils import load_brain_model, decode_command
from commands.command_executor import execute_command, shutdown_system
from config import BCI_PORT, BCI_BAUDRATE, MODEL_PATH, EEG_SAMPLING_RATE, EEG_SIGNAL_LENGTH
from utils.logger import log_info, log_error

running = True

def brain_listener(dev, model):
    log_info("[Listener] Brain signal listener started.")
    while running:
        try:
            raw_signal = dev.read_signal()
            processed_signal = preprocess_signal(raw_signal)
            prediction = model.predict(processed_signal)
            command = decode_command(prediction)
            if command == "type_text":
                from thought_to_text.transcriber import get_thought_text
                text = get_thought_text()
                execute_command(command, text)
            else:
                execute_command(command)
            time.sleep(0.1)  # Neurofeedback latency control
        except Exception as e:
            log_error(f"[Listener] Error: {e}")

def main():
    global running
    dev = BCIInterface(BCI_PORT, BCI_BAUDRATE, EEG_SAMPLING_RATE, EEG_SIGNAL_LENGTH)
    dev.connect()
    model = load_brain_model(MODEL_PATH)

    listener_thread = threading.Thread(target=brain_listener, args=(dev, model))
    listener_thread.start()

    try:
        while running:
            time.sleep(1)
    except KeyboardInterrupt:
        log_info("[SYSTEM] Interrupt received. Shutting down.")
        running = False

    listener_thread.join()
    shutdown_system()

if __name__ == "__main__":
    main()
