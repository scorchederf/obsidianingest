---
title: Kali Linux Bash Scripting
aliases: []
tags:
- topic/bash-scripting
- tool/kali
category: study_notes
status: draft
date_created: '2026-08-27'
date_modified: '2026-08-27'
source: notes.md
related_tools:
- '[[bash]]'
related_techniques: []
related_tactics: []
related_services: []
related_os: []
related_notes: []
mitre_tactic: ''
mitre_technique: ''
real_path: ''
port: ''
protocol: ''
os: linux
---

# Kali Linux Bash Scripting

## Shebang and Basic Syntax
Always use a shebang at the beginning of a bash script to specify the interpreter. The single-quote-enclosed declaration of greeting preserved the exact value of the text and did not interpret the space as a command delimiter. The double-quote-enclosed declaration of greeting2 expanded the greeting1 variable to its value, honoring the special meaning of the dollar sign character.

```bash
#!/bin/bash

greeting1='hello world'
echo $greeting1
hello world

greeting2="New $greeting1"
echo $greeting2
New hello world
```

Command substitution allows the output of a command or program to be saved as the value of a variable.

```bash
user=$(whoami)
echo $user
kali
```

## Arguments
Bash scripts can accept arguments. The first two arguments are accessible via $1 and $2.

```bash
#!/bin/bash
# arg.sh
echo "The first two arguments are $1 and $2"

# shell
chmod +x arg.sh
./arg.sh hello there
The first two arguments are hello and there
```

## User Input
Bash scripts can accept user input using the `read` command with the `-p` option for a prompt or the `-sp` option for a secure prompt.

```bash
#!/bin/bash
# input.sh

read -p 'what is your name?' response
echo "hello \
$response ", time to work
```

## Conditional Statements
Bash scripts can use `if`, `elif`, and `else` statements to make decisions based on conditions. The `&&` and `||` operators can be used to combine conditions.

```bash
age=15

if [ $age -lt 16 ]
then
    echo 'you are too young'
elif [ $age -gt 60 ]
then
    echo 'hats off to you, respect'
else
    echo 'welcome'
fi
```

## Loops
Bash scripts can use `for` and `while` loops to iterate over a set of values or conditions.

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
```

The `for` loop can also be used to generate a range of values.

```bash
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

The `while` loop can be used to execute a block of code as long as a condition is true.

```bash
counter=1

while [ $counter -lt 10 ]
do
    echo "10.11.1.$counter"
    ((counter++))
done
```

## Functions
Bash scripts can define functions to encapsulate reusable code. Functions can return values using the `return` statement.

```bash
name='joe'
printme() {
    #variables can be set to local 
    local name='bob'
    echo 'printed'
}
printme

passarg() {
    echo 'todays random number from a script is $1'
}

passarg $RANDOM

returnme() {
    echo 'setting global $? value by returning'
    return $RANDOM
}
returnme
echo "The previous function return a value of dollarsignquestionmark $?"
```

Table 2 - Common test command operators
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

Table 3 - Common test command operators
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

## References
- kali.md

