import uuid as uuid
from sqlalchemy import String, Column

from db import Base


class Example(Base):
    __tablename__ = 'example'

    uuid = Column(String(length=36), primary_key=True, default=lambda: str(uuid.uuid4()))
    text = Column(String(100))
