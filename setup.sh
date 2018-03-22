#!/bin/bash 
RED='\033[1;31m'
BLUE='\033[1;36m'
NC='\033[0m'

clear
echo -e "${BLUE}" ; cat includes/textpic ; echo -e "${NC}"
sleep 3

check_distro=0
#Checking if the distro is debianbase / archbase / redhatbase/ openSUSEbae and running the correct script
if pacman -Q &> /dev/null; then # Check Arch
    sudo chmod +x ./traktor_arch.sh
    ./traktor_arch.sh # Run Traktor Arch
elif apt list --installed &> /dev/null; then # Check Debian
    sudo chmod +x ./ubuntu.sh
    ./ubuntu.sh # Run Traktor Debian
elif dnf list &> /dev/null; then
    sudo chmod +x ./centos.sh
    ./centos.sh# Run Traktor Fedora
elif zypper search i+ &> /dev/null; then
    sudo chmod +x ./traktor_opensuse.sh
    ./traktor_opensuse.sh # Run Traktor OpenSUSE
else
    echo "Your distro is neither archbase nor debianbase nor redhatbase nor susebase So, The script is not going to work in your distro."
    check_distro="1"
fi
