import json
import requests
from .ILanguage import ILanguage
from abc import ABCMeta, abstractmethod


class Node(ILanguage):
    def __init__(self):
        self.__url = "https://api.npms.io/v2/search/suggestions?q="

    @abstractmethod
    def name(self):
        return "NodeJS"

    @abstractmethod
    def packageManager(self):
        return "npm"

    @abstractmethod
    def dependencyFile(self):
        return "package.json"

    def parsePackageFile(self, path):
        packageJson = self.dependencyFile()
        return json.load(open(f'{path}/{packageJson}'))

    @abstractmethod
    def getPackageInfo(self, package):
        request = requests.get(f'{self.__url}{package}')
        return request.json()