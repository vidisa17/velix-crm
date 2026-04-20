from sqlalchemy import Column, String, Float, DateTime, Enum, Text, ForeignKey
from sqlalchemy.dialects.postgresql import UUID, INET
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
import enum, uuid
Base = declarative_base()
class OrderStatus(str, enum.Enum):
    DRAFT = "draft"
    ACTIVATION_PAID = "activation_paid"
    READY_FOR_RADIUS = "ready_for_radius"
    RADIUS_PROVISIONED = "radius_provisioned"
    ACTIVATED_ONSITE = "activated_onsite"
    ACTIVE = "active"
class Order(Base):
    __tablename__ = "orders"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    plan_code = Column(String(32), nullable=False)
    activation_price = Column(Float, nullable=False)
    monthly_price = Column(Float, nullable=False)
    status = Column(Enum(OrderStatus), default=OrderStatus.DRAFT)
    stripe_customer_id = Column(String(128))
    stripe_pi_id = Column(String(128))
    stripe_pm_recurring_id = Column(String(128))
    recurring_method = Column(String(32))
    stripe_sub_id = Column(String(128))
    radius_username = Column(String(128))
    radius_profile = Column(String(64))
    assigned_ip = Column(INET)
    activated_onsite_at = Column(DateTime(timezone=True))
    first_billing_status = Column(String(32), default="pending")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
