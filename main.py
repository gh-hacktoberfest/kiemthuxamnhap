import platform
import os
import grp, pwd
import getpass
import subprocess
import colorama
from colorama import Fore, Style

def sysinfo():
	
	
	print('System:   ',platform.system())
	print('Kernel version:  ',platform.version())
	print('Release:  ',platform.release())
	print('Platform: ',platform.platform())
	
	kernel=platform.version()
		
	
	print('PATH Variables: ',os.system("echo $PATH"))	
	
	
def userinfo():
	
	print("Current user:  ", os.system("whoami"))
	print("Current ID:    ",subprocess.run(["id"]))
	

	print("SUID Permissions",os.system("find / -perm -u=s -type f 2>/dev/null"))
	
	print("can we run using sudo without password",os.system("sudo -l"))	


	
	
	
	
	
	
def service_info():
	os.system("bash tuan1.sh")
    	
	

def potential_exp_files():
	
	colorama.init()
	
	
	print('\n', 'Critic Finding!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! ')
	
	print(os.system("cat ~/.ssh/authorized_keys 2>/dev/null"),os.system("cat ~/.ssh/identity.pub 2>/dev/null"),os.system("cat ~/.ssh/identity 2>/dev/null"),os.system("cat ~/.ssh/id_rsa.pub 2>/dev/null"),
	os.system("cat ~/.ssh/id_rsa 2>/dev/null"),os.system("cat ~/.ssh/id_dsa.pub 2>/dev/null"),os.system("cat ~/.ssh/id_dsa 2>/dev/null"),os.system("cat /etc/ssh/ssh_config 2>/dev/null"),
	os.system("cat /etc/ssh/sshd_config 2>/dev/null"),os.system("cat /etc/ssh/ssh_host_dsa_key.pub 2>/dev/null"),os.system("cat /etc/ssh/ssh_host_dsa_key 2>/dev/null"),os.system("cat /etc/ssh/ssh_host_rsa_key.pub 2>/dev/null"),os.system("cat /etc/ssh/ssh_host_rsa_key 2>/dev/null"),
	os.system("cat /etc/ssh/ssh_host_key.pub 2>/dev/null"),os.system("cat /etc/ssh/ssh_host_key 2>/dev/null"))
	
	
	print(Style.RESET_ALL)
	
	
	os.system("bash testwr.sh /etc/passwd")

		
	print('\n','------------------------- Is /ect/shadow  File Readable  --------------------------') 

	os.system("bash testre.sh /etc/shadow")
	
	

	

def networkInfo():
    
    print("==> Hostname")
    os.system("cat /etc/hostname")
    print("")
    print("==> Hosts")
    os.system("cat /etc/hosts ")
    print("")
    

def softwareInfo():
    
    print("=============== Database Info ===============")
    os.system("mysqlver=`mysql --version 2>/dev/null ")
    print("")
    print("=============== Kernel ===============")
    #os.system("bash kernel2.sh")
    os.system("bash kernel2.sh")
		
	
	
if __name__=="__main__":
	
	sysinfo()
	userinfo()
	service_info()
	potential_exp_files()
	softwareInfo()
	networkInfo()
