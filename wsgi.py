from omb1_api import run_production_api

# Render/Vercel execution binding port fallback hook
if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8080))
    run_server(port=port)
