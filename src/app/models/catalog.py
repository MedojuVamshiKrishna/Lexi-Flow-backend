import uuid
from sqlalchemy import Column, String, Float, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from pgvector.sqlalchemy import Vector
from app.core.database import Base

class CatalogItem(Base):
    __tablename__ = "catalog_items"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    tenant_id = Column(UUID(as_uuid=True), ForeignKey("tenants.id"), nullable=False)
    name = Column(String, nullable=False)
    description = Column(String)
    price = Column(Float)
    embedding = Column(Vector(1536))


class FAQEntry(Base):
    __tablename__ = "faq_entries"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    tenant_id = Column(UUID(as_uuid=True), ForeignKey("tenants.id"), nullable=False)
    question = Column(String, nullable=False)
    answer = Column(String, nullable=False)
    embedding = Column(Vector(1536))