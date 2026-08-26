import os,sys
from datetime import datetime
import logging
logger = logging.getLogger("testmodule")



def ShowTestMessage(msg):
    logging.info("at the begining of the function call")
    logging.error("yeah, thats bad")
    logging.info("at the end of hte call") 