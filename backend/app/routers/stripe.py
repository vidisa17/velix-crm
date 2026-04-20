from fastapi import APIRouter, Request, Header, HTTPException
import stripe
from app.config import settings
router = APIRouter(prefix="/webhook/stripe", tags=["Stripe"])
stripe.api_key = settings.STRIPE_SECRET_KEY
@router.post("")
async def handle_webhook(request: Request, stripe_signature: str = Header(None)):
    payload = await request.body()
    try: event = stripe.Webhook.construct_event(payload, stripe_signature, settings.STRIPE_WEBHOOK_SECRET)
    except Exception as e: raise HTTPException(400, str(e))
    if event.type == "payment_intent.succeeded": pass
    elif event.type == "setup_intent.succeeded": pass
    elif event.type == "invoice.payment_succeeded": pass
    return {"received": True}
