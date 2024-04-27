import hashlib
import binascii
import bisect
from libs import ProcessNode
from typing import List

class Ring:
    def __init__(self, nodelist: List[ProcessNode], virtual):
        ring = []
        for node in nodelist:
            for i in range(virtual):
                nodestring = "%s:%d" % (node, i)
                ring.append((hashlib.md5(nodestring.encode()).digest(), node))

        self.ring = sorted(ring, key=lambda x: x[0])
        self.hashes = [p[0] for p in self.ring]
    
    def find_nodes(self, key, count = 1, avoid = set()):
        avoided = set()
        nodes = set()

        hash = hashlib.md5(str(key)).digest()

        jdx = idx = bisect.bisect(self.hashes, hash)

        while count > 0:
            n = self.ring[jdx][1]
            if n in avoid: 
                avoided.add(n)
            else:
                nodes.add(n)
                count -= 1
            jdx = (jdx + 1) % (len(self.hashes))
            if idx == jdx:
                break

        return list(nodes), list(avoided)
    
    def __str__(self):
        return "Ring: " + ", ".join(["(%s, %s)" %
                         (binascii.hexlify(n[0]), n[1]) for n in self.ring])
