import configparser

from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker

config = configparser.ConfigParser()
config.read('config.ini')

username = config.get('DB', 'user')
password = config.get('DB', 'password')
db_name = config.get('DB', 'db_name')
host = config.get('DB', 'host')
port = config.get('DB', 'port')

url_to_db = f"postgresql://{username}:{password}@{host}:{port}/{db_name}"

engine = create_engine(url_to_db, echo=True, pool_size=5)
DBSession = sessionmaker(bind=engine)
session = DBSession()