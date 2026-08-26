#!/bin/bash

sudo groupadd ftpgroup
sudo useradd -g ftpgroup -d /dev/null -s /etc ftpuser
sudo pure-pw useradd offsec -u ftpuser -d /ftphome
sudo pure-pw mkdb
# unsure of these commands    cd /etc/pure-ftpd/auth/
# unsure of these commands    sudo ln -s ../conf/PureDB 60pdb
sudo mkdir -p /ftphome
sudo chown -R ftpuser:ftpgroup /ftphome/
sudo systemctl restart pure-ftpd





#sudo apt-get --purge remove pure-ftpd


#sudo apt update && sudo apt install pure-ftpd