from app.models import BaseModel
from sqlalchemy import Column, Integer, VARCHAR, BOOLEAN

class RoleModel(BaseModel):
    __tablename__ = 'roles'

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(VARCHAR(8))
    status = Column(BOOLEAN, default=True)