import time
import urllib.request

import mss
import mss.tools

# ===================== settings — adjust if needed =====================
SERVER_URL = "http://127.0.0.1:5000/upload"   # where the server is listening
INTERVAL_SECONDS = 30                          # how often to send a screenshot
# =======================================================================


def capture_loop():
    with mss.mss() as sct:
        while True:                     # runs until you close this window (Ctrl+C)
            try:
                shot = sct.grab(sct.monitors[0])              # the whole screen
                png = mss.tools.to_png(shot.rgb, shot.size)
                urllib.request.urlopen(SERVER_URL, data=png)  # send to the server
                print("sent a screenshot")
            except Exception as e:
                # server not up yet, or busy: just try again next time
                print(f"could not send ({e}); will retry")
            time.sleep(INTERVAL_SECONDS)


def run():
    print(f"Sending a screenshot to {SERVER_URL} every {INTERVAL_SECONDS} seconds.")
    print("Press Ctrl+C to stop.")
    try:
        capture_loop()
    except KeyboardInterrupt:
        print("\nStopped.")
if __name__ == "__main__":
    run()
