




Just leave the damn fonts alone. 
TO RESTORE FONTS CAUSE YOU DONT LISTEN
- Close all terminals
- Open ~/.config/qterminal.org folder
- Change fontFamily to Fira Code and exit.

Install Jet Brains Mono
```shell
cd Documents && 
mkdir JetBrainsMono &&
cd JetBrainsMono &&
wget https://download.jetbrains.com/fonts/JetBrainsMono-1.0.0.zip && 
unzip JetBrainsMono-1.0.0.zip &&
sudo mv JetBrainsMono-*.ttf /usr/share/fonts/
fc-cache -f -v
cd ../
pwd
```