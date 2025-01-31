from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
from typing import Dict

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

@app.get("/", response_model=Dict[str, str])
def get_info():
    """Returns user information with ISO 8601 formatted UTC timestamp."""
    return {
        "email": "tatatheclaire@gmail.com",  
        "current_datetime": datetime.utcnow().isoformat() + "Z",  
        "github_url": "https://github.com/TATA-THECLAIRE/stage0-Theclaire.git"  
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, workers=1)