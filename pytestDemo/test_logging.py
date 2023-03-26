import logging


def test_logginDemo():
    # create a logger object, add __name__ in params to include the name of the file whihc is executed
    logger = logging.getLogger(__name__)

    # create a file hancer object ehich has the name and location of the file that will be generated
    file_handler = logging.FileHandler("logfile.log")

    # adding the format for the lof in Formatter
    # %(asctime)s : get the date
    # %(levelname)s : prints what lvl it is fromthe log defied below, is warning is executed then it comets there
    # %(name)s : print the name of the file bien executed
    # %(message)s : print the message defined in the logger.[logType]("[message]")
    formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s %(message)s")

    # add formater to file handler
    file_handler.setFormatter(formatter)

    # add the handler to the logfger object, now inclued file name and location and format
    logger.addHandler(file_handler)

    # set level from where log will start loggin, ex setlevel(WARNING) then degub and info wont be printing
    logger.setLevel(logging.INFO)

    logger.debug("a debug stament is executed")
    logger.info("information statemnet")
    logger.warning("shows a warning but do not stops the code from running")
    logger.error("error statment, stop executioon")
    logger.critical("bigger error, CRITICAL")
