#sudo kill -USR2 $(pidof suricata)

kill $(ps aux | grep 'suricata' | awk '{print $2}')

sudo iptables -F

sudo iptables -I INPUT -p udp --sport 60000:61000 -j ACCEPT
sudo iptables -I OUTPUT -p udp --dport 60000:61000 -j ACCEPT

sudo ip6tables -I INPUT -p tcp --sport 22 -j ACCEPT
sudo ip6tables -I OUTPUT -p tcp --dport 22 -j ACCEPT

sudo ip6tables -I INPUT -p udp --sport 123 -j ACCEPT
sudo ip6tables -I OUTPUT -p udp --dport 123 -j ACCEPT

sudo iptables -I INPUT -p tcp --sport 22 -j ACCEPT
sudo iptables -I OUTPUT -p tcp --dport 22 -j ACCEPT

sudo iptables -t nat -I PREROUTING -p tcp --dport 80 -j REDIRECT --to-ports 3000

sudo suricata -D -q 0
