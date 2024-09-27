
class WaypointGraph:
    nodeLocations=[]
    graph={} ##edges

    def __init__(self,graph,nodeLocations):
        self.nodeLocations=nodeLocations
        self.graph=graph
