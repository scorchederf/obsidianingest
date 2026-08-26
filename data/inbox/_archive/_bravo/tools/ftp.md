# ftp

  - ports
    - port 21 is control
    - port 20 is data
  - active or passive
    - active is when the client tells the server which port to use
    - passive is when the server tells the client which port to use
  - ftp creds are in cleartext
  - `/etc/ftpusers` contains list of users who cannot log in via ftp
  - Trivial File Transfer Protocol (TFTP) uses udp instead of tcp
    - requires no authentication
    - | Commands | Description                                                                                                                            |
|----------|----------------------------------------------------------------------------------------------------------------------------------------|
| connect  | Sets the remote host, and optionally the port, for file transfers.                                                                     |
| get      | Transfers a file or set of files from the remote host to the local host.                                                               |
| put      | Transfers a file or set of files from the local host onto the remote host.                                                             |
| quit     | Exits tftp.                                                                                                                            |
| status   | Shows the current status of tftp, including the current transfer mode (ascii or binary), connection status, time-out value, and so on. |
| verbose  | Turns verbose mode, which displays additional information during file transfer, on or off.                                             |

  - common misconfigurations
  - 
  | Setting                      | Description                                                                        |
|------------------------------|------------------------------------------------------------------------------------|
| anonymous_enable=YES         | Allowing anonymous login?                                                          |
| anon_upload_enable=YES       | Allowing anonymous to upload files?                                                |
| anon_mkdir_write_enable=YES  | Allowing anonymous to create new directories?                                      |
| no_anon_password=YES         | Do not ask anonymous for password?                                                 |
| anon_root=/home/username/ftp | Directory for anonymous.                                                           |
| write_enable=YES             | Allow the usage of FTP commands: STOR, DELE, RNFR, RNTO, MKD, RMD, APPE, and SITE? |
