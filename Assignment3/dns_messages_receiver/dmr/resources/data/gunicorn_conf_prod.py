user = 'www-data'
group = 'www-data'

debug = 'false'
daemon = 'true'

bind = 'unix:/tmp/dmr.gunicorn.sock'

errorlog = '-'
loglevel = 'warning'
worker_class = 'gevent'
