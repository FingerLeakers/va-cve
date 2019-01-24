from colorama import init, Fore, Back, Style
init(autoreset=True)


def errorStr(msg):
    return f"{Fore.RED}{Style.BRIGHT}{msg}{Fore.RESET}{Style.RESET_ALL}"


class Logger():
    def __init__(self):
        Logger.__init__(self)

    @staticmethod
    def Print(msg):
        print(Fore.RESET + msg)

    @staticmethod
    def Warn(msg):
        print(Fore.YELLOW + msg)

    @staticmethod
    def Error(msg):
        return errorStr(msg)

    @staticmethod
    def ErrorTitle(title, msg):
        colorTitle = errorStr('['+title.upper()+']')
        print(f"{colorTitle} {msg}")