#!/bin/bash


#checkping
cmd=`dig ubuntu.com | grep "ANSWER: 1"`
    if [[ "$cmd" == *"ANSWER: 1"* ]]; then
        echo "DNS settings is ok"  
    else
        echo "writing DNS settings"
        echo "nameserver 8.8.8.8" | sudo tee -a /etc/resolv.conf
    fi    
#install packages
    sudo apt install bind9 -y

#backup
    sudo mv /etc/bind backups

    sudo cp -r includes/bind /etc/bind

#maindomain
    read -p "Enter your domain name without www: " userdomain
    autoip=$(hostname -I | cut -d' ' -f1)
    read -p "Ok... and enter a ip for it (default $autoip): " userip
    if [ "$userip" = "" ]
    then
    userip=$autoip
    fi
    sudo sed -i -e "s/domainv/$userdomain/g" /etc/bind/named.conf.default-zones
    sudo cp includes/examplezone /etc/bind/$userdomain
    sudo sed -i -e "s/domainv/$userdomain/g" /etc/bind/$userdomain
    sudo sed -i -e "s/ipv/$userip/g" /etc/bind/$userdomain
    sudo systemctl enable bind9
    sudo systemctl restart bind9
echo -e "${BLUE}Install finished!${NC}"
