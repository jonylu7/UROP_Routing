from tools import loadJSONFile
class WaypointGraph:
    nodeLocations=[]
    graph={} ##edges
    def __init__(self,graph,nodeLocations):
        self.nodeLocations=nodeLocations
        self.graph=graph

    def loadFile(self,filelocatin):
        loadJSONFile(filelocation)

    def saveAs(self,filelocation):
        return
