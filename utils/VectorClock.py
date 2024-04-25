class VectorClock: 
    def __init__(self):
        self.clock = {}

    def incClock(self, nodeId):
        if nodeId in self.clock: 
            self.clock[nodeId] += 1
        else:
            self.clock[nodeId] = 1
    
    def __str__(self):
        return "{%s}" % ", ".join(["Node %d:%d" % (nodeId, self.clock[nodeId])
                                   for nodeId in sorted(self.clock.keys())])
    
    def __eq__(self, other):
        return self.clock == other.clock

    def __lt__(self, other):
        for node in self.clock:
            if node not in other.clock:
                return False
            if self.clock[node] > other.clock[node]:
                return False
        return True

    def __ne__(self, other):
        return not (self == other)

    def __le__(self, other):
        return (self == other) or (self < other)

    def __gt__(self, other):
        return (other < self)

    def __ge__(self, other):
        return (self == other) or (self > other)
