"""
Connection Shim
"""
from firebirdsql import Connection
from typing import TypeVar

conn_T = TypeVar("T", bound="ConnectionShim")


class ConnectionShim(Connection):
    def __init__(self, host: str = "", **kargs):
        if "/" in host:
            host = host[0 : host.find("/")]
        super().__init__(host=host, **kargs)


def connect(**kwargs) -> conn_T:
    conn = ConnectionShim(**kwargs)
    return conn


def create_database(**kwargs) -> conn_T:
    kwargs["create_new"] = True
    return connect(**kwargs)
