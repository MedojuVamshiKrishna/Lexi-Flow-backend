import uuid
from datetime import datetime
from sqlalchemy import Column, String, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID
from app.core.database import Base

class Conversation(Base):
    __tablename__ = "conversations"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    tenant_id = Column(UUID(as_uuid=True), ForeignKey("tenants.id"), nullable=False)
    customer_id = Column(String, nullable=False)   # phone number / IG user id
    channel = Column(String, nullable=False)       # "whatsapp" or "instagram"
    status = Column(String, default="open")        # open / needs_review / closed
    created_at = Column(DateTime, default=datetime.utcnow)