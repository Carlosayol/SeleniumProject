import logging
class LoggerDemoConsole():

    def testLog(self):

        logger = logging.getLogger(LoggerDemoConsole.__name__)
        logger.setLevel(logging.INFO)

        #Handlers
        chandler = logging.StreamHandler()
        chandler.setLevel(logging.INFO)

        #Formatter
        formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s at Line %(lineno)d',
                    datefmt='%m/%d/%Y %H:%M:%S')
        chandler.setFormatter(formatter)

        #Agregar Handler al logger
        logger.addHandler(chandler)

        logger.debug("debug message")
        logger.info("info message")
        logger.warning("warning message")
        logger.error("error message")
        logger.critical("critical message")

demo = LoggerDemoConsole()
demo.testLog()