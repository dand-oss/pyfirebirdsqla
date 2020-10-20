# pyfirebirdsqla
firebirdsql works just like the "fdb" dbpapi driver for SQLA

Except

pfs takes host rather than host/port

This shim fixes the call to match what sqlalchemy expecpts

and provides a compatability module to insert pyfirebirdsqla into the sqlalchemy engine

in the same manner as postgresqlcffi
