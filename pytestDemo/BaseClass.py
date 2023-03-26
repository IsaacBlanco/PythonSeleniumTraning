import inspect
import logging


class BaseClass:
    def getLogger(self):
        # __name__ will add the name of the base class
        #change to get the name of the test that invoked the looger
        loger_name = inspect.stack()[1][3]
        logger = logging.getLogger(loger_name)
        file_handler = logging.FileHandler("logfile.log")
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

        logger.setLevel(logging.DEBUG)
        return logger
