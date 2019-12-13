BASE = 'postgresql+psycopg2'
USERNAME = 'tzxlafwyaqqlzf'
PASSWORD = '2cd44532fb7672b16eafda82016b90af320812680c97d421e763af28bc15e034'
HOST = 'ec2-54-75-235-28.eu-west-1.compute.amazonaws.com'
PORT = '5432'
DATABASE = 'd7q78cmhi891kf'
DATABASE_URI = '{base}://{user}:{pw}@{host}:{port}/{db}'.format(
base=BASE,
user=USERNAME,
pw=PASSWORD,
host=HOST,
port=PORT,
db=DATABASE
)
