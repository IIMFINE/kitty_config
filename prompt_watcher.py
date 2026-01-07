import subprocess
import time

# Cooldown state
_last_notify_time = 0
_COOLDOWN_SECONDS = 5

def on_receive(boss, window, data):
    """Called when terminal receives output"""
    global _last_notify_time

    text = data.decode('utf-8', errors='ignore')

    if "Do you want to proceed?" in text:
        current_time = time.time()
        if current_time - _last_notify_time > _COOLDOWN_SECONDS:
            subprocess.Popen([
                'notify-send', '-u', 'normal',
                'Terminal Prompt',
                'Detected: Do you want to proceed?',
                '-i', 'dialog-question'
            ])
            _last_notify_time = current_time
