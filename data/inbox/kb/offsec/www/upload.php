    
    <?php
        //save as upload.php
        //check uploads folder exists and permissions applied
        //  sudo chown www-data: /var/www/uploads
    
    $uploaddir = '/home/kali/Documents/git/bravo/offsec/www/uploads';

    $uploadfile = $uploaddir . $_FILES['file']['name'];

    move_uploaded_file($_FILES['file']['tmp_name'], $uploadfile)
    ?>
