import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

Base = declarative_base()

class Note(Base):
    __tablename__ = 'notes'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    created_date = Column(DateTime, default=datetime.datetime.utcnow)

    
    def __repr__(self):
        return "<Note(id='{}', name='{}', description='{}')>"\
                .format(self.id, self.name, self.description)
