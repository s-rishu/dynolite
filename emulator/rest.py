import logging
from libs import ProcessNode

logger = logging.getLogger("dynolite")

class REST:
    def __init__(self):
        logger.info("Creating a REST util to simulate message passing")

    @staticmethod
    def send(_from, to: ProcessNode, msg):
        to.rcv(_from, msg)

