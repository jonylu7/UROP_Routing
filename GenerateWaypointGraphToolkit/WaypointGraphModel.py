from tools import loadJSONFile
class WaypointGraph:
    nodeLocations=[]
    graph={} ##edges
    def __init__(self,graph,nodeLocations):
        self.nodeLocations=nodeLocations
        self.graph=graph

    def loadFile(self,filelocatin):
        loadJSONFile(filelocation)

    def saveAs(self,exportlocation):
        graphJSON = {}
        for key, value in self.graph.items():
            graphJSON[str(key)] = {"edges": value}
        data = {"node_locations": self.nodeLocations, "graph": graphJSON}
        json_object = json.dumps(data, indent=2)

        # Writing to sample.json
        with open(exportlocation, "w") as outfile:
            outfile.write(json_object)
        return
