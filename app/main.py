import sys
import uvicorn

from pathlib import Path
from fastapi import FastAPI

sys.path.append(str(Path(__file__).parent.parent))

from app.api.redirect import router as redirect_router  # noqa: E402
from app.api.shorten import router as shorten_router  # noqa: E402

app = FastAPI()

app.include_router(redirect_router)
app.include_router(shorten_router)

if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)
