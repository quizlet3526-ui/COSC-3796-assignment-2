# Import modules
import os
from datetime import datetime
import ngrok
from dotenv import load_dotenv
from flask import Flask, render_template_string, request, send_from_directory


# ===================== ngrok settings — read from .env =====================
# Load the .env file that sits next to server.py (works no matter where you run it from)
load_dotenv(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env"))

NGROK_AUTHTOKEN = os.getenv("NGROK_AUTHTOKEN", "")
NGROK_DOMAIN = os.getenv("NGROK_DOMAIN", "")
# ===========================================================================

app = Flask(__name__)

# The screenshots folder sits next to server.py
SCREENSHOTS = os.path.join(app.root_path, "screenshots")
os.makedirs(SCREENSHOTS, exist_ok=True)


def connect_ngrok():
    # No token set? Just run locally instead of crashing.
    if not NGROK_AUTHTOKEN:
        print("No NGROK_AUTHTOKEN set in .env - running locally only: http://127.0.0.1:5000")
        return

    options = {"authtoken": NGROK_AUTHTOKEN}
    if NGROK_DOMAIN:                      # use the reserved domain only if one was given
        options["domain"] = NGROK_DOMAIN

    forwarder = ngrok.forward("localhost:5000", **options)
    print(f"Available at: {forwarder.url()}")


# Show the web page. ?n=0 is the newest screenshot, ?n=1 the one before it, and so on.
@app.route("/")
def home():
    shots = sorted(os.listdir(SCREENSHOTS), reverse=True)  # newest first
    n = int(request.args.get("n", 0))
    n = max(0, min(n, len(shots) - 1))                     # keep n inside the list

    with open(os.path.join(app.root_path, "index.html")) as f:
        page = f.read()
    return render_template_string(page, shots=shots, n=n)


# Send one screenshot file to the browser
@app.route("/screenshots/<name>")
def screenshot(name):
    return send_from_directory(SCREENSHOTS, name)


# Receive a screenshot from the game and save it with the time as its name
@app.route("/upload", methods=["POST"])
def upload():
    name = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".png"
    with open(os.path.join(SCREENSHOTS, name), "wb") as f:
        f.write(request.get_data())
    return "OK"


if __name__ == "__main__":
    connect_ngrok()       # open the public tunnel first (if a token is set)
    app.run(port=5000)    # then start serving
