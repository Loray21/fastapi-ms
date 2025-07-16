from database import Base
from sql_alchemy import Columns,Integer,String,Boolean

class Todos(Base):
    __tablename__="todos"
    id= Columns(Integer, primary_key=True,index=True)
    title= Columns(String)
    description= Columns(String)
    priority=Columns(Integer)
    complete=Columns(Boolean,default=False)

