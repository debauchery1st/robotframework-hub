import pkg_resources
from .version import __version__

try:
    from .kwdb import *
except:
    import kwdb
# this will be defined once the app starts
KWDB = None
