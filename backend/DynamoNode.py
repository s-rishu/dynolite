from libs import ProcessNode
import copy
class DynamoNode(ProcessNode):
    def __init__(self):
        super().__init__({"merkle_config":{}, "preference_list": []})
        # Each node may act as "Coordinator". 
        # Hence, store pending requests and responses to make commit decisions
        self.pending_put_rsp = {}
        self.pending_put_msg = {}
        self.pending_get_rsp = {}
        self.pending_get_msg = {}

        self.sent_put = {}
        self.sent_get = {}

        # contains the local view of ring
        self.view = []

    def set_view(self, new_view):
        self.view = copy.deepcopy(new_view)

    def update_view(self, updated_node):
        updated_view = []
        for node in self.view:
            if node.id == updated_node.id:
                updated_view.append(updated_node)
            else:
                updated_view.append(node)
        
        self.view = updated_view

    def store_put(self, key, value, metadata):
        self.merkle[key] = (value, metadata)
    
    def store_get(self, key):
        if key in self.merkle:
            return self.merkle[key]
        return (None, None)
    