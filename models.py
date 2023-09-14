from sqlalchemy import Column, Integer
from database import Base


class Counter(Base):
    __tablename__ = "counter"

    id = Column(Integer, primary_key=True, index=True)
    counter_val = Column(Integer)
