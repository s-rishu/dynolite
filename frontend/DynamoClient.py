from libs import Message, ProcessNode
from utils import VectorClock
from backend import Dynamo
from emulator import Network
from typing import List
import logging
import random

logger = logging.getLogger("dynolite")

class DynamoClient:
    def __init__(self, name, R, W, N):
        logger.info("Creating Dynamo Client node: %s", name)
        self.dynamo = Dynamo(R, W, N)
        self.name = name
    
    def get(self, key, destNode: ProcessNode = None):
        if destNode is None:
            destNode = random.choice(Dynamo.view)
        
        msg = Message("ClientGet", {"key": key, "type": "get", "sender": self.name})
        
        Network.send(self.name, destNode, msg)
        
        return msg

    def put(self, key, value, metadata: List[VectorClock], destNode: ProcessNode = None):
        if destNode is None:
            destNode = random.choice(Dynamo.view)
        
        metadata = VectorClock.merge(metadata)
        msg = Message("ClientPut", {"key": key, "value": value, "metadata": metadata})

        Network.send(self.name, destNode, msg)

        return msg

    def __str__(self):
        return "Dynamo Client Node: %s" % self.name
