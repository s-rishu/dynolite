import logging
from libs import ProcessNode

logger = logging.getLogger("dynolite")

class REST:
    idNodeMap = {}

    def __init__(self):
        logger.info("Creating a REST util to simulate message passing")

    @staticmethod
    def send(_from, to, msg):
        node: ProcessNode = REST.idNodeMap[to]
        node.rcv(_from, msg)
    
    @staticmethod
    def addNode(id, node: ProcessNode):
        REST.idNodeMap[id] = node
