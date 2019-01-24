#!/usr/bin/python3

from os import getcwd
from sys import argv
from src.domain.lang.Node import Node
from src.domain.lang.ILanguage import ILanguage
from src.utils.Logger import Logger
from src.msg.translate import msg

PROJECT_PATH = getcwd()
if argv[1] != None:
    PROJECT_PATH = argv[1]

try:
    import requests
except:
    msg('DEPENDENCY-ERROR')

node = Node()
print(node.parsePackageFile(PROJECT_PATH)['dependencies'])
print(node.getPackageInfo("ramda"))
