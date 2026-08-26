from docx import Document
from docx.opc.constants import RELATIONSHIP_TYPE as RT
from zipfile import ZipFile
import re
import sys, datetime, logging,os
import glob
from pathlib import Path

#region "import common functions, init logging"
"""
import importlib
spec = importlib.util.spec_from_file_location("inc", "\\UCQ-CYBER-P002\\secops\\git\\cyber\\common\\inc.py")
inc = importlib.util.module_from_spec(spec)
sys.modules["inc"] = inc
spec.loader.exec_module(inc)
logfile  = datetime.today().strftime('%Y%m%d') + "-" + (os.path.basename(__file__).replace(".py", ".log"))
inc.initLogging(logfile, logging.INFO)
"""
#endregion

searchstrings = ["reviltest", "10.14.121.123"]
searchpattern = "|".join(searchstrings)

directory = r'C:\Users\AdamS\**'

for filepath in glob.iglob(directory, recursive=True):
    #print(filename)
    if (filepath.endswith(".docx")):
        print("checking " + filepath)
        with ZipFile(filepath) as myzip:
            for z in myzip.filelist:
                if (z.filename =='_rels/.rels'):
                    f = myzip.open(z.filename)
                    content = f.read()
                    matches = re.findall(searchpattern, content.decode('utf-8'))
                    if (matches):
                        print(matches)
                    
