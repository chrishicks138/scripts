#rm backup/* &&
tar czvf backup/scripts.tar.gz scripts &&
tar czf backup/webservers.tar.gz webservers &&
tar czvf backup/data.tar.gz data &&
sudo tar czf backup/etc.tar.gz /etc &&
sudo tar czf backup/var.tar.gz /var
