debug = 'true'
daemon = 'false'

bind = 'unix:/tmp/dmr.gunicorn.sock'

# So we don't see the logging associated with the unhandled screen-resize 
# signals.
errorlog = '-'
loglevel = 'warning'

worker_class = 'gevent'
