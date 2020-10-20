# pyfirebirdsqla
firebirdsql works just like the "fdb" dbpapi driver for SQLA

Except

pyfirebirdsql takes host rather than host/port

This shim fixes the call to match what sqlalchemy expecpts

and provides a compatability module to insert pyfirebirdsqla into the sqlalchemy engine

in the same manner as postgresqlcffi

## how to use

add this code before sql alchemy query
```python
from firebirdsqla import compat
compat.register()
```
compat.register will register [pyfirebirdsql](https://github.com/nakagami/pyfirebirdsql) as fdb
and this package have shim to support sql-alchemy hostname style
so, no need to change  sql-alchemy
