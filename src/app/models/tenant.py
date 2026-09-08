import uuid
from sqlalchemy import Column, String, Boolean, JSON
from sqlalchemy.dialects.postgresql import UUID
from app.core.database import Base

class Tenant(Base):
    __tablename__ = "tenants"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    business_name = Column(String, nullable=False)
    whatsapp_number = Column(String)
    instagram_handle = Column(String)
    tone_settings = Column(JSON)
    working_hours = Column(JSON)
    llm_provider = Column(String, default="openai")
    llm_model = Column(String, default="gpt-4o-mini")
    embedding_provider = Column(String, default="openai")
    embedding_model = Column(String, default="text-embedding-3-small")
    is_active = Column(Boolean, default=True)