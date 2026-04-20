from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db import get_db
router = APIRouter(prefix="/admin/orders", tags=["Admin"])
@router.post("/{order_id}/radius")
async def save_radius_data(order_id: str, username: str, profile: str, ip: str = None, db: AsyncSession = Depends(get_db)):
    return {"status": "ok", "msg": "Dati Radius salvati. Ordine pronto per attivazione on-site."}
@router.post("/{order_id}/activate-onsite")
async def activate_onsite(order_id: str, db: AsyncSession = Depends(get_db)):
    return {"status": "activated_onsite", "msg": "Addebito ricorrente programmato. In attesa conferma Stripe."}
