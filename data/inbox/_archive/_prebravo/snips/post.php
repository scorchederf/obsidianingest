<?php
    # if running from python you will need to allow the apache www-data user write permissions to this directory
    # sudo chown www-data:www-data <thisfolder>

    $data = "Client IP Address: " . $_SERVER['REMOTE_ADDR'] . "\n";
    $data .= file_get_contents('php://input');
    $data .= "---------------------------------\n\n";
    file_put_contents('captured.txt', print_r($data, true), FILE_APPEND | LOCK_EX);
?>