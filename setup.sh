#!/bin/bash 
RED='\033[1;31m'
BLUE='\033[1;36m'
NC='\033[0m'

clear
echo -e "${BLUE}" ; cat includes/textpic ; echo -e "${NC}"
sleep 3


#Checking if the distro is debianbase / archbase / redhatbase/ openSUSEbae and running the correct script
if apt list --installed &> /dev/null; then # Check Debian
    sudo chmod +x ./ubuntu.sh
    ./ubuntu.sh # Run bindbot Debian
elif dnf list &> /dev/null; then
    sudo chmod +x ./centos.sh
    ./centos.sh # Run bindbot Fedora
else
    echo "Your distro is neither debianbase nor redhatbase nor susebase So, The script is not going to work in your distro."
    exit
fi
