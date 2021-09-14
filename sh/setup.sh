tar xzf webservers.tar.gz
cd webservers/adonis
sh node-setup.sh
sudo apt-get install fail2ban
cd ../../scripts/sh
sh suricata-setup.sh
sudo sh nfq-iptables.sh
