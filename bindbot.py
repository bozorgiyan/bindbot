#!/usr/bin/env python3
import os

## Functions
def installBind9():
    debian = os.path.exists("/bin/apt")
    redhat = os.path.exists("/bin/yum")
    if debian:
        ## Install Debian
        pass
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
