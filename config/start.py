from os import environ

host = '127.0.0.1'

bind = host + ':' + environ.get('PORT', '8000')
