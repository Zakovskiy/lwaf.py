__title__ = "durakonline.py"
__author__ = "Zakovskiy"
__license__ = "MIT"
__copyright__ = "Copyright 2021-2022 Zakovskiy"
__version__ = "3.4.2"

from .lwaf import Client
#from .authorization import Authorization
#from .game import Game
#from .friend import Friend
#from .socket_listener import SocketListener

from .utils import objects
from .utils import md5hash

from requests import get
from json import loads

#__newest__ = loads(get("https://pypi.python.org/pypi/durakonline.py/json").text)["info"]["version"]

#if __version__ != __newest__:
#    exit(f"New version of {__title__} available: {__newest__} (Using {__version__})")
