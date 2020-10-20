sudo apt-get -y install libpcre3 libpcre3-dbg libpcre3-dev build-essential autoconf automake libtool libpcap-dev libnet1-dev libyaml-0-2 libyaml-dev zlib1g zlib1g-dev libmagic-dev libcap-ng-dev libjansson-dev pkg-config &&
sudo apt-get -y install libnetfilter-queue-dev &&


wget http://www.openinfosecfoundation.org/download/suricata-3.1.tar.gz &&
tar -xvzf suricata-3.1.tar.gz &&
cd suricata-3.1 &&


sudo ./configure --enable-nfqueue --prefix=/usr --sysconfdir=/etc --localstatedir=/var &&
sudo make &&
sudo make install &&
sudo ldconfig

wget http://rules.emergingthreats.net/open/suricata/emerging-all.rules
sudo cp -v emerging-all.rules /etc/suricata/rules/
