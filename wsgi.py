from omb1_api import run_server

# Render environment port hook
import os
port = int(os.environ.get("PORT", 8080))

# Ye line Gunicorn ke liye zaroori hai
app = run_server

if __name__ == "__main__":
    run_server(port=port)
