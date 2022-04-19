"""Patches pyfirebirdsql for sqlalchemy."""
import sys
import typing

import firebirdsqla

# function used to parse dsn
g_f_parse_dsn: typing.Callable = None


def sqla_parse_dsn(
    dsn: str,
    host: str = None,
    port: str = None,
    database: str = None,
    user: str = None,
    password: str = None,
) -> str:
    """Parse DSN for sqlalchemy."""
    if not g_f_parse_dsn:
        raise RuntimeError("Must register first")

    # check the driver version
    least_vers = "1.1.3"
    import firebirdsql as fbm

    fb_vers = fbm.__version__
    if fb_vers <= least_vers:
        raise RuntimeError(f"Require firebirdsql driver > {least_vers}")

    # two lines to fix SQLA
    if "/" in host:
        host = host[0 : host.find("/")]

    # run the "original"
    return g_f_parse_dsn(dsn, host, port, database, user, password)


def register() -> None:
    """Register this driver as fdb."""
    # WE are the fdb driver!
    sys.modules["fdb"] = firebirdsqla

    # monkey patch DSN parsing to work with SQLA
    # upstream refused the fix...
    from firebirdsql import utils

    # out with the old
    global g_f_parse_dsn
    g_f_parse_dsn = utils.parse_dsn

    # in with the new
    utils.parse_dsn = sqla_parse_dsn
