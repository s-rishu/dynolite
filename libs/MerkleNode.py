import hashlib

class MerkleNode:
    def __init__(self, config):
        self.config = config
        self.parent: MerkleNode = config["parent"] if "parent" in config else None
        self.left: MerkleNode = config["left"] if "left" in config else None
        self.right: MerkleNode = config["right"] if "right" in config else None
        self.data = config["data"] if "data" in config else {}
        self.type = config["type"] if "type" in config else "leaf"
        self.range = config["range"] if "range" in config else (0, 2**128-1)
        self.hash()
    
    def is_leaf_node(self): 
        return self.type == "leaf"
    
    def has_parent(self):
        return self.parent != None
    
    def hash(self):
        if self.is_leaf_node():
            self.digest = hashlib.md5(str(self.data).encode()).digest()
        else:
            self.digest = hashlib.md5(self.left.digest + self.right.digest).digest()

        if self.parent != None:
            self.parent.hash()

    def __str__(self):
        if self.is_leaf_node():
            return "leaf: [%s,%s)=>%s" % (self.range[0], self.range[1], self.digest)
        
        return ("node: [%s,%s)=>%s\n left: { %s }\n right: { %s }" 
                % (self.range[0], self.range[1], self.digest, self.root.left, self.root.right))