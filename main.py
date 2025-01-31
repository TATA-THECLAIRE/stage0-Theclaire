# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
import pytz

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/")
async def get_info():
    """
    Returns basic information including email, current datetime, and GitHub URL.
    """
    # Get current UTC time in ISO 8601 format
    current_time = datetime.now(pytz.UTC).isoformat()
    
    return {
        "email": "tatatheclaire@gmail.com",  
        "current_datetime": current_time,
        "github_url": "https://github.com/TATA-THECLAIRE/stage0-Theclaire.git"  # repo URL
    }

# For local development
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)