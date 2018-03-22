#!/bin/bash
#check os
    read -p "You are using Ubuntu. is that so?[Y/n]: " userif
    if [ "$userif" = Y ] || [ "$userif" = y ] ; then
    echo
    else
    echo -e "${RED}Sorry... it is just for Ubuntu${NC}"
    exit
    fi

#checkping
    if [ "`ping -c 1 google.com`" ]
    then
    echo DNS settings is ok  
    else
    echo writing DNS settings
    echo "nameserver 8.8.8.8" | sudo tee -a /etc/resolv.conf
    fi

#open ports    
	sudo ufw allow 53
	sudo ufw status verbose

#install packages
    sudo apt install bind* -y

#backup
    sudo mv /etc/bind backups

    sudo cp -r includes/bind /etc/bind

#maindomain
    read -p "Enter your domain name without www: " userdomain
    read -p "ok... and enter a ip for it: " userip
    sudo sed -i -e "s/domainv/$userdomain/g" /etc/bind/named.conf.default-zones
    sudo cp includes/examplezone /etc/bind/$userdomain
    sudo sed -i -e "s/domainv/$userdomain/g" /etc/bind/$userdomain
    sudo sed -i -e "s/ipv/$userip/g" /etc/bind/$userdomain
    sudo systemctl enable bind9
    sudo systemctl restart bind9
echo -e "${BLUE}Install finished!${NC}"
