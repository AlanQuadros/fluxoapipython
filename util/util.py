import json
from sqlalchemy.ext.declarative import DeclarativeMeta
from datetime import date, datetime

def new_alchemy_encoder():
    _visited_objs = []
    class AlchemyEncoder(json.JSONEncoder):
        def default(self, obj):                 
            if isinstance(obj.__class__, DeclarativeMeta):
                # don't re-visit self
                if obj in _visited_objs:
                    return None
                _visited_objs.append(obj)

                # an SQLAlchemy class
                fields = {}
                for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:                   
                    if isinstance(obj.__getattribute__(field), (date, datetime)):
                        fields[field] = str(obj.__getattribute__(field))
                    else:                        
                        fields[field] = obj.__getattribute__(field)                     
                # a json-encodable dict
                return fields

            return json.JSONEncoder.default(self, obj)
    return AlchemyEncoder