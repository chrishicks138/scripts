sudo kill -USR2 $(pidof suricata)

sudo kill $(ps aux | grep 'suricata' | awk '{print $2}')

sudo iptables -F
sudo iptables -X

sudo iptables -I FORWARD -j NFQUEUE


sudo iptables -I INPUT -p tcp --sport 80 -j NFQUEUE
sudo iptables -I OUTPUT -p tcp --dport 80 -j NFQUEUE

sudo iptables -I INPUT -p tcp --sport 6697 -j NFQUEUE
sudo iptables -I OUTPUT -p tcp --dport 6697 -j NFQUEUE

sudo iptables -I INPUT -p tcp --sport 5000 -j NFQUEUE
sudo iptables -I OUTPUT -p tcp --dport 5000 -j NFQUEUE

sudo iptables -I INPUT -p tcp --sport 443 -j NFQUEUE
sudo iptables -I OUTPUT -p tcp --dport 443 -j NFQUEUE

sudo iptables -I INPUT -p tcp --sport 22 -j NFQUEUE
sudo iptables -I OUTPUT -p tcp --dport 22 -j NFQUEUE

sudo iptables -I INPUT -p tcp --sport 80 -j NFQUEUE
sudo iptables -I OUTPUT -p tcp --dport 80 -j NFQUEUE

sudo iptables -I INPUT -p tcp --sport 443 -j NFQUEUE
sudo iptables -I OUTPUT -p tcp --dport 443 -j NFQUEUE

sudo iptables -I INPUT -p udp --sport 68 -j NFQUEUE
sudo iptables -I OUTPUT -p udp --dport 68 -j NFQUEUE

sudo iptables -I INPUT -p udp --sport 60000:61000 -j NFQUEUE
sudo iptables -I OUTPUT -p udp --dport 60000:61000 -j NFQUEUE

sudo ip6tables -I INPUT -p tcp --sport 22 -j NFQUEUE
sudo ip6tables -I OUTPUT -p tcp --dport 22 -j NFQUEUE

sudo ip6tables -I INPUT -p udp --sport 123 -j NFQUEUE
sudo ip6tables -I OUTPUT -p udp --dport 123 -j NFQUEUE

sudo iptables -t nat -I PREROUTING -p tcp --dport 80 -j REDIRECT --to-ports 3000
#sudo iptables -t nat -I PREROUTING -p tcp --dport 80 -j REDIRECT --to-ports 5000

sudo iptables -L

sudo suricata -D -q 0


sudo service fail2ban start

sudo iptables-save
