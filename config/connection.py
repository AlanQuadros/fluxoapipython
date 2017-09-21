from sqlalchemy import create_engine
from data import ip, password, port, schema, user

engine = create_engine('mysql://' + user + ':' + password + '@' + ip + ':' + port + '/' + schema, echo=False)