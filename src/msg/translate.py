import colorama
from locale import getdefaultlocale
from .en import en
from .ptbr import ptbr
from ..utils.Logger import Logger

langs = {
    "ptbr": ptbr,
    "en":en
}


def msg(code, status="info", lang="en"):
    Logger.Warn(langs[lang][code])
