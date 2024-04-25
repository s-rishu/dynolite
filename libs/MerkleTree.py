from libs import MerkleNode
import math
import hashlib
from typing import List
import logging
logger = logging.getLogger("dynolite")

class MerkleTree:
    def __init__(self, config):
        self.config = config
        self.key_range = config["key_range"] if "key_range" in config else (0, 2**128 - 1)

        logger.debug("Building merkle tree root for (%d, %d)", self.key_range[0], self.key_range[1])
        
        depth = config["depth"] if "depth" in config else 12
        initdata = config["initdata"] if "initdata" in config else {}
        self.leaves: List[MerkleNode] = self.init_leaves(initdata, depth)

        self.root: MerkleNode = self.construct_tree(depth)

    def init_leaves(self, initdata: dict, depth):
        tot_leaves = 2**depth
        self.leaf_size = math.ceil((self.key_range[1] - self.key_range[0] + 1)/tot_leaves)

        leaf_nodes = []
        for i in range(tot_leaves):
            min_range = self.key_range[0] + i*self.leaf_size
            max_range = min(min_range + self.leaf_size, self.key_range[1]+1)

            leaf_data = {}

            for k, v in initdata.items():
                hash_key = self.keyhash(k)
                if hash_key < max_range and hash_key >= min_range: 
                    leaf_data[k] = v
        
            node_config = {"type": "leaf", "data": leaf_data, "range": (min_range, max_range)}
            leaf_nodes.append(MerkleNode(node_config))

        return leaf_nodes
        
    def construct_tree(self, depth):
        nodes = self.leaves
        if len(nodes) == 0: 
            return None
        
        while depth > 0:
            new_nodes = []
            sz = len(nodes)
            for i in range(0, sz, 2):
                left: MerkleNode = nodes[i]
                right: MerkleNode  = nodes[i+1] if i < sz - 1 else None
                node_config = {"type": "imm", "left": left, "right": right}
                left.parent = right.parent = parent = MerkleNode(node_config)
                new_nodes.append(parent)
            nodes = new_nodes
            depth -= 1
        
        if len(nodes) == 1 and not nodes[0].has_parent():
            return nodes[0]
        
        logger.error("Failed to create merkle tree root for (%d, %d)", self.key_range[0], self.key_range[1])

        return None

    def find_leaf(self, key):
        hash_key = self.keyhash(key)
        if not (hash_key < self.key_range[1] and hash_key >= self.key_range[0]):
            logger.error("Key %s: and hash %s: out of range for merkle tree", str(key), str(hash_key)) 
        else: 
            idx = hash_key // self.leaf_size

            logger.info("Key: %d found at node id: %d", key, idx)
            return self.leaves[idx]
    
    def keyhash(self, key):
        hashval = hashlib.md5(str(key).encode())
        return int(hashval.hexdigest(), 16)
    
    def __str__(self):
        return self.root