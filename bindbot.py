#!/usr/bin/env python3
import os

## Functions
def installDebian():
    # Install packages
    os.system("sudo apt install bind9 -y > /dev/null")
    # Creat bind9 install verify file
    os.system("sudo touch /usr/share/bindbot/.bind9")
    # Save service name
    os.system("sudo echo 'bind9' | sudo tee -a /usr/share/bindbot/.service > /dev/null")
    # Save config path
    os.system("sudo echo '/etc/bind/' | sudo tee -a /usr/share/bindbot/.etc > /dev/null")
    # Open ports
    os.system("sudo ufw allow 53/tcp > /dev/null")
    os.system("sudo ufw allow 53/udp > /dev/null")
    os.system("sudo iptables --append INPUT --match tcp --protocol tcp --sport 53 --jump ACCEPT > /dev/null")
    os.system("sudo iptables --append OUTPUT --match tcp --protocol tcp --sport 53 --jump ACCEPT > /dev/null")
    os.system("sudo iptables --append INPUT --match udp --protocol udp --sport 53 --jump ACCEPT > /dev/null")
    os.system("sudo iptables --append OUTPUT --match udp --protocol udp --sport 53 --jump ACCEPT > /dev/null")
    # Enable service
    os.system("sudo systemctl enable bind9 > /dev/null")

def installBind9():
    debian = os.path.exists("/bin/apt")
    redhat = os.path.exists("/bin/yum")
    if debian:
        ## Install Debian
        installDebian()
    elif redhat:
        ## Install Redhat
        pass
    else:
        print("BindBot dosn't support your distribution.")
        os._exit(0)

## Start
print("BindBot 2.0 Beta")

# Check bind9 installed
installed = os.path.exists("/usr/share/bindbot/.bind9")
if (installed == False):
    print("Installing bind9...")
    ##install bind9
    installBind9()
