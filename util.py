import os, platform, subprocess


hosts = {'local': '192.168.0.5',
        'external': '70.80.147.138'}

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


def navigate(user, ip):
    subprocess.Popen(['C:\\Program Files\\Git\\git-bash.exe'])
    input("\n\n\t-----> \tssh " + user + "@" + ip + "\n\t\tor ssh " + user + " alone if on the local network.")
