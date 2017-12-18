import os, platform, subprocess


def main_menu():
    clear_console()
    print('                                           \n   _|_|_|  _|_|_|_|  _|_|_|_|_|  _|_|_|    \n _|        _|            _|      _|    _|  \n   _|_|    _|_|_|        _|      _|_|_|    \n       _|  _|            _|      _|        \n _|_|_|    _|            _|      _|        ')
    print('\n\n\n\t[1] Upload file')
    print('\t[2] Download file')
    print('\t[3] Navigate')

def clear_console():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def navigate():
    subprocess.call(['C:\\Program Files\\Git\\git-bash.exe'])
