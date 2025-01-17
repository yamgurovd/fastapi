# from fastapi import FastAPI
# import uvicorn
#
# import sys
# from pathlib import Path
#
# # from src.database import *
#
# sys.path.append(str(Path(__file__).parent.parent))
# app = FastAPI()
#
# from src.api.hotels import router as router_hotels
# from src.api.auth import router as router_auth
#
# app.include_router(router_auth)
# app.include_router(router_hotels)
#
# if __name__ == "__main__":
#     uvicorn.run("main:app", host="0.0.0.0",  reload=True)


from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import sys
from pathlib import Path

# Adjust the system path to include the parent directory
sys.path.append(str(Path(__file__).parent))

# Create FastAPI instance
app = FastAPI()

# Include routers for different modules
from api.auth import router as router_auth  # Adjusted import path
from api.hotels import router as router_hotels  # Adjusted import path

app.include_router(router_auth)
app.include_router(router_hotels)

# Configure CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Run the application with Uvicorn if this script is executed directly
if __name__ == "__main__":
    uvicorn.run("src.main:app", host="0.0.0.0", port=8000, reload=True)  # Adjusted for module path

# Запуск
# uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload
