#!/bin/bash
n=$1                  #$1
ip=$2                   #$2
IFS='.' read -a ipa <<< $ip
counter=0
max=$((counter + n))
while [ $counter -le $n ]
do
    
    newip="${ipa[0]}.${ipa[1]}.${ipa[2]}.${counter}"
    #echo $p
    if [ "$newip" != "$ip" ] && [ $counter -lt 255 ] ;
    then
        echo $newip
    fi
    ((counter++))  
done























#!/bin/bash

IP="$1"     # IPv4 address
N="$2"      # Number of addresses to generate

# Extract the subnet address and netmask from the given IP
subnet=$(echo "$IP" | awk -F '.' '{print $1"."$2"."$3}')
netmask=$(echo "$IP" | awk -F '.' '{print $4}')
IFS='.' read -a ipa <<< $IP
# Calculate the first usable host address and the last usable host address
first_host=$netmask
last_host=254

# Ensure N is within the valid range
if (( N > last_host )); then
    N=$last_host
fi

# Generate the list of N IPv4 addresses
for (( i = 0; i < N; i++ )); do
    host=$((first_host + i))
    address="$subnet.$host"
    
    # Check if the generated address is the given IP
    if [[ $address == $IP ]]; then
        break
    fi
    
    echo "$address"
done