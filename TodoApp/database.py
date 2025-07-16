from sql_alchemy import create_engine
from sql_alchemy.orm import sessionmaker
from sql_alchemy.ext.declarative import declarative_base


SQLALCHEMY_DATABASE_URL='sqlite:///./todos.db'
# estos args son para permiteir que alla varios hilos consumidendo la db
engine= create_engine(SQLALCHEMY_DATABASE_URL,connects_args:{'check_same_thread': False})

# le decimos a la sessionq que queremos usar esa conexion y que queres el ctrol total
sessionLocal=sessionmaker(autocommit=False, auto_flush=False, bind=engine)

Base= declarative_base()