import os
import sys
from pathlib import Path

# Add the parent directory to Python path for imports
parent_dir = str(Path(__file__).parent.parent)
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

# Import the FastAPI app from final_api
from api.final_api import app

# Vercel serverless function handler
handler = app

# For local testing
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
