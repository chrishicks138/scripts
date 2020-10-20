VER=6.0.0
sudo apt-get install libpcre3 libpcre3-dbg libpcre3-dev build-essential libpcap-dev libnet1-dev libyaml-0-2 libyaml-dev pkg-config zlib1g zlib1g-dev libcap-ng-dev libcap-ng0 make libmagic-dev libjansson-dev libnss3-dev libgeoip-dev liblua5.1-dev libhiredis-dev libevent-dev python-yaml rustc cargo libnetfilter-queue-dev libnetfilter-queue1 libnetfilter-log-dev libnetfilter-log1 libnfnetlink-dev libnfnetlink0 autoconf automake libtool libpcap-dev libnet1-dev libyaml-dev libjansson4 pkg-config oinkmaster
wget "https://www.openinfosecfoundation.org/download/suricata-$VER.tar.gz" 
tar -xvzf "suricata-$VER.tar.gz" 
cd "suricata-$VER" 
./configure  --enable-geopip --enable-nfqueue --prefix=/usr --sysconfdir=/etc --localstatedir=/var
make
sudo make install-full
sudo ldconfig
