#Searches for .docx, xlsx and pptx files and captures relationship information
#specific to extracting information from word documents
import os
import zipfile
#other tools useful in extracting the information from our document
import re
#to pretty print our xml:s
import xml.dom.minidom


print('<?xml version="1.0" encoding="UTF-8" standalone="yes" ?><Relationships>')

for dirpath, dirs, files in os.walk(directory):	
    for filename in files:
        f = os.path.join(dirpath,filename)
        if (f.endswith('.docx') or f.endswith(".xlsx") or f.endswith(".pptx")):
            try:
                #print(f)
                document = zipfile.ZipFile(f)
                for i in document.namelist():
                    if '.rels' in i:
                        #print (i)
                        d=document.read(name=i)
                        dom = xml.dom.minidom.parseString(d)
                        for rel in dom.getElementsByTagName('Relationship'):
                            rel.setAttribute('filename', f) 
                            print (rel.toprettyxml(), end='')
            except:
                a = "bad"


print ("</Relationships>")