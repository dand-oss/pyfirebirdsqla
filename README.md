# pyfirebirdsqla

## how to use

add this code before using sqlalchemy
```python
from firebirdsqla import compat
compat.register()
```
compat.register will register [pyfirebirdsql](https://github.com/nakagami/pyfirebirdsql) as "fdb" driver

## Why

[pyfirebirdsql](https://github.com/nakagami/pyfirebirdsql) works just like the "fdb" dbpapi driver for SQLA

Except..

[pyfirebirdsql](https://github.com/nakagami/pyfirebirdsql) takes "host" rather than "host/port"

This shim
   - fixes the call to match what sqlalchemy expects
    - provides a compatability module to insert pyfirebirdsqla into the sqlalchemy engine

in the same manner as [psycopg2cffi](https://github.com/chtd/psycopg2cffi)
