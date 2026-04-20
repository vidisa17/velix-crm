from fastapi import FastAPI
from app.routers import coverage, stripe, admin
app = FastAPI(title="Velix CRM API")
app.include_router(coverage.router, prefix="/api")
app.include_router(stripe.router)
app.include_router(admin.router, prefix="/api")
@app.get("/health")
async def health(): return {"status": "ok"}
