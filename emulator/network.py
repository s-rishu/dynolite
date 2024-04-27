import logging
from libs import ProcessNode

logger = logging.getLogger("dynolite")

class Network:
    def __init__(self):
        logger.info("Creating a network util to simulate message passing")

    @staticmethod
    def send(_from, to: ProcessNode, msg):
        to.rcv(_from, msg)

