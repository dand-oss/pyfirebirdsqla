"""Connection Shim."""
import typing

import firebirdsql as fb
from firebirdsql import *  # fails with this!!! code run at import time?


class ConnectionShim(fb.Connection):
    """Shim firebird connection."""

    def __init__(self, host: str = "", **kargs: str):
        """Override initialize instance."""
        if "/" in host:
            host = host[0 : host.find("/")]
        super().__init__(host=host, **kargs)


def connect(**kwargs: str) -> ConnectionShim:
    """Override db connect."""
    conn = ConnectionShim(**kwargs)
    return conn


def create_database(**kwargs: typing.Any) -> ConnectionShim:
    """Call from sqlalchemy."""
    kwargs["create_new"] = True
    return connect(**kwargs)
