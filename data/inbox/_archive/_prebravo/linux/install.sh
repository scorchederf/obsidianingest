#!/bin/bash

# install packages from apt

sudo atp update && apt install pure-ftpd 





# add user and group for ftp
groupadd ftpgroup
useradd -g ftpgroup -d /dev/null -s /etc ftpuser
pure-pw useradd kali -u ftpuser -g ftpgroup
pure-pw mkdb
cd /etc/pure-ftpd/auth/
ln -s ../conf/PureDB 60pdb
mkdir -p /ftphome
chown -R ftpuser:ftpgroup /ftphome/
systemctl restart pure-ftpd

