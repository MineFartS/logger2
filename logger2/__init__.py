from logging import basicConfig
from ._log import VERBOSE, HELP
from functools import partial
import logging as nlog
from sys import argv
from . import _log

def _arg(*name:str) -> int:
    return min(1, len(set(name) & set(argv)))

VERBOSE.set(_arg('-v', '--verbose'))
HELP.set(_arg('-h', '--help'))

class _Formatter(_log.Formatter, nlog.Formatter):
    def __init__(self) -> None:
        _log.Formatter.__init__(self)
        nlog.Formatter.__init__(self)

class _StreamHandler(nlog.StreamHandler):
    def __init__(self) -> None:
        super().__init__()
        self.terminator = ''
        self.setFormatter(_Formatter())
        self.setLevel(10)

setup = partial(basicConfig,
    level = 10,
    handlers = [_StreamHandler()]
)

