---
id: kali.md
tags: [offsec, kali, pen-200]
created: 2023-01-13 11:56
---
# PEN-200: 5 Bash scripting

backlinks:
- [[offsec/pen200/4/lab]]

sources:

---

always has a shebang
- -x shows additional debugging details
```bash
#!/bin/bash
```



```bash
# in this example, the single-quote-enclosed declaration of greeting preserved the exact value of our text and did not interpret the space as a command delimiter.
greeting1='hello world'
echo $greeting1
hello world

# In the double-quote-enclosed declaration of greeting2, Bash expanded the greeting1 variable to its value of “Hello World”, honoring the special meaning of the dollar sign character
greeting2="New $greeting1"
echo $greeting2
New hello world


#command substitution, which allows us to take the output of a command or program (what would normally be printed to the screen) and have it saved as the value of a variable
# the command gets executed in a subshell and therefore wont have access to all the variables, session, etc
user =$(whoami)
echo $user
kali

```

# arguments
```bash

#!/bin/bash
# arg.sh
echo "The first two arguments are $1 and $2"

# -----------

#shell
chmod +x arg.sh
./arg.sh hello there
The first two arguments are hello and there


```

# user input

```bash

#!/bin/bash
# input.sh

# -p for prompt
# -sp for secure prompt
read -p 'what is your name?' response
echo "hello " $response ", time to work"

# -----

```

# if else elif

VERY IMPORTANT TO REMEMBER THE SPACES

```shell

age=15

if [ $age -lt 16 ]
then
    echo "you are too young"
elif [ $age -gt 60 ]
then
    echo "hats off to you, respect"
else
    echo "welcome"
fi


```

# boolean operators

```bash

if [ $USER == 'kali' ] && [ $HOSTNAME == 'kali' ]
then
    echo 'yo kali dude'
else
    echo 'move along'
fi

if [ $USER == 'kali' ] || [ $USER == 'bob' ]
then
    echo 'its either kali or bob logging in'
else
    echo 'not sure who this is'
fi



```

# for loops

```bash


for v in example.csv example.txt
do 
    cat $v 
done


for VARIABLE in file1 file2 file3
do
    command1 on $VARIABLE
    command2
    commandN
done


for OUTPUT in $(Linux-Or-Unix-Command-Here)
do
    command1 on $OUTPUT
    command2 on $OUTPUT
    commandN
done






for ip in $(seq 1 10); do echo 10.11.1.$ip; done

10.11.1.1
10.11.1.2
10.11.1.3
10.11.1.4
10.11.1.5
10.11.1.6
10.11.1.7
10.11.1.8
10.11.1.9
10.11.1.10

for i in {1..10}; do echo 10.11.1.$i; done
10.11.1.1
10.11.1.2
10.11.1.3
10.11.1.4
10.11.1.5
10.11.1.6
10.11.1.7
10.11.1.8
10.11.1.9
10.11.1.10
           
```

# while loops

```bash

counter=1


#while [ $counter -le 10 ]
while [ $counter -lt 10 ]
do
    echo "10.11.1.$counter"
    ((counter++))
done


10.11.1.1
10.11.1.2
10.11.1.3
10.11.1.4
10.11.1.5
10.11.1.6
10.11.1.7
10.11.1.8
10.11.1.9


```

# functions

```bash

name='joe'
printme() {
    #variables can be set to local 
    local name='bob'
    echo 'printed'
}
printme

# -------

passarg() {
    echo "todays random number from a script is $1"
}

passarg $RANDOM

# -------

returnme() {
    echo 'setting global $? value by returning'
    return $RANDOM
}
returnme
echo "The previous function return a value of dollarsignquestionmark $?"

# output
setting global $? value by returning
The previous function return a value of dollarsignquestionmark 32486

# -------






```

|Variable Name |Description|
|:----|:----|
|$0 |The name of the Bash script|
|$1 - $9 |The first 9 arguments to the Bash script|
|$# |Number of arguments passed to the Bash script|
|$@ |All arguments passed to the Bash script|
|$? |The exit status of the most recently run process|
|$$ |The process ID of the current script|
|$USER |The username of the user running the script|
|$HOSTNAME |The hostname of the machine|
|$RANDOM |A random number|
|$LINENO |The current line number in the script|



|Operator |Description: Expression True if...|
|:----|:----|
|!EXPRESSION |The EXPRESSION is false.|
|-n STRING |STRING length is greater than zero|
|-z STRING |The length of STRING is zero (empty)|
|STRING1 != STRING2 |STRING1 is not equal to STRING2|
|STRING1 = STRING2 |STRING1 is equal to STRING2|
|INTEGER1 -eq INTEGER2 |INTEGER1 is equal to INTEGER2|
|INTEGER1 -ne INTEGER2 |INTEGER1 is not equal to INTEGER2|
|INTEGER1 -gt INTEGER2 |INTEGER1 is greater than INTEGER2|
|INTEGER1 -lt INTEGER2 |INTEGER1 is less than INTEGER2|
|INTEGER1 -ge INTEGER2 |INTEGER1 is greater than or equal to INTEGER 2|
|INTEGER1 -le INTEGER2 |INTEGER1 is less than or equal to INTEGER 2|
|-d FILE |FILE exists and is a directory|
|-e FILE |FILE exists|
|-r FILE |FILE exists and has read permission|
|-s FILE |FILE exists and it is not empty|
|-w FILE |FILE exists and has write permission|
|-x FILE |FILE exists and has execute permission|
|    Table 2 - Common test command operators|
