#sudo kill -USR2 $(pidof suricata)

#sudo kill $(ps aux | grep 'suricata' | awk '{print $2}')

sudo iptables -F
sudo iptables -X

#sudo iptables -t nat -I PREROUTING -p tcp --dport 443 -j REDIRECT --to-ports 3000
sudo iptables -t nat -I PREROUTING -p tcp --dport 80 -j REDIRECT --to-ports 3000
sudo iptables-save
#sudo service fail2ban start
