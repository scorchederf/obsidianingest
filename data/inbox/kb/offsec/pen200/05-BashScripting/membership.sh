#!/bin/bash
 
read -p "" username
read -p "" usergroup

if [ $( getent passwd $username ) ]
then
  userexists=true
else
  userexists=false
fi

if [ $(getent group $usergroup) ]
then
    groupexists=true
else
    groupexists=false
fi

#echo "username $username exists $userexists"
#echo "usergroup $usergroup exists $groupexists"

if [ $userexists = 'true' ] && [ $groupexists = 'true' ]
then
    # check if user already in group
    if [[ $( groups $username | grep $usergroup ) ]]
    then
        echo 'Membership valid!'
    else
        echo 'Membership invalid but available to join.'
    fi
else 
    if [ $userexists = 'false' ] || [ $groupexists = 'false' ]
    then
        echo 'One exists, one does not. You figure out which.'
    else 
        echo 'Both are not found - why are you even asking me this?'
    fi 
fi
