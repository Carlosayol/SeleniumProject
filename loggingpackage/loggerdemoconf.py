import logging
import logging.config

class LoggerDemoConf():

    def testLog(self):
        #logger goes here xd
        logging.config.fileConfig('logging.conf')
        logger = logging.getLogger(LoggerDemoConf.__name__)

        logger.debug("debug message")
        logger.info("info message")
        logger.warning("warning message")
        logger.error("error message")
        logger.critical("critical message")

demo = LoggerDemoConf()
demo.testLog()