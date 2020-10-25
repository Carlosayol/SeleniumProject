import logging

logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s at Line %(lineno)d ',
                    level=logging.DEBUG,
                    datefmt='%m/%d/%Y %H:%M:%S')

logging.warning("warning message")
logging.info("info message")
logging.error("error message")