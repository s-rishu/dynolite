import logging
logger = logging.getLogger("dynolite")

class Timer(object):
    def __init__(self):
        pass
    
    @classmethod
    def reset_all(cls):
        """removes all pending timers"""
        pass

    @classmethod
    def set_timer(cls, node, callback=None):
        """sets a timer for the given node"""
        pass

    @classmethod
    def cancel_timer(cls, tmsg):
        """cancels the timer identified by tmsg"""
        pass
    
    @classmethod
    def trigger_timer(cls):
        """pops and triggers the first timer in the queue"""
        pass