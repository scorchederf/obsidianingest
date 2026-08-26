import sys
import shlex #only needed if apachelogs cannot be pip'd
import os 
import subprocess

#USAGE
#  python3 ./ApacheLogParser.py access.log output.log

def check_ping(ip):
    try:
        subprocess.check_call(
            ['ping', '-c', '1', '-q', ip], stdout=subprocess.DEVNULL
        )
        #subprocess.check_call(
        #    ['ping', '-c', '1', ip],
        #    "/dev/null",  # suppress output
        #    "/dev/null"
        #)
        return True
    except subprocess.CalledProcessError:
        return False





threeocts = sys.argv[1]
start=int(sys.argv[2])
end=int(sys.argv[3])


while start <= end:
    ip=threeocts+"."+str(start)
    if check_ping(ip):
        print (ip)
    start += 1




'''
threeocts=$1
start=$2
end=$3


for ip in $(seq $start $end); 
do 
    ip="$threeocts.$ip"
    if ping -c 1 $ip &> /dev/null
    then
        echo $ip
    #   else
    #   echo "error"
    fi

    #echo 10.11.1.$ip; 
done

'''
