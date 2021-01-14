from firebirdsql import *


class ConnectionShim(Connection):
    def __init__(self, host="", **kargs):
        if '/' in host:
            host = host[0:host.find('/')]
        super().__init__(host=host, **kargs)


def connect(**kwargs):
    conn = ConnectionShim(**kwargs)
    return conn


def create_database(**kwargs):
    kwargs['create_new'] = True
    return connect(**kwargs)