from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from root.dal import credentials

connection_string = '{base}://{user}:{pw}@{host}:{port}/{db}'.format(
    base=credentials.BASE,
    user=credentials.USERNAME,
    pw=credentials.PASSWORD,
    host=credentials.HOST,
    port=credentials.PORT,
    db=credentials.DATABASE
)

DBEngine = create_engine(connection_string)
Session = sessionmaker(bind=DBEngine)

ModelBase = declarative_base()
session = Session()
