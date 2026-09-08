import uuid
from datetime import datetime
from sqlalchemy import Column, String, Text, Boolean, Float, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID
from app.core.database import Base

class Message(Base):
    __tablename__ = "messages"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    conversation_id = Column(UUID(as_uuid=True), ForeignKey("conversations.id"), nullable=False)
    sender = Column(String, nullable=False)        # "customer" / "bot" / "human"
    content = Column(Text, nullable=False)
    topic = Column(String)                         # filled in later by intent classifier
    urgency = Column(String)                        # filled in later by intent classifier
    confidence_score = Column(Float)
    needs_review = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)