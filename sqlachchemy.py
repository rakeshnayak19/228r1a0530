from sqlalchemy import create_engine, String, Integer, Column
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
Base=declarative_base()
class students(Base):
    __tablename__="CSE-A"
    Id=Column(Integer,primary_key=True)
    name=Column(String)
    rollno=Column(String)
    Section=Column(String)
engine=create_engine("sqlite:///mydb.db")
Base.metadata.create_all(engine)
session=sessionmaker(bind=True)
s=session()
data=students(name="virat",rollno=18)
data1=students(name="Dhoni",rollno=60)
s.add(data)
s.add(data1)
s.commit()