import os, platform, subprocess


hosts = {'home_server_local': '192.168.0.5',
        'home_server_external': '70.80.147.138'}

def print_title():
    print('                                           \n   _|_|_|  _|_|_|_|  _|_|_|_|_|  _|_|_|    \n _|        _|            _|      _|    _|  \n   _|_|    _|_|_|        _|      _|_|_|    \n       _|  _|            _|      _|        \n _|_|_|    _|            _|      _|        ')

def clear_console():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def navigate(user, ip):
    subprocess.Popen(['C:\\Program Files\\Git\\git-bash.exe'])
    input("\n\n\t-----> \tssh " + user + "@" + ip + "\n\t\tor ssh " + user + " alone if on the local network.")
