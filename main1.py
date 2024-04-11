import platform
import os
import subprocess
import colorama
from colorama import Fore, Style

def sysinfo():
    print('System:   ', platform.system())
    print('Kernel version:  ', platform.version())
    print('Release:  ', platform.release())
    print('Platform: ', platform.platform())

    kernel = platform.version()

    print('PATH Variables: ')
    print(os.environ['PATH'])


def userinfo():
    print("Current user:  ", os.getlogin())
    print("Current ID:    ", os.getuid())

    print("SUID Permissions")
    subprocess.call(["find", "/", "-perm", "-u=s", "-type", "f", "2>/dev/null"])

    print("can we run using sudo without password")
    subprocess.call(["sudo", "-l"])


def service_info():
    subprocess.call(["bash", "tuan1.sh"])


def potential_exp_files():
    colorama.init()

    print('\n', 'Critic Finding!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! ')

    subprocess.call(["cat", "~/.ssh/authorized_keys", "2>/dev/null"])
    subprocess.call(["cat", "~/.ssh/identity.pub", "2>/dev/null"])
    subprocess.call(["cat", "~/.ssh/identity", "2>/dev/null"])
    subprocess.call(["cat", "~/.ssh/id_rsa.pub", "2>/dev/null"])
    subprocess.call(["cat", "~/.ssh/id_rsa", "2>/dev/null"])
    subprocess.call(["cat", "~/.ssh/id_dsa.pub", "2>/dev/null"])
    subprocess.call(["cat", "~/.ssh/id_dsa", "2>/dev/null"])
    subprocess.call(["cat", "/etc/ssh/ssh_config", "2>/dev/null"])
    subprocess.call(["cat", "/etc/ssh/sshd_config", "2>/dev/null"])
    subprocess.call(["cat", "/etc/ssh/ssh_host_dsa_key.pub", "2>/dev/null"])
    subprocess.call(["cat", "/etc/ssh/ssh_host_dsa_key", "2>/dev/null"])
    subprocess.call(["cat", "/etc/ssh/ssh_host_rsa_key.pub", "2>/dev/null"])
    subprocess.call(["cat", "/etc/ssh/ssh_host_rsa_key", "2>/dev/null"])
    subprocess.call(["cat", "/etc/ssh/ssh_host_key.pub", "2>/dev/null"])
    subprocess.call(["cat", "/etc/ssh/ssh_host_key", "2>/dev/null"])

    print(Style.RESET_ALL)

    subprocess.call(["bash", "testwr.sh", "/etc/passwd"])

    print('\n', '------------------------- Is /ect/shadow  File Readable  --------------------------')

    subprocess.call(["bash", "testre.sh", "/etc/shadow"])


def networkInfo():
    print("==> Hostname")
    subprocess.call(["cat", "/etc/hostname"])
    print("")
    print("==> Hosts")
    subprocess.call(["cat", "/etc/hosts"])
    print("")


def softwareInfo():
    print("=============== Database Info ===============")
    os.system("mysqlver=`mysql --version 2>/dev/null ")
    print("")
    print("=============== Kernel ===============")
    # os.system("bash kernel2.sh")
    subprocess.call(["bash", "kernel2.sh"])


if __name__ == "__main__":
    sysinfo()
    userinfo()
    service_info()
    potential_exp_files()
    softwareInfo()
    networkInfo()
