#!/bin/bash
#checkping
cmd=`dig ubuntu.com | grep "ANSWER: 1"`
    if [ "$cmd" == "1"; thencmd=`dig ubuntu.com | grep "ANSWER: 1"`
    if [[ "$cmd" == *"ANSWER: 1"* ]]; then
    echo DNS settings is ok  
    else
    echo writing DNS settings
    echo "nameserver 8.8.8.8" | sudo tee -a /etc/resolv.conf
    fi    

#open ports    
    sudo firewall-cmd --zone=public --add-port=53/tcp --permanent
    sudo firewall-cmd --zone=public --add-port=53/udp --permanent
    sudo firewall-cmd --reload 

    sudo iptables -I INPUT -p tcp -m tcp --dport 53 -j ACCEPT
    sudo iptables -I INPUT -p udp -m tcp --dport 53 -j ACCEPT
    sudo service iptables save

#install packages
    sudo yum install bind -y

#backup
    mkdir backups
    sudo mv /etc/named.conf backups/named.conf
    sudo cp includes/namedcentos.conf /etc/named.conf

#maindomain
    read -p "Enter your domain name without www: " userdomain
    read -p "ok... and enter a ip for it: " userip
    sudo sed -i -e "s/domainv/$userdomain/g" /etc/named.conf
    sudo cp includes/examplezone /var/named/$userdomain
    sudo sed -i -e "s/domainv/$userdomain/g" /var/named/$userdomain
    sudo sed -i -e "s/ipv/$userip/g" /var/named/$userdomain
    sudo systemctl enable named
    sudo systemctl restart named
echo -e "${BLUE}Install finished!${NC}"
