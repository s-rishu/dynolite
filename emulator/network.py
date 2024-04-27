import logging
from libs import ProcessNode

logger = logging.getLogger("dynolite")

class Network:
    def __init__(self):
        logger.info("Creating a network..")

    @staticmethod
    def send(_from, to: ProcessNode, msg):
        #TODO: remove
        to.rcv(_from, msg)

    @classmethod
    def make_unreachable(cls, from_nodes, to_nodes):
        """cuts connection from all from nodes to all to nodes"""
        pass

    @classmethod
    def is_reachable(cls, from_node, to_node):
        """returns true of a connection exists between from and to node"""
        pass

    @classmethod
    def reset(cls):
        """resets entire network"""
        pass

    @classmethod
    def send_message(cls, msg):
        """send message"""
        pass

    @classmethod
    def cancel_timers_to(cls, dest):
        """cancel all timers waiting for a response from dest node"""
        pass

    @classmethod
    def run_tasks(cls):
        """run all tasks in the queue"""
        pass





