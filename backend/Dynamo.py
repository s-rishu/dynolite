import libs
import utils
from backend import DynamoNode
from libs import Ring

# Only create one per instance of dynamo store.
class Dynamo:
    view = []
    virtual = 5
    ring = []

    def __init__(self, R, W, N):
        self.R = R
        self.W = W
        self.N = N
        for _ in range(2*N):
            Dynamo.view.append(DynamoNode())

        Dynamo.ring = Ring(Dynamo.view, Dynamo.virtual)

        
        



    