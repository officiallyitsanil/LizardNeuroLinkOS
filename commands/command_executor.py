import time
import threading
from utils.logger import log_info
from thought_to_text.transcriber import get_thought_text
from config import COMMAND_EXECUTION_DELAY

command_lock = threading.Lock()

def execute_command(command, text=None):
    if command is None:
        return
    with command_lock:
        if command == "open_browser":
            log_info("[COMMAND] Executing: Open Browser")
            # Insert OS-specific code here, e.g.:
            # import webbrowser; webbrowser.open('http://google.com')
        elif command == "open_email":
            log_info("[COMMAND] Executing: Open Email Client")
        elif command == "type_text" and text is not None:
            log_info(f"[COMMAND] Executing: Type Text -> {text}")
            # Simulate keyboard input or send text to active window
        elif command == "shutdown":
            log_info("[COMMAND] Executing: Shutdown System")
            shutdown_system()
        else:
            log_info(f"[COMMAND] Unknown or unsupported command: {command}")
        time.sleep(COMMAND_EXECUTION_DELAY)

def shutdown_system():
    global running
    running = False
    log_info("[SYSTEM] Shutting down Lizard NeuroLink OS gracefully...")
