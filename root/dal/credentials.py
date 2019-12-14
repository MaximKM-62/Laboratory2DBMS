BASE = 'postgresql+psycopg2'
USERNAME = 'skyxhlgvrzpahp'
PASSWORD = '95018380db23f699f252b6e329944e40efdd9c5636da4955802887af62932249'
HOST = 'ec2-54-75-235-28.eu-west-1.compute.amazonaws.com'
PORT = '5432'
DATABASE = 'delgjbilp6jvhv'
DATABASE_URI = '{base}://{user}:{pw}@{host}:{port}/{db}'.format(
base=BASE,
user=USERNAME,
pw=PASSWORD,
host=HOST,
port=PORT,
db=DATABASE
)


