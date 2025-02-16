from datetime import datetime, timezone
from sqlalchemy.orm import mapped_column, Mapped
import uuid

from src.settings.database import BaseModel


class UserModel(BaseModel):
  __tablename__ = 'Users'

  id: Mapped[str] = mapped_column(primary_key=True, default=lambda: uuid.uuid4() )
  name: Mapped[str] = mapped_column(unique=True,nullable=False)

  # def __init__(self,id):
  #   self.id =
  #   # crear hash de la password antes de guardarlo
