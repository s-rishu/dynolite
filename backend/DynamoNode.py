from libs import ProcessNode

class DynamoNode(ProcessNode):
    def __init__(self):
        super().__init__({"merkle_config":{}, "preference_list": []})

    