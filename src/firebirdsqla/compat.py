import sys
import firebirdsqla


def register():
    sys.modules['fdb'] = firebirdsqla
