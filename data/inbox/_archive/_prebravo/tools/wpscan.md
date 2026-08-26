---
id: tools-apache2
tags: ["kali", "tool", "exfiltration", "secure"]
created: 2023-01-12 11:56
---
# tools-apache2

backlinks: [[]]

sources:

---
first, uninstall all Wpscan with the following command:

gem uninstall wpscan
apt remove wpscan

then, use the following command to fix it:

sudo apt-get update
gpg --keyserver hkp://keys.gnupg.net --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3 7D2BAF1CF37B13E2069D6956105BD0E739499BDB
\curl -sSL https://get.rvm.io | bash -s stable --ruby --ignore-dotfiles
\curl -sSL https://get.rvm.io | bash -s stable --rails
gem install rails 5
source /usr/local/rvm/scripts/rvm
rvm reinstall ruby 2.6.0
rvm install "ruby-2.5.3"
gem install wpscan

Make sure it is installed correctly with this command:

which ruby
ruby --version
rails -v

It works now.