#!/bin/bash 
RED='\033[1;31m'
BLUE='\033[1;36m'
NC='\033[0m'

clear
echo -e "${BLUE}" ; cat includes/textpic ; echo -e "${NC}"

echo "1.Ubuntu"
echo "2.CentOS"
echo "3.Others"
read -p "Enter Your OS number from list: " useros
if [ "$useros" = "1" ]
then
chmod +x ubuntu.sh
./ubuntu.sh
elif [ "$useros" = "2" ]
then
chmod +x centos.sh
else
echo "Sorry we can not support your OS now..."
exit
fi
