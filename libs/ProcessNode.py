import logging
from libs import MerkleTree
from utils import VectorClock

logger = logging.getLogger("dynolite")

class ProcessNode:
    total_nodes = 0
    
    def __init__(self, config):
        self.config = config
        self.alive = True
        self.id = ProcessNode.getCounter(self)
        self.merkle = MerkleTree(config["merkle_config"])
        self.clock = VectorClock()
        self.preference_list = config["preference_list"]
        logger.debug("Created Node with id: %d", self.id)

    def fail(self):
        self.alive = False
        logger.debug("Failed Node with id: %d", self.id)
    
    def recover(self):
        self.alive = True
        logger.debug("Recovered Node with id: %d", self.id)

    def rcv(self, _from, msg):
        pass

    @staticmethod
    def getCounter():
        ProcessNode.total_nodes += 1
        return ProcessNode.total_nodes



