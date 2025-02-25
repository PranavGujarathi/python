import logging

logging.basicConfig(filename="newFile.txt",level=logging.DEBUG)
logging.debug("this indicates debuggging information")
logging.info("this indicates important information")
logging.error("this indicates error information")
logging.warning("this indicates warning information")
logging.critical("this indicates critical information")