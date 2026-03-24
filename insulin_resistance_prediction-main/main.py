import os
import sys
from pathlib import Path

# Add the parent directory to Python path for imports
parent_dir = str(Path(__file__).parent)
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

# Import the FastAPI app
from api.final_api import app

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get('PORT', 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
