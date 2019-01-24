from abc import ABCMeta, abstractmethod


class ILanguage:
    __metaclass__ = ABCMeta

    @abstractmethod
    def name(self): raise NotImplementedError

    @abstractmethod
    def packageManager(self): raise NotImplementedError

    @abstractmethod
    def dependencyFile(self): raise NotImplementedError

    @abstractmethod
    def parsePackageFile(self, path): raise NotImplementedError

    @abstractmethod
    def getPackageInfo(self, package): raise NotImplementedError
