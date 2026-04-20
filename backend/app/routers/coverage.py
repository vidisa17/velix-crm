from fastapi import APIRouter
from httpx import AsyncClient
from app.config import settings
router = APIRouter(prefix="/coverage", tags=["NETMAP"])
@router.get("/comuni")
async def autocomplete_comuni(q: str, limit: int = 10):
    async with AsyncClient() as client:
        r = await client.get("https://netmap.velixconnect.it/v1/comuni", params={"q": q.upper(), "limit": limit}, headers={"X-API-Key": settings.NETMAP_API_KEY}, timeout=10)
    return r.json()
@router.get("/check")
async def check_coverage(comune: str, strada: str, civico: str, area: str):
    async with AsyncClient() as client:
        r = await client.get("https://netmap.velixconnect.it/v1/coverage", params={"comune": comune.upper(), "strada": strada.upper(), "civico": civico, "area": area.upper()}, headers={"X-API-Key": settings.NETMAP_API_KEY}, timeout=10)
    return r.json()
