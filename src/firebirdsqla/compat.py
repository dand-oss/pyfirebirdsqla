"""
patches pyfirebirdsql for sqalalchemy

"""
import sys
import firebirdsqla

# function used to parse dsn
_f_parse_dsn = None


def sqla_parse_dsn(dsn, host=None, port=None, database=None, user=None, password=None):
    global _f_parse_dsn

    if not _f_parse_dsn:
        raise "Must register first"

    # check the driver version
    least_vers = "1.1.3"
    import firebirdsql as fbm

    fb_vers = fbm.__version__
    if fb_vers <= least_vers:
        raise f"Require firebirdsql driver > {least_vers}"

    # two lines to fix SQLA
    if "/" in host:
        host = host[0 : host.find("/")]

    # run the "original"
    return _f_parse_dsn(dsn, host, port, database, user, password)


def register():
    # WE are the fdb driver!
    sys.modules["fdb"] = firebirdsqla

    # monkey patch DSN parsing to work with SQLA
    # upstream refused the fix...
    from firebirdsql import utils

    global _f_parse_dsn

    # out with the old
    _f_parse_dsn = utils.parse_dsn

    # in with the new
    utils.parse_dsn = sqla_parse_dsn
