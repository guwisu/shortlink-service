from fastapi import APIRouter

from app.schemas.shorten import UrlInput

router = APIRouter(prefix="/shorten", tags=["Shorten"])


@router.post("")
def shorten(url_input: UrlInput):
    return {"short_url": "https://test/url"}