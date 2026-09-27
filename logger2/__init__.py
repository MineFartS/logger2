from logging import basicConfig
from functools import partial
import logging as nlog
from sys import argv
from . import _log

def _arg(*name:str):
    return _log.MutState(len(set(name) & set(argv)))

HELP = _arg('-h', '--help')
VERBOSE = _arg('-v', '--verbose')

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

