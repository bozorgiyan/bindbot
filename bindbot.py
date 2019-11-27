#!/usr/bin/env python
import os
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
## Functions
def installDebian():
    # Install packages
    os.system("apt install bind9 -y > /dev/null 2>&1")
    # Creat bindbot dir
    os.system("mkdir /usr/share/bindbot")
    # Creat bind9 install verify file
    os.system("touch /usr/share/bindbot/.bind9")
    # Save service name
    os.system("echo 'bind9' | sudo tee -a /usr/share/bindbot/.service > /dev/null 2>&1")
    # Save config path
    os.system("echo '/etc/bind/' | sudo tee -a /usr/share/bindbot/.etc > /dev/null 2>&1")
    # Creat bindbot at config path
    os.system("mkdir /etc/bind/bindbot")
    # Open ports
    print(bcolors.BOLD + "Opening ports..." + bcolors.ENDC)
    os.system("ufw allow 53/tcp > /dev/null 2>&1")
    os.system("ufw allow 53/udp > /dev/null 2>&1")
    os.system("iptables --append INPUT --match tcp --protocol tcp --sport 53 --jump ACCEPT > /dev/null 2>&1")
    os.system("iptables --append OUTPUT --match tcp --protocol tcp --sport 53 --jump ACCEPT > /dev/null 2>&1")
    os.system("iptables --append INPUT --match udp --protocol udp --sport 53 --jump ACCEPT > /dev/null 2>&1")
    os.system("iptables --append OUTPUT --match udp --protocol udp --sport 53 --jump ACCEPT > /dev/null 2>&1")
    # Enable service
    print(bcolors.BOLD + "Enable bind9 service..." + bcolors.ENDC)
    os.system("systemctl enable bind9 > /dev/null 2>&1")

    print(bcolors.OKGREEN + "Bind9 installation finished." + bcolors.ENDC)
def installRedhat():
        # Install packages
        os.system("yum install bind bind-utils -y > /dev/null 2>&1")
        # Creat bindbot dir
        os.system("mkdir /usr/share/bindbot")
        # Creat bind9 install verify file
        os.system("touch /usr/share/bindbot/.bind9")
        # Save service name
        os.system("echo 'named' | sudo tee -a /usr/share/bindbot/.service > /dev/null 2>&1")
        # Save config path
        os.system("echo '/var/named/' | sudo tee -a /usr/share/bindbot/.etc > /dev/null 2>&1")
        # Open ports
        print(bcolors.BOLD + "Opening ports..." + bcolors.ENDC)
        os.system("firewall-cmd --zone=public --add-port=53/tcp --permanent > /dev/null 2>&1")
        os.system("firewall-cmd --zone=public --add-port=53/tcp --permanent > /dev/null 2>&1")
        os.system("firewall-cmd --reload > /dev/null 2>&1")
        # Enable service
        print(bcolors.BOLD + "Enable named service..." + bcolors.ENDC)
        os.system("systemctl enable named > /dev/null 2>&1")

        print(bcolors.OKGREEN + "Bind9 installation finished." + bcolors.ENDC)
def installBind9():
    debian = os.path.exists("/bin/apt")
    redhat = os.path.exists("/bin/yum")
    if debian:
        ## Install Debian
        installDebian()
    elif redhat:
        ## Install Redhat
        installRedhat()
    else:
        print("BindBot dosn't support your distribution.")
        os._exit(0)

# Add zone Functions
def addZone():
    configdir = open('/usr/share/bindbot/.etc', 'r').read()
    service = open('/usr/share/bindbot/.service', 'r').read()
    domain = raw_input("Enter domain name whitout WWW(ex: Site.com): ")
    ip = raw_input("Enter an IP to this domain: ")
    v = raw_input("'"+domain+"' points to '"+ip+"' is correct(y or n): ")
    if (v != "y" and v != "Y"):
        print(bcolors.FAIL+"Process canceled by user."+bcolors.ENDC)
        os._exit(0)


def mainMenu():
    print("1.Add zone")
    print("2.Delete zone")
    print("3.Exit")
    input = raw_input("Enter number: ")
    if input == "1":
        os.system("clear")
        addZone()
    elif input == "2":
        pass
    else:
        os._exit(0)
## Start
# Check root
user = os.getenv("SUDO_USER")
if user is None:
    print(bcolors.FAIL + "This program need sudo."+ bcolors.ENDC)
    exit()
os.system("clear")
print(bcolors.HEADER + "BindBot 2.0 Beta" + bcolors.ENDC)
# Check bind9 installed
installed = os.path.exists("/usr/share/bindbot/.bind9")
if (installed == False):
    print(bcolors.BOLD + "Installing bind9..." + bcolors.ENDC)
    ##install bind9
    installBind9()
mainMenu()
