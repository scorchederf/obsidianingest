import testmodule
import os,sys
from datetime import datetime
import logging


#region "Logging"
# Adopted from https://stackoverflow.com/a/35804945/1691778
# Adds a new logging method to the logging module
def addLoggingLevel(levelName, levelNum, methodName=None):
    if not methodName:
        methodName = levelName.lower()

    if hasattr(logging, levelName):
        raise AttributeError("{} already defined in logging module".format(levelName))
    if hasattr(logging, methodName):
        raise AttributeError("{} already defined in logging module".format(methodName))
    if hasattr(logging.getLoggerClass(), methodName):
        raise AttributeError("{} already defined in logger class".format(methodName))

    def logForLevel(self, message, *args, **kwargs):
        if self.isEnabledFor(levelNum):
            self._log(levelNum, message, args, **kwargs)

    def logToRoot(message, *args, **kwargs):
        logging.log(levelNum, message, *args, **kwargs)

    logging.addLevelName(levelNum, levelName)
    setattr(logging, levelName, levelNum)
    setattr(logging.getLoggerClass(), methodName, logForLevel)
    setattr(logging, methodName, logToRoot)


# addLoggingLevel("GOOD", logging.INFO - 5)
def _init_logger(logpath):
    level    = logging.INFO
    format   = "%(asctime)s [%(levelname)-10s] %(message)s [%(pathname)s %(funcName)s %(lineno)d]"
    logfile  = logpath          #os.path.join("C:\\dev\\git\\bravo\\code\\python\\stub" + dtestamp + "-stub.log")
    handlers = [logging.FileHandler(logfile), logging.StreamHandler()]
    logging.basicConfig(level = level, format = format, handlers = handlers )#, datefmt=dtefmt)
#endregion

dtefmt   = '%Y-%m-%d %H:%M:%S,.%f'
timestamp = datetime.today().strftime('%Y-%m-%dT%H:%M:%S')
dtestamp = datetime.today().strftime('%Y%m%d')
logpath = ("C:\\dev\\git\\bravo\\code\\python\\stub\\" + dtestamp + "-stub.log")
_init_logger(logpath)
logger = logging.getLogger('rootapp')
logger.info("inline script started")

testmodule.ShowTestMessage("calling a function from testmodule")


