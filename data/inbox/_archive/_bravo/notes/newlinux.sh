


sudo apt install locate
sudo updatedb


# install seclists
cd /usr/share && git clone https://github.com/danielmiessler/SecLists.git


# vmware mounted drives not visible?
#   sudo mount-shared-folders



#install fonts
# https://download.jetbrains.com/fonts/JetBrainsMono-2.304.zip




#Oracle-Tools-Setup
sudo apt-get install libaio1 python3-dev alien python3-pip -y
git clone https://github.com/quentinhardy/odat.git
cd odat/
git submodule init
git submodule update
sudo apt install oracle-instantclient-basic oracle-instantclient-devel oracle-instantclient-sqlplus -y
pip3 install cx_Oracle
sudo apt-get install python3-scapy -y
sudo pip3 install colorlog termcolor pycryptodome passlib python-libnmap
sudo pip3 install argcomplete && sudo activate-global-python-argcomplete