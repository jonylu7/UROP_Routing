
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
    filedata=loadJSONFile("overall_route.json")
    filedata = connectNode(filedata, 126,6)
    filedata = connectNode(filedata, 127,5)
    filedata = connectNode(filedata, 140,67)
    filedata = connectNode(filedata, 150,72)
    filedata = connectNode(filedata, 148,184)
    filedata = connectNode(filedata, 142,174)
    filedata = connectNode(filedata, 140,167)
    filedata = connectNode(filedata, 167,64)
    filedata = connectNode(filedata, 157,59)
    filedata = connectNode(filedata, 142,165)
    filedata = connectNode(filedata, 159,191)
    filedata = connectNode(filedata, 165,201)
    filedata = connectNode(filedata, 174,201)
    filedata = connectNode(filedata, 199,176)
    filedata = connectNode(filedata, 176,208)
    filedata = connectNode(filedata, 182,218)
    filedata = connectNode(filedata, 208,235)
    filedata = connectNode(filedata, 210,233)
    filedata = connectNode(filedata, 225,252)
    filedata = connectNode(filedata, 227,250)
    filedata = connectNode(filedata, 193, 225)
    filedata = connectNode(filedata, 119, 235)

    saveFile(filedata, "_modify_1", filelocation)




if __name__=="__main__":
    main()