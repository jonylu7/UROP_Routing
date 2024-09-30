
filelocation="waypoint_graph.json"
import json
from VectorModel import Vector
from tools import loadJSONFile,saveFile

def modifyNodeLocation(filedata,whichnode:int,newlocations:Vector):
    filedata["node_locations"][whichnode]=newlocations.toListWithZ()
    return filedata


def connectNode(filedata,nodeA:int,nodeB:int):
    if nodeB not in filedata["graph"][str(nodeA)]["edges"]:
        filedata["graph"][str(nodeA)]["edges"].append(nodeB)
    if nodeA not in filedata["graph"][str(nodeB)]["edges"]:
        filedata["graph"][str(nodeB)]["edges"].append(nodeA)
    return filedata


def addNewNodeAndConnectToPrevNode(filedata,newnodelocation:Vector,prevnode:int):
    filedata["node_locations"].append(newnodelocation.toListWithZ())

    newNodeIndex=len(filedata["node_locations"])-1
    filedata["graph"][str(newNodeIndex)]={"edges":[prevnode]}
    filedata=connectNode(filedata,prevnode,newNodeIndex)
    return filedata

def mergeWaypointGraphs(mergeintofile,mergefromfile):
    startIndex=len(mergeintofile["node_locations"])
    mergeintofile["node_locations"]=mergeintofile["node_locations"]+mergefromfile["node_locations"]

    for i in range(len(mergefromfile["graph"])):
        value=mergefromfile["graph"][str(i)]
        newEdgeList=[]
        for nodeIndex in value["edges"]:
            newEdgeList.append(nodeIndex+startIndex)
        mergeintofile["graph"][str(i+startIndex)]={"edges":newEdgeList}
    return mergeintofile

def duplicateWaypointGraphs(filedata,relocatebottomleft):
    return

def main():
    intoFileLocation="main_path/main_waypoint_path.json"
    fromFileLocation="bottom_path/bottom_waypoint_path.json"
    saveFileLocation=""
    intoFile=loadJSONFile(intoFileLocation)
    fromFile=loadJSONFile(fromFileLocation)
    newFile=mergeWaypointGraphs(intoFile,fromFile)
    saveFile(newFile,"_merge_1",saveFileLocation)




if __name__=="__main__":
    main()